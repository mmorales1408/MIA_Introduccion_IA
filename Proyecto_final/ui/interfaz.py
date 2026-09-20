import streamlit as st
import httpx

URL_API = "http://localhost:8000"

st.set_page_config(
    page_title="Proyecto final",
    page_icon="logo/uady-logo.png",  # Reemplaza esto con tu emoji, ruta local o URL
    layout="wide"
)
st.title("Asistente basado en documentos - Mario Morales")

with st.sidebar:
    st.header("Estado de la API")
    try:
        resp_salud = httpx.get(f"{URL_API}/health", timeout=3.0)
        if resp_salud.status_code == 200:
            datos_salud = resp_salud.json()
            st.success("API Conectada")
            st.write(f"Chunks indexados: {datos_salud.get('total_fragmentos', 0)}")
        else:
            st.error("Error al conectar con la API")
    except Exception:
        st.error("No se pudo conectar con FastAPI en http://localhost:8000")

    st.divider()
    st.header("Sube tus documentos aquí")
    archivos_subidos = st.file_uploader(
        "Sube archivos (.txt, .md, .pdf)", 
        accept_multiple_files=True
    )

    if st.button("Procesar e Ingestar"):
        if archivos_subidos:
            archivos_a_enviar = [("archivos", (a.name, a.getvalue(), a.type)) for a in archivos_subidos]
            with st.spinner("Procesando documentos..."):
                try:
                    respuesta = httpx.post(f"{URL_API}/ingest", files=archivos_a_enviar, timeout=60.0)
                    if respuesta.status_code == 200:
                        datos_ingesta = respuesta.json()
                        st.success(f"Ingesta lista: {datos_ingesta['fragmentos_indexados']} chunks creados.")
                        st.rerun()
                    else:
                        st.error(f"Error en ingesta: {respuesta.text}")
                except Exception as error:
                    st.error(f"Error de conexión: {error}")
        else:
            st.warning("Selecciona al menos un archivo.")

st.subheader("Consulta")
pregunta = st.text_input("Pregunta:")
top_k = st.slider("Top K evidencias", min_value=1, max_value=5, value=3)

if st.button("Consultar"):
    if pregunta.strip():
        with st.spinner("Generando respuesta..."):
            try:
                respuesta = httpx.post(
                    f"{URL_API}/query", 
                    json={"pregunta": pregunta, "top_k": top_k},
                    timeout=30.0
                )
                if respuesta.status_code == 200:
                    datos = respuesta.json()
                    
                    st.markdown("### Respuesta:")
                    if datos.get("abstenido"):
                        st.warning(datos["respuesta"])
                    else:
                        st.write(datos["respuesta"])

                    st.markdown("---")
                    st.markdown("### Evidencias:")
                    for indice, cita in enumerate(datos.get("citas", []), start=1):
                        with st.expander(f"[{indice}] {cita['fuente']} (Score: {cita['distancia']})"):
                            st.write(cita["texto"])
                else:
                    st.error(f"Error en la consulta: {respuesta.text}")
            except Exception as error:
                st.error(f"Error de comunicación con la API: {error}")
    else:
        st.warning("Ingresa una pregunta.")

