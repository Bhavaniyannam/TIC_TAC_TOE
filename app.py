import streamlit as st

st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")

st.title("🎮 Tic-Tac-Toe Game")
st.write("Enjoy playing the classic game!")

with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

st.components.v1.html(html_data, height=600)
