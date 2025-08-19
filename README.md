
# 🎮 Tic-Tac-Toe Game – Prodigy Infotech Task

This project is a submission for the **Prodigy Infotech Web Development Internship**. It features a classic **Tic-Tac-Toe game** built using HTML, CSS, and JavaScript, and deployed via **Streamlit Community Cloud**.

---

Task - To build a tic-tac-toe web application, you can use HTML, CSS, and JavaScript. By implementing functions to handle user clicks, track game state, and check for winning conditions, you can create an interactive and engaging tic-tac-toe game. With these technologies and functionalities, users can play against each other or against an AI opponent, aiming to get three markers in a row to win the game.


## 🚀 Live Demo

You can play the game here:  
🔗 [Tic-Tac-Toe Streamlit App](https://tictactoe-3dqf9umktmhkjrtcy5hhvu.streamlit.app/)

---

## 🧩 Features

- Interactive 3x3 Tic-Tac-Toe grid
- Two-player mode (X vs O)
- Turn-based logic with visual indicators
- Win detection and draw handling
- "Play Again" button to reset the game
- Fully embedded in a Streamlit app using `st.components.v1.html`

---

## 📦 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Streamlit Community Cloud
- **Integration**: Python wrapper (`app.py`) to embed the game in Streamlit

---

## 📁 Project Structure

```
├── app.py               # Streamlit wrapper for embedding the game
├── index.html           # Main game interface with inlined CSS and JS
├── requirements.txt     # Python dependencies
```

## 🛠️ How It Works

The game is built as a standalone web app using HTML, CSS, and JS. To deploy it on Streamlit:

1. The entire game is inlined into `index.html` (CSS and JS included).
2. `app.py` reads and embeds the HTML using Streamlit’s `st.components.v1.html()` method.
3. The app is deployed on Streamlit Cloud for public access.


## 📌 Deployment Notes

- Streamlit does not serve static files like CSS or JS separately.
- All styles and scripts are embedded directly into `index.html` using `<style>` and `<script>` tags.
- The app is lightweight and runs entirely in the browser.


## 🧠 Author

**Bhavani Yannam**  
GitHub: [Bhavaniyannam](https://github.com/Bhavaniyannam)


## 📜 License

This project is for educational and internship purposes under Prodigy Infotech. Feel free to fork and modify for personal learning.













