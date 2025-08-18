import streamlit as st
import random
import time

st.set_page_config(page_title="🧠 두뇌 게임 모음집", page_icon="🕹️")
st.title("🧠 두뇌 게임 모음집")
st.write("재밌게 두뇌를 자극해 보세요!")

# 탭 나누기
tabs = st.tabs(["📘 퀴즈 게임", "🔢 기억력 게임", "✊ 가위바위보", "🎨 색깔 단어 게임"])

# ------------------ 1. 퀴즈 게임 ------------------
with tabs[0]:
    st.subheader("📘 랜덤 퀴즈 게임")
    st.write("문제를 보고 정답을 골라보세요!")

    quiz_data = [
        {"q": "지구에서 가장 큰 대륙은?", "options": ["아시아", "아프리카", "유럽"], "answer": "아시아"},
        {"q": "빛의 속도는?", "options": ["약 30만 km/s", "약 3만 km/s", "약 300km/s"], "answer": "약 30만 km/s"},
        {"q": "우리 몸에서 가장 큰 장기는?", "options": ["폐", "간", "심장"], "answer": "간"},
        {"q": "대한민국의 수도는?", "options": ["서울", "부산", "인천"], "answer": "서울"},
        {"q": "피타고라스 정리는?", "options": ["a²+b²=c²", "E=mc²", "F=ma"], "answer": "a²+b²=c²"},
    ]

    quiz = random.choice(quiz_data)
    choice = st.radio(quiz["q"], quiz["options"])

    if st.button("정답 확인", key="quiz"):
        if choice == quiz["answer"]:
            st.success("🎉 정답입니다!")
        else:
            st.error(f"❌ 오답! 정답은 {quiz['answer']}")

# ------------------ 2. 기억력 게임 ------------------
with tabs[1]:
    st.subheader("🔢 숫자 기억력 게임")
    st.write("숫자를 잘 보고 기억해보세요!")

    if "number" not in st.session_state:
        st.session_state.number = None

    if st.button("새로운 숫자 생성"):
        st.session_state.number = "".join([str(random.randint(0,9)) for _ in range(6)])
        st.write("👀 3초 동안 숫자를 외우세요!")
        st.write(f"**{st.session_state.number}**")
        time.sleep(3)
        st.empty()  # 숫자 감추기

    if st.session_state.number:
        answer = st.text_input("👉 기억한 숫자를 입력하세요:")
        if st.button("제출", key="memory"):
            if answer == st.session_state.number:
                st.success("🎉 정확히 기억했어요!")
            else:
                st.error(f"❌ 틀렸습니다! 정답은 {st.session_state.number}")

# ------------------ 3. 가위바위보 ------------------
with tabs[2]:
    st.subheader("✊✌️✋ 가위바위보 게임")
    st.write("컴퓨터와 대결해보세요!")

    choices = ["가위", "바위", "보"]
    user_choice = st.radio("당신의 선택은?", choices)
    if st.button("대결하기"):
        comp_choice = random.choice(choices)
        st.write(f"🤖 컴퓨터의 선택: **{comp_choice}**")
        if user_choice == comp_choice:
            st.info("😐 비겼습니다!")
        elif (user_choice == "가위" and comp_choice == "보") or \
             (user_choice == "바위" and comp_choice == "가위") or \
             (user_choice == "보" and comp_choice == "바위"):
            st.success("🎉 당신이 이겼습니다!")
        else:
            st.error("😢 졌습니다...")

# ------------------ 4. 색깔 단어 게임 (Stroop Test) ------------------
with tabs[3]:
    st.subheader("🎨 색깔 단어 게임")
    st.write("단어가 아니라 **글자 색깔**을 맞춰보세요!")

    colors = ["빨강", "파랑", "초록", "노랑", "검정"]
    color_codes = {
        "빨강": "red",
        "파랑": "blue",
        "초록": "green",
        "노랑": "yellow",
        "검정": "black"
    }

    if st.button("새 문제 생성"):
        st.session_state.word = random.choice(colors)
        st.session_state.color = random.choice(list(color_codes.values()))

    if "word" in st.session_state and "color" in st.session_state:
        st.markdown(
            f"<h2 style='color:{st.session_state.color}; text-align:center;'>{st.session_state.word}</h2>",
            unsafe_allow_html=True
        )
        user_answer = st.radio("👉 글자 색깔은 무엇일까요?", colors)
        if st.button("정답 확인", key="stroop"):
            correct = [k for k, v in color_codes.items() if v == st.session_state.color][0]
            if user_answer == correct:
                st.success("🎉 정답입니다! 색깔을 제대로 구분했네요.")
            else:
                st.error(f"❌ 오답! 정답은 {correct} 색입니다.")
