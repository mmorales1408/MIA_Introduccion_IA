import os
from pypdf import PdfReader


def extraer_texto_archivo(ruta_archivo: str) -> str:
    extension = os.path.splitext(ruta_archivo)[1].lower()
    if extension == ".pdf":
        lector = PdfReader(ruta_archivo)
        contenido_paginas = []
        for pagina in lector.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                contenido_paginas.append(texto_pagina)
        return "\n".join(contenido_paginas)
    
    with open(ruta_archivo, "r", encoding="utf-8", errors="ignore") as archivo:
        return archivo.read()


def crear_fragmentos(texto: str, nombre_fuente: str, tamano_fragmento: int = 300, solapamiento: int = 50) -> list[dict]:
    palabras = texto.split()
    fragmentos = []
    paso = tamano_fragmento - solapamiento
    indice = 0

    for i in range(0, len(palabras), paso):
        palabras_fragmento = palabras[i:i + tamano_fragmento]
        if not palabras_fragmento:
            continue
        
        fragmentos.append({
            "id": f"{nombre_fuente}_fragmento_{indice}",
            "texto": " ".join(palabras_fragmento),
            "fuente": nombre_fuente,
            "indice_fragmento": indice
        })
        indice += 1
        
        if i + tamano_fragmento >= len(palabras):
            break

    return fragmentos
