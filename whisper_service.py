import whisper

# Load Whisper model once
model = whisper.load_model("base")

def transcribe_audio(file_path):
    """
    Input: file_path -> path to audio file
    Output: text transcription
    """
    result = model.transcribe(file_path)
    return result['text']