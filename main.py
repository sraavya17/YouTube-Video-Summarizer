import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os
import re

load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")
# for model in genai.list_models():
#     print(model.name)

# Configure Gemini
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# Function to get YouTube video transcript
def summarizer_yt_video(video_url):
    try:
        match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", video_url)
        video_id = match.group(1) if match else None
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry['text'] for entry in transcript])
        prompt = f"Summarize the following YouTube video transcript:\n\n{text}\n\nSummary:"
        response = model.generate_content(prompt)
    except Exception as e:
        return f"An error occurred: {e}"

    return response.text

video_url = "https://www.youtube.com/watch?v=OFPwDe22CoY"
summary = summarizer_yt_video(video_url)
print("Summary of the YouTube video:")
print(summary)


