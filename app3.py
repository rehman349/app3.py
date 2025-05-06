import streamlit as st
from datetime import datetime
from PIL import Image
import random
import streamlit.components.v1 as components

# --- Page Settings ---
st.set_page_config(page_title="🎂 Happy Birthday!", page_icon="🎈", layout="wide")

# --- Custom CSS Styling with Animation, Fonts, Effects ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
    <style>
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .stApp {
        background: linear-gradient(-45deg, #f9d29d, #ffd7e9, #ffc0cb, #ffe4e1);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Poppins', sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Pacifico', cursive;
        color: #ff4081;
        text-shadow: 2px 2px 8px #ff69b4, 0 0 10px #ff6ec7;
    }
    p, div, span, li {
        color: #7b2cbf;
        font-size: 18px;
    }
    .play-button {
        background-color: #ff6ec7;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 50px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 2px 2px 10px #ff1493;
    }
    .play-button:hover {
        background-color: #ff1493;
        transform: scale(1.1);
        box-shadow: 4px 4px 20px #ff1493;
    }
    img {
        transition: transform 0.3s ease;
    }
    img:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("🎈 Happy Birthday 🎈")
st.balloons()

# --- Countdown Timer ---
st.markdown("<h1 style='text-align: center;'>⏳ Countdown to Your Big Day!</h1>", unsafe_allow_html=True)

birthday_date = datetime(2025, 5, 29, 23, 59, 0)
now = datetime.now()

countdown_placeholder = st.empty()

if birthday_date <= now:
    st.success("🎂 It's your Birthday! Let's Celebrate! 🎉")
    st.markdown("""
        <script src="https://cdn.jsdelivr.net/npm/fireworks-js@2.1.0/dist/index.umd.min.js"></script>
        <div id="fireworks" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:9999; pointer-events:none;"></div>
        <script>
        const container = document.getElementById('fireworks');
        const fireworks = new Fireworks.default(container, {
            rocketsPoint: { min: 0, max: 100 },
            intensity: 30
        });
        fireworks.start();
        </script>
    """, unsafe_allow_html=True)
else:
    countdown = birthday_date - now
    days = countdown.days
    hours, remainder = divmod(countdown.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    countdown_placeholder.success(f"🎉 {days} days, {hours} hours, {minutes} minutes, {seconds} seconds left!")

st.divider()

# --- Birthday Image ---
try:
    img = Image.open(r"")
    img = img.resize((800, 800))
    st.image(img, caption="Have a Magical Day! 🎉", use_container_width=True)
except Exception:
    st.warning("📸 Local image not found. Showing online image instead.")
    st.image("https://i.imgur.com/8z9z5ch.jpg", caption="Have a Magical Day! 🎉", use_container_width=True)

st.divider()

# --- Play Birthday Song ---
st.markdown("""
    <audio id="birthday-audio" src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"></audio>
    <center><button class="play-button" onclick="playAudio()">▶️ Play Music</button></center>
    <canvas id="confetti-canvas"></canvas>
    <script>
    function playAudio() {
        var audio = document.getElementById('birthday-audio');
        audio.play();
        setTimeout(function() {
            const confettiSettings = { target: 'confetti-canvas', max: 200, size: 1.2, animate: true };
            const confetti = new ConfettiGenerator(confettiSettings);
            confetti.render();
        }, 500);
    }
    </script>
    <script src="https://cdn.jsdelivr.net/npm/confetti-js@0.0.18/dist/index.min.js"></script>
""", unsafe_allow_html=True)

st.divider()

# --- Secret Code Unlock ---
st.subheader("🏱 Enter Secret Code to Unlock Surprise!")
code = st.text_input("Enter Secret Code:")
if code.upper() == "ABDUL29":
    st.success("🌟 Secret Unlocked! 🌟")
    st.snow()
    st.markdown("""
        <div style="font-size:22px; color:#6a0572; text-align:center;">
        Wishing you endless happiness and a day full of love! 💖
        </div>
    """, unsafe_allow_html=True)
elif code:
    st.error("❌ Incorrect code, please try again!")

st.divider()

# --- Birthday Wish Generator ---
wishes = [
    "May your birthday be filled with joy and laughter!",
    "Wishing you health, wealth, and happiness!",
    "Cheers to another year of success and adventure!",
    "May all your dreams come true this year!"
]
if st.button("💍 Get a Birthday Wish"):
    st.info(random.choice(wishes))

st.divider()

# --- Message Wall ---
st.markdown("### 🌐 Birthday Memory Wall")
message = st.text_area("Leave a message for Abdul Rehman:")
if st.button("Submit Message"):
    st.success("Message saved! (simulation)")
    st.write("You wrote:", message)

st.divider()

# --- Fun Fact on Birthday ---
st.markdown("### 🤔 Fun Fact about May 29")
st.info("Did you know? Mount Everest was first summited on May 29, 1953!")

st.divider()

# --- Birthday Poem ---
with st.expander("📜 Click to Read a Special Birthday Poem"):
    st.markdown("""
    <div style="font-size:20px; text-align:center; color:#6a0572;">
    Life’s too short not to celebrate,<br>
    Another trip around the sun.<br>
    You’re a star, a gem, a lovely soul,<br>
    May your year be full of fun! 🎉
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- Special Memories Gallery ---
st.markdown("<h2 style='text-align: center;'>📸 Special Memories</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://i.imgur.com/8z9z5ch.jpg", caption="Fun Memories!", use_container_width=True)
with col2:
    st.image("https://i.imgur.com/U5xB1uY.jpg", caption="Smiling Moments!", use_container_width=True)
with col3:
    st.image("https://i.imgur.com/Nm9hJbV.jpg", caption="Beautiful Times!", use_container_width=True)

st.divider()

# --- Mini Birthday Quiz ---
st.markdown("<h2 style='text-align: center;'>🎯 Mini Birthday Quiz</h2>", unsafe_allow_html=True)
with st.form("quiz_form"):
    q1 = st.radio("🎂 What is the traditional birthday dessert?", ("Pizza", "Cake", "Burger", "Pasta"))
    q2 = st.radio("🎉 Which color is often associated with celebrations?", ("Gray", "Pink", "Blue", "Black"))
    q3 = st.radio("🏱 What do we usually give on birthdays?", ("Gifts", "Homework", "Bills", "Receipts"))
    submitted = st.form_submit_button("Submit Quiz")
    if submitted:
        score = sum([q1 == "Cake", q2 == "Pink", q3 == "Gifts"])
        st.success(f"🎉 You scored {score}/3!")
        if score == 3:
            st.balloons()
        elif score == 2:
            st.info("Almost perfect! 🎯")
        else:
            st.warning("Try again to get a perfect score! 🎂")

st.divider()

# --- Footer ---
st.markdown("<h4 style='text-align: center;'>Made with 💖 by Your Best Friend!</h4>", unsafe_allow_html=True)
