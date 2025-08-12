import streamlit as st

# 제목
st.title("💼 MBTI 기반 진로 추천 사이트")
st.write("MBTI를 선택하면 적합한 직업을 추천해 드립니다.")

# MBTI 데이터
mbti_jobs = {
    "INTJ": ["전략기획가", "데이터 분석가", "연구원"],
    "ENTP": ["창업가", "마케팅 기획자", "변호사"],
    "INFJ": ["상담가", "교사", "작가"],
    "ESFP": ["승무원", "이벤트 기획자", "배우"],
    # 필요한 MBTI 계속 추가
}

mbti_description = {
    "INTJ": "분석적이고 계획적인 성향, 전략을 세우는 데 강점이 있습니다.",
    "ENTP": "도전적이고 창의적인 성향, 새로운 아이디어를 구현하는 데 강점이 있습니다.",
    "INFJ": "통찰력과 배려심이 많아 사람을 돕는 직업에 적합합니다.",
    "ESFP": "사교적이고 에너지가 넘쳐 사람들과 함께하는 활동에 강점이 있습니다.",
}

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"🔍 {selected_mbti} 추천 직업")
    st.write(mbti_description[selected_mbti])
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")

