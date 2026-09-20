import os
import chromadb
from back.embed import obtener_embedding

DIRECTORIO_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_CHROMA = os.path.join(DIRECTORIO_BASE, "chroma")

cliente_chroma = chromadb.PersistentClient(path=RUTA_CHROMA)
coleccion = cliente_chroma.get_or_create_collection(name="rag_documents")


def agregar_fragmentos_chroma(fragmentos: list[dict]):
    if not fragmentos:
        return

    ids = [f["id"] for f in fragmentos]
    documentos = [f["texto"] for f in fragmentos]
    vectores = [obtener_embedding(f["texto"]) for f in fragmentos]
    metadatos = [{"fuente": f["fuente"], "indice_fragmento": f["indice_fragmento"]} for f in fragmentos]

    coleccion.add(
        ids=ids,
        documents=documentos,
        embeddings=vectores,
        metadatas=metadatos
    )


def consultar_top_k(pregunta: str, top_k: int = 3) -> dict:
    vector = obtener_embedding(pregunta)
    return coleccion.query(
        query_embeddings=[vector],
        n_results=top_k
    )

