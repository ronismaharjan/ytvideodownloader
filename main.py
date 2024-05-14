from pytube import YouTube
import os
from moviepy.editor import AudioFileClip

# Function to convert to mp3


def convert_to_mp3(input_path, output_path):
    try:

        audio_clip = AudioFileClip(input_file_path)

        # Save the audio as MP3
        audio_clip.write_audiofile(output_file_path)

        # Close the video clip
        audio_clip.close()

        print("Conversion to MP3 completed.")
    except Exception as e:
        print("MoviePy error:", e)


stream = ''
DOWNLOAD_FOLDER = r"C:\Users\Home\Downloads"
is_on = True

# Loop until exit or close
while is_on:
    # Take the video url
    URL = input("URL: ")
    if URL == "exit" or URL == "close":
        is_on = False
    else:
        try:
            yt = YouTube(URL)

            # Ask user if they want to download or not
            user_choice = input(
                f"{yt.title} by: {yt.author}.\nDo you want to download 'y' or 'n': ").lower()

            # If want to download ask which format
            format_type = input(
                "Which format 'a' for mp3 and 'v' for mp4: ").lower()

            # IF format is video then download at highest qualit
            if format_type == "v":
                video_quality = str(
                    input("For Quality Type: '1080p', '720p', '360p': ").lower())
                stream = yt.streams.get_by_resolution(video_quality)

            # If format is in audio
            if format_type == "a":
                stream = yt.streams.get_by_itag(140)

            # Show user downloading ....
            print("Downloading...")
            # Download video
            if format_type == "v":
                stream.download(output_path=DOWNLOAD_FOLDER)
            else:
                stream.download(output_path=DOWNLOAD_FOLDER)
            # Convert video into mp3 file
                input_file_path = rf"{DOWNLOAD_FOLDER}\{yt.title}.mp4"
                output_file_path = rf"{DOWNLOAD_FOLDER}\{yt.title}_by_{yt.author}.mp3"
                convert_to_mp3(input_file_path, output_file_path)
            # Delete the video file
                os.remove(input_file_path)

            # Show download complete
            print("Download completed..")
        except Exception as e:
            print(f"Error: {e}")
