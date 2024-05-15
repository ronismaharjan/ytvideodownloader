from pytube import YouTube
import os
from moviepy.editor import AudioFileClip

# Function to download video
def download_video(download_folder):
    """Download the video from the given url"""
    stream_dictionary = {}
    available_resolutions = []
    available_video_streams = youtube.streams.filter(
        file_extension="mp4", type="video", progressive=True)

    # Adding each classes into new dictionary
    for stream_classes in available_video_streams:
        stream_dictionary[stream_classes.resolution] = stream_classes
    for key in stream_dictionary:
        available_resolutions.append(key)

    # Taking resolution input form user
    choosed_resolution = input(
        f"Available resolutions:{('/'.join(available_resolutions))}\nType the resolution you want to download:")
    selected_stream = stream_dictionary[choosed_resolution]

    # Downloading the given resolution video
    print("Downloading...")
    selected_stream.download(download_folder)
    print("Download Completed..")

# Function to download audio
def download_audio(download_folder):
    """Downloads the mp3 of given youtube link"""
    print("Downloading...")
    audio_stream = youtube.streams.get_by_itag(251)
    audio_stream.download(download_folder, filename="audio.webm")
    youtube_title = youtube.title.replace("|", "")

    input_file = os.path.join(download_folder, "audio.webm")
    output_file = os.path.join(download_folder, f"{youtube_title}.mp3")

    mp3_converter(input_file, output_file)
    os.remove(input_file)
    print("Download Completed..")

# Function to convert the downloaded audio to mp3 format
def mp3_converter(input_file, output_file):
    try:
        # Load the WebM file
        audio_clip = AudioFileClip(input_file)

        # Write the audio clip to an MP3 file
        audio_clip.write_audiofile(output_file, codec='mp3')

    except Exception as e:
        print("An error occurred during conversion:", e)

# The main function
def downloader(file_type, download_folder):
    if file_type == "v":
        download_video(download_folder)

    elif file_type == "a":
        download_audio(download_folder)
    else:
        print("We only support audio and video type")

# Main loop
download_folder = "downloads"
is_on = True
while is_on:
    try:
        URL = input("URL: ")
        if URL == "exit":
            is_on = False
        youtube = YouTube(URL)
        user_choice = input(
            f"Do you want to download\n{youtube.title} by: {youtube.author}\nType 'y' or 'n': ").lower()

        if user_choice == "y":
            user_type = input(
                f"To Download\nType 'a' for audio and 'v' for video: ").lower()
            downloader(user_type, download_folder)
        elif user_choice == "n":
            is_on = False

    except Exception as e:
        print(f"An error occurred: {e}")
