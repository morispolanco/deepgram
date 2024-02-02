import streamlit as st
from deepgram import DeepgramClient, PrerecordedOptions

DEEPGRAM_API_KEY = '5ca1ee9b3731dfbc099204fdd514be946e21f7c6'

def transcribe_audio(audio_file):
    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)

        options = PrerecordedOptions(
            model="whisper-medium",
            language="es",
            smart_format=True,
            punctuate=True,
            paragraphs=True,
        )

        response = deepgram.listen.prerecorded.v('1').transcribe_file(audio_file, options)
        return response

    except Exception as e:
        return f'Exception: {e}'

def main():
    st.title("Transcripción de Archivos de Voz con Deepgram")

    uploaded_file = st.file_uploader("Cargar archivo de audio", type=['wav', 'mp3', 'm4a'])

    if uploaded_file is not None:
        st.write("Transcribiendo el archivo de audio...")
        response = transcribe_audio(uploaded_file)
        st.write("Texto transcribido:")
        st.write(response)

if __name__ == '__main__':
    main()
