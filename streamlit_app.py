import speech_recognition as sr

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()

    # Leer el archivo de audio
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    # Utilizar Google Web Speech API para transcribir el audio
    try:
        text = recognizer.recognize_google(audio_data, language="es-ES")
        return text
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return None
    except sr.RequestError as e:
        print("Error en la solicitud a la API; {0}".format(e))
        return None

def main():
    # Nombre del archivo de audio
    audio_file = "audio.m4a"  # Ajusta el nombre de tu archivo de audio aquí
    
    # Transcribir el archivo de audio
    transcription = transcribe_audio(audio_file)
    
    # Imprimir la transcripción
    if transcription:
        print("Transcripción del audio:")
        print(transcription)
    else:
        print("No se pudo transcribir el audio.")

if __name__ == "__main__":
    main()
