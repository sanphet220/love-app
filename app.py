import streamlit as str
import random

# ตั้งค่าหน้าเว็บให้เปิดบนมือถือแล้วสวย
st.set_page_config(page_title="มีอะไรจะถามหน่อยยย 💖", page_icon="💖", layout="centered")

# ตกแต่งหน้าตาเว็บด้วย CSS นิดหน่อย
st.markdown("""
    <style>
    .stApp { background-color: #ffe6e6; }
    h1 { color: #cc0000; text-align: center; font-family: 'Arial', sans-serif; }
    div.stButton > button {
        background-color: #ff4d4d; color: white; border-radius: 20px;
        padding: 10px 25px; font-weight: bold; border: none; width: 100%;
    }
    </style>
""", unsafe_allow_back_color=True)

st.write("# เค้ารักเบบี๋มากเลยนะอยู่ด้วยกันกับเค้าไปนานๆเลยนะ  🥺")

# สร้างตัวแปรเก็บสถานะการกด
if 'agreed' not in st.session_state:
    st.session_state.agreed = False

if not st.session_state.agreed:
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("ตกลงอยู่แล้ว ❤️", key="yes"):
            st.session_state.agreed = True
            st.rerun()
            
    with col2:
        # บนหน้าเว็บ ปุ่ม No จะใช้วิธีแกล้งแบบ "กดแล้วมันจะสุ่มสลับฝั่ง" หรือเปลี่ยนข้อความไปเรื่อยๆ แทนการวาร์ปหนี (เพราะบนมือถือไม่มีเมาส์มาชี้)
        no_texts = ["ไม่ตกลง 😜", "คิดใหม่ซิ๊ 🥺", "กดปุ่มซ้ายเถอะจ้า 💖", "กดยังไงก็ไม่ได้หรอก แบร่ 😝"]
        if 'no_click_count' not in st.session_state:
            st.session_state.no_click_count = 0
            
        if st.button(no_texts[st.session_state.no_click_count % len(no_texts)], key="no"):
            st.session_state.no_click_count += 1
            st.rerun()
else:
    st.balloons() # เอฟเฟกต์ลูกโป่งลอยฉลองเต็มจอ 🎈
    st.write("### เย้! น่ารักที่สุดในโลกเลยยยยย ยักนะงับบ 🥰❤️")
