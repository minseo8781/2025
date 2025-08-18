import streamlit as st
import random

st.set_page_config(page_title="🎵 오늘의 기분 기반 음악 추천", page_icon="🎧", layout="centered")

st.title("🎵 오늘의 기분 기반 음악 추천")

# 기분 선택
mood = st.selectbox(
    "오늘 기분은 어떤가요? 🤔",
    ["😊 행복해", "😢 슬퍼", "🔥 신나", "😌 차분해", "💪 자신감 뿜뿜"]
)

# 기분별 노래 추천 (더 많이 추가!)
songs = {
    "😊 행복해": [
        ("Pharrell Williams - Happy", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("BTS - Dynamite", "https://www.youtube.com/watch?v=gdZLi9oWNZg"),
        ("Red Velvet - Power Up", "https://www.youtube.com/watch?v=WyiIGEHQP8o"),
        ("TWICE - Cheer Up", "https://www.youtube.com/watch?v=c7rCyll5AeY"),
        ("AKMU - 200%", "https://www.youtube.com/watch?v=0Oi8jDMvd_w"),
    ],
    "😢 슬퍼": [
        ("Adele - Someone Like You", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("이하이 - 한숨", "https://www.youtube.com/watch?v=K0l5Q_Vzdx8"),
        ("Paul Kim - 모든 날, 모든 순간", "https://www.youtube.com/watch?v=l9SsORr7T5M"),
        ("Baek Yerin - Square", "https://www.youtube.com/watch?v=95b1Xj9wWqU"),
        ("김광석 - 이등병의 편지", "https://www.youtube.com/watch?v=kq9N7tE9dY4"),
    ],
    "🔥 신나": [
        ("PSY - 강남스타일", "https://www.youtube.com/watch?v=9bZkp7q19f0"),
        ("Stray Kids - MANIAC", "https://www.youtube.com/watch?v=OvioeS1ZZ7o"),
        ("BLACKPINK - BOOMBAYAH", "https://www.youtube.com/watch?v=bwmSjveL3Lc"),
        ("NCT 127 - Cherry Bomb", "https://www.youtube.com/watch?v=WkuHLzMMTZM"),
        ("SEVENTEEN - Very Nice", "https://www.youtube.com/watch?v=J-wFp43XOrA"),
    ],
    "😌 차분해": [
        ("IU - 밤편지", "https://www.youtube.com/watch?v=BzYnNdJhZQw"),
        ("Dean - instagram", "https://www.youtube.com/watch?v=wKyMIrBClYw"),
        ("Sam Smith - Stay With Me", "https://www.youtube.com/watch?v=pB-5XG-DbAA"),
        ("Paul Kim - 집돌이", "https://www.youtube.com/watch?v=gWJfwLV4lHc"),
        ("Standing Egg - Little Star", "https://www.youtube.com/watch?v=Jz8wU9DdbqU"),
    ],
    "💪 자신감 뿜뿜": [
        ("2NE1 - 내가 제일 잘 나가", "https://www.youtube.com/watch?v=j7_lSP8Vc3o"),
        ("Kanye West - Stronger", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
        ("Little Mix - Power", "https://www.youtube.com/watch?v=HjBo--1n8lI"),
        ("Jessie J - Domino", "https://www.youtube.com/watch?v=UJtB55MaoD0"),
        ("ITZY - WANNABE", "https://www.youtube.com/watch?v=fE2h3lGlOsk"),
    ]
}

# 버튼 눌렀을 때 노래 1곡만 랜덤 추천
if st.button("🎧 노래 추천 받기"):
    song = random.choice(songs[mood])
    st.subheader(f"✨ 오늘의 추천곡: {song[0]}")
    st.markdown(f"[👉 유튜브에서 듣기]({song[1]})")
