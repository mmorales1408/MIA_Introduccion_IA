import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from back.chunk import extraer_texto_archivo, crear_fragmentos
from back.store import agregar_fragmentos_chroma, consultar_top_k, coleccion
from back.generate import generar_respuesta_rag

app = FastAPI(title="RAG Service API", version="1.0")


class SolicitudConsulta(BaseModel):
    pregunta: str
    top_k: int = 3


@app.get("/health")
def verificar_salud():
    try:
        total = coleccion.count()
        return {"estado": "ok", "chroma_disponible": True, "total_fragmentos": total}
    except Exception as error:
        return {"estado": "error", "chroma_disponible": False, "detalle": str(error)}


@app.post("/ingest")
async def ingestar_documentos(archivos: list[UploadFile] = File(...)):
    carpeta_temporal = "temp_uploads"
    os.makedirs(carpeta_temporal, exist_ok=True)
    
    total_archivos = len(archivos)
    total_fragmentos_creados = 0

    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta_temporal, archivo.filename)
        with open(ruta_archivo, "wb") as buffer:
            shutil.copyfileobj(archivo.file, buffer)

        texto = extraer_texto_archivo(ruta_archivo)
        fragmentos = crear_fragmentos(texto, nombre_fuente=archivo.filename)
        if fragmentos:
            agregar_fragmentos_chroma(fragmentos)
            total_fragmentos_creados += len(fragmentos)

        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)

    if os.path.exists(carpeta_temporal):
        os.rmdir(carpeta_temporal)

    return {
        "mensaje": "Ingesta completada exitosamente.",
        "archivos_procesados": total_archivos,
        "fragmentos_indexados": total_fragmentos_creados
    }


@app.post("/query")
def consultar_rag(solicitud: SolicitudConsulta):
    if not solicitud.pregunta.strip():
        raise HTTPException(status_code=400, detail="La pregunta no puede estar vacía.")

    resultados = consultar_top_k(solicitud.pregunta, top_k=solicitud.top_k)
    
    documentos = resultados.get("documents", [[]])[0]
    metadatos = resultados.get("metadatas", [[]])[0]
    distancias = resultados.get("distances", [[]])[0]
    identificadores = resultados.get("ids", [[]])[0]

    if not documentos:
        return {
            "respuesta": "No hay documentos cargados en la base de datos.",
            "citas": [],
            "abstenido": True
        }

    citas = []
    for i in range(len(documentos)):
        citas.append({
            "id": identificadores[i],
            "texto": documentos[i],
            "fuente": metadatos[i].get("fuente", "desconocido"),
            "distancia": round(float(distancias[i]), 4) if distancias else None
        })

    respuesta, abstenido = generar_respuesta_rag(solicitud.pregunta, citas)

    return {
        "respuesta": respuesta,
        "citas": citas,
        "abstenido": abstenido
    }

