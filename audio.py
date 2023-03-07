import streamlit as st
from gtts import gTTS

var1 = gTTS(text="वर्तमान में वक्रासन कर रहे हैं", lang='hi')
var1.save("wel1.mp3")


def play(file):
    audio_file = open(file, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format=f'{file}/mp3')


if __name__ == '__main__':
    play("wel1.mp3")
