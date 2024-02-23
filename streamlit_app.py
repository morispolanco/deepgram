import whisper
from pydub import AudioSegment

def transcribe_audio(audio_file):
    # Cargar el modelo Whisper
    model = whisper.load_model("base")
    
    try:
        # Transcribir el archivo de audio
        result = model.transcribe(audio_file)
        transcription = result["text"]
        return transcription
    except Exception as e:
        print("Error al transcribir el audio:", str(e))
        return None

def main():
    # Nombre del archivo de audio
    audio_file = "audio.m4a"
    
    # Cargar el archivo de audio usando pydub
    sound = AudioSegment.from_file(audio_file)
    # Convertir a formato wav, ya que Whisper puede manejar wav
    wav_audio_file = "audio.wav"
    sound.export(wav_audio_file, format="wav")
    
    # Transcribir el archivo de audio
    transcription = transcribe_audio(wav_audio_file)
    
    # Imprimir la transcripción
    if transcription:
        print("Transcripción del audio:")
        print(transcription)
    else:
        print("No se pudo transcribir el audio.")

if __name__ == "__main__":
    main()
