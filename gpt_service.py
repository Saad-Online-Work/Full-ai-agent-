import openai
import json

# Load API key from config/settings.json
with open("config/settings.json") as f:
    config = json.load(f)
openai.api_key = config["OPENAI_API_KEY"]

def generate_script(transcript_text):
    """
    Input: transcript from Whisper
    Output: improved script + new ideas
    """
    prompt = f"Convert this transcript into a professional video script:\n{transcript_text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content