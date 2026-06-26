import streamlit as st
import time

st.set_page_config(page_title="For coding queen👑", layout="centered")

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #2c003e, #4b006e);
    color: gold;
    text-align: center;
}
.title {
    font-size: 45px;
    font-weight: bold;
    text-shadow: 0 0 20px gold;
    margin-top: 40px;
}
.message {
    font-size: 22px;
    margin-top: 30px;
    background: rgba(255, 215, 0, 0.08);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
}
.stButton>button {
    background-color: gold;
    color: purple;
    border-radius: 30px;
    font-size: 18px;
    padding: 10px 25px;
    box-shadow: 0 0 15px gold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Session Setup ----------------
if "page" not in st.session_state:
    st.session_state.page = 1

if "animation_done" not in st.session_state:
    st.session_state.animation_done = False


# ---------------- Typewriter ----------------
def typewriter(text):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(
            '<div class="message">' + typed + '</div>',
            unsafe_allow_html=True
        )
        time.sleep(0.02)


# ================= PAGE 1 =================
if st.session_state.page == 1:

    st.markdown('<div class="title"> Enter Password🔐</div>', unsafe_allow_html=True)

    password = st.text_input("Enter Password", type="password")

    if st.button("Open🔓"):

        if password == "Guri@780":
            st.session_state.page = 2
            st.session_state.animation_done = False
            st.rerun()
        else:
            st.error("Wrong Password ❌ Try Again")
            st.rerun()


# ================= PAGE 2 (WELCOME) =================
elif st.session_state.page == 2:

    st.markdown('<div class="title">Welcome 💐</div>', unsafe_allow_html=True)

    welcome_text = """🌍Welcome to the Digital  World 🚀 

✨ Every great programmer begins with a single line of code. 💻

🌐 Technology is not just about writing programs—it's about creating ideas that can change lives. 💡

🚀 Every challenge is an opportunity to learn something new.

🌸 I hope your C++ journey is filled with curiosity 🧠, confidence 💪, and success 🏆.

Happy Coding Life 💙"""

    if not st.session_state.animation_done:
        typewriter(welcome_text)
        st.session_state.animation_done = True
    else:
        st.markdown('<div class="message">' + welcome_text + '</div>', unsafe_allow_html=True)

    if st.button("Next ⏭️"):
        st.session_state.page = 3
        st.session_state.animation_done = False
        st.rerun()


# ================= PAGE 3 (THANK YOU) =================
elif st.session_state.page == 3:

    st.markdown('<div class="title">💻C++ Journey 🚀</div>', unsafe_allow_html=True)

    thank_text = """

✨ C++ is more than a programming language—it teaches logic 🧩, patience 🌱, and problem-solving 💡.

⚡ There will be difficult days, but every error ❌ is a lesson 📚 and every solved problem ✅ is a step forward.

🌟 Believe in yourself 💪, enjoy the learning process 😊, and keep moving toward your goals 🎯.

🚀 Keep Learning. Keep Building. Keep Growing. 🌸"""

    if not st.session_state.animation_done:
        typewriter(thank_text)
        st.session_state.animation_done = True
    else:
        st.markdown('<div class="message">' + thank_text + '</div>', unsafe_allow_html=True)

    if st.button("Next Page ⏭️"):
        st.session_state.page = 4
        st.session_state.animation_done = False
        st.rerun()


# ================= PAGE 4 (SORRY) =================
elif st.session_state.page == 4:

    st.markdown('<div class="title">🌸 Best of Luck for Your Future ✨ 💜</div>', unsafe_allow_html=True)

    sorry_text = """🌸 Best of Luck for Your Future ✨
🎓 Wishing you endless success 🏆 in your studies, your coding journey 💻, and everything you dream of achieving 🌈.
🌟 May every challenge make you stronger 💪, every project make you more confident 🚀, and every achievement bring you closer to your goals 🎯.
😊 Keep coding 💻. Keep smiling 🌸. Keep believing in yourself ✨
 ."""

    if not st.session_state.animation_done:
        typewriter(sorry_text)
        st.session_state.animation_done = True
    else:
        st.markdown('<div class="message">' + sorry_text + '</div>', unsafe_allow_html=True)

    if st.button("Next ⏭️"):
        st.session_state.page = 5
        st.session_state.animation_done = False
        st.rerun()


# ================= PAGE 5 (MISS YOU) =================
elif st.session_state.page == 5:

    st.markdown('<div class="title"> Ones again 💫</div>', unsafe_allow_html=True)

    miss_text = """
🙏 Thank you for visiting this little project.
🌷 I simply wanted to wish you all the very best for your C++ journey 💻 and your future ✨.
🌟 May your hard work always bring you success 🏆 and happiness 😊.
🌸 Best of Luck dear 🥰 🚀✨"""

    if not st.session_state.animation_done:
        typewriter(miss_text)
        st.session_state.animation_done = True
