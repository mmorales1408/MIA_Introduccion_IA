import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

clave_api = os.getenv("GOOGLE_API_KEY")
cliente = genai.Client(api_key=clave_api) if clave_api else None


def generar_respuesta_rag(pregunta: str, fragmentos_recuperados: list[dict]) -> tuple[str, bool]:
    if not cliente:
        raise ValueError("GOOGLE_API_KEY no configurada.")

    texto_contexto = ""
    for indice, fragmento in enumerate(fragmentos_recuperados, start=1):
        texto_contexto += f"[{indice}] Fuente: {fragmento['fuente']}\n{fragmento['texto']}\n\n"

    instrucciones = f"""Eres un asistente estricto de soporte basado en documentos.
Tu única tarea es responder a la pregunta del usuario utilizando EXCLUSIVAMENTE la evidencia proporcionada en el siguiente contexto.

Reglas estrictas:
1. Responde en español.
2. Cita la fuente usada al final de la frase relevante usando el formato [1], [2], etc.
3. Si el contexto NO contiene información suficiente para responder a la pregunta de manera completa, responde EXACTAMENTE: "No tengo evidencia suficiente en los documentos para responder a esta pregunta." y no agregues nada más.
4. No utilices tu conocimiento previo fuera del contexto dado

Contexto disponible:
{texto_contexto}

Pregunta del usuario: {pregunta}
Respuesta:"""

    respuesta = cliente.models.generate_content(
        model="gemini-3.6-flash",
        contents=instrucciones
    )

    texto_respuesta = respuesta.text.strip() if respuesta.text else ""
    abstenido = "No tengo evidencia suficiente" in texto_respuesta

    return texto_respuesta, abstenido

