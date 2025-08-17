from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip
import os

def create_video(audio_path, output_path="static/final_video.mp4"):
    """
    Simple demo: attach audio to a template video + add text
    """
    # Ensure static folder exists
    os.makedirs("static", exist_ok=True)

    # Template video (can be stock footage)
    video = VideoFileClip("backend/static/template.mp4")
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio)

    # Example: Add text overlay
    txt_clip = TextClip("AI Generated Video", fontsize=50, color='white')
    txt_clip = txt_clip.set_position('center').set_duration(video.duration)
    final = CompositeVideoClip([video, txt_clip])

    final.write_videofile(output_path, fps=24)
    return output_path