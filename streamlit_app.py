import streamlit as st
from openai import OpenAI

st.title("Transcripción de Audio en Español")

uploaded_file = st.file_uploader("Cargar archivo de audio en español", type=["mp3"])

if uploaded_file is not None:
    audio_bytes = uploaded_file.read()
    client = OpenAI()
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_bytes,
        language="es"
    )
    st.write(transcript.text)
