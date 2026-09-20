import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

clave_api = os.getenv("GOOGLE_API_KEY")
cliente = genai.Client(api_key=clave_api) if clave_api else None


def obtener_embedding(texto: str, modelo: str = "gemini-embedding-2") -> list[float]:
    if not cliente:
        raise ValueError("GOOGLE_API_KEY no configurada en el entorno.")
    
    respuesta = cliente.models.embed_content(
        model=modelo,
        contents=texto.strip() or " "
    )
    return list(respuesta.embeddings[0].values)
