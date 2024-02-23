from deepgram import DeepgramClient, PrerecordedOptions 
 
DEEPGRAM_API_KEY = 'b1496eba2a1921f08280492628fdbc90c89b353c' 
 
AUDIO_URL = { 
  'url': 'https://static.deepgram.com/examples/Bueller-Life-moves-pretty-fast.wav' 
} 
 
def main(): 
  try: 
    deepgram = DeepgramClient(DEEPGRAM_API_KEY) 
 
    options = PrerecordedOptions(
      model="whisper-medium", 
      language="es", 
      smart_format=True, 
    ) 
 
    response = deepgram.listen.prerecorded.v('1').transcribe_url(AUDIO_URL, options) 
    print(response) 
 
  except Exception as e: 
    print(f'Exception: {e}') 
 
if __name__ == '__main__': 
  main()
