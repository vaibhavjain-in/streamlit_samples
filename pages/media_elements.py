import streamlit as st

st.header('Display image using st.image')

st.image('files/India_gate.png',caption='India Gate',width=500)
st.divider()

st.header('Display video')
video_file = open('files/India_flag.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.divider()

# display audio
st.header('Display audio')
audio_file = open('files/bells.wav','rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes,format='audio/ogg')
