# Sistema RAG con FastAPI, ChromaDB y Streamlit

Proyecto de Recuperación y Generación Aumentada (RAG) utilizando Google Gemini para la generación de embeddings y síntesis de respuestas, ChromaDB como base de datos vectorial, FastAPI para el backend y Streamlit para la interfaz de usuario.
***
***
# Instalación y Configuración

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar la clave de Google Gemini

Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
GOOGLE_API_KEY=tu_api_key_aqui
```

---

## Ejecución

Para utilizar el sistema es necesario ejecutar el backend y el frontend en dos terminales independientes.

### Terminal 1 - Backend (FastAPI)

```bash
uvicorn main:app --reload --port 8000
```
**Nota:** Aunque suene obvio, es necesario estar en el directorio en donde se encuentr el archivo de main.py

El servicio estará disponible en `http://localhost:8000`.

### Terminal 2 - Frontend (Streamlit)

```bash
streamlit run ui/interfaz.py
```
**Nota:** Al igual que en el punto anterior, asegúrate de estar en el directorio correcto del archivo.

La interfaz estará disponible en `http://localhost:8501`.

---

## Uso

1. Verifica en la barra lateral que la API se encuentre conectada.
2. Sube archivos (.pdf, .txt, .md) y haz clic en **Procesar e Ingestar**. Es totalmente necesario hacer click en el sistema de ingesta para que el archivo sea cargado correctamente.
3. Ingresa tu consulta en el campo de texto, selecciona el valor de `top_k` deseado y presiona **Consultar**. Al igual que en el punto anterior, es totalmente necesario darle click al botón de **Consultar** para poder obtener una respuesta.

***
***
El reporte final se puede encontrar [en el documento del proyecto final](proyecto_final.md) en donde se responden todas las preguntas solicitadas en la descripción del proyecto así como se adjuntan capturas de su uso.