import streamlit as st
from pytube import YouTube
import time

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    return stream.default_filename

st.title('📥 YouTube Video Downloader by Rizwan')

video_url = st.text_input('Enter the URL of the YouTube video you wish to download:')

if st.button('Download'):
    try:
        # Display a message and start a progress bar
        st.info('Starting download...')
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)  # Simulate a delay (Replace with actual download progress if possible)
            progress_bar.progress(percent_complete + 1)
        
        filename = download_video(video_url)
        
        st.success(f'Video downloaded successfully: {filename}')
        st.info('Please check your device\'s download folder.')
    except Exception as e:
        st.error(f'An error occurred: {e}')
