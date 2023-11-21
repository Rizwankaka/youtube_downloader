import streamlit as st
from pytube import YouTube

def download_video(url, path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=path)
    return stream.default_filename

st.title('YouTube Video Downloader')

video_url = st.text_input('Enter the URL of the YouTube video you wish to download:')
download_path = st.text_input('Enter the download path:')

if st.button('Download'):
    try:
        filename = download_video(video_url, download_path)
        st.success(f'Video downloaded successfully: {filename}')
    except Exception as e:
        st.error(f'An error occurred: {e}')
