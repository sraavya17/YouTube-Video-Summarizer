import streamlit as st
from main import summarizer_yt_video

st.set_page_config(page_title="YouTube Video Summarizer", layout="wide", page_icon=":video_camera:")
st.title("YouTube Video Summarizer")
st.write("Enter the URL of a YouTube video to get its summary.")
video_url = st.text_input("YouTube video URL")
if st.button("Summarize"):
    if video_url:
        with st.spinner("Generating summary..."):
            summary = summarizer_yt_video(video_url)
            st.subheader("Summary:")
            st.write(summary)
    else:
        st.error("Please enter a valid YouTube video URL.")


