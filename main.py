import streamlit as st
import random
import pandas as pd

# ========== 앱 설정 ==========
st.set_page_config(page_title="✨ MBTI 진로 & 궁합🎯", page_icon="🧭", layout="wide")

# CSS 스타일 (화려하게) - safe use of markdown
st.markdown(
    """
    <style>
    .big-title {font-size:42px; font-weight:700; color: #2b6cb0;}
    .subtitle {font-size:18px; color:#1a202c;}
    .card {background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%); padding:18px; border-radius:16px; box-shadow:0 6px 18px rgba(0,0,0,0.08);}
    .emoji {font-size:24px}
    .job-badge {display:inline-block; padding:6px 10px; margin:4px; border-radius:999px; background:#fff; box-shadow: 0 2px 6px rgba(0,0,0,0.06);}
    .sparkle {color:#f6ad55}
    </style>
    """,
    unsafe_allow_html=True,
)

# ========== MBTI 데이터(모든 16가지) ==========
mbti_jobs = {
    "INTJ": ["전략기획가 🧭", "데이터 분석가 📊", "연구원 🔬", "스타트업 CTO 💡"],
    "INTP": ["연구원 🔎", "데이터 과학자 🤖", "소프트웨어 엔지니어 🖥️", "게임 디자이너 🎮"],
    "ENTJ": ["CEO/경영자 🏢", "사업개발 🔗", "전략컨설턴트 📈", "프로젝트 매니저 📌"],
    "ENTP": ["창업가 🚀", "마케팅 기획자 📣", "제품매니저 🧩", "변호사 ⚖️"],
    "INFJ": ["상담가 🕊️", "교사 🍎", "작가 ✍️", "사회복지사 🤝"],
    "INFP": ["작가/시인 🖋️", "아트 디렉터 🎨", "상담사 💬", "비영리 활동가 🌱"],
    "ENFJ": ["HR/조직개발 👥", "교사/강사 🎓", "PR/커뮤니케이션 🌟", "상담가 🤝"],
    "ENFP": ["콘텐츠 크리에이터 🎥", "광고 카피라이터 ✨", "마케터 🔥", "이벤트 플래너 🎉"],
    "ISTJ": ["회계사 📚", "품질관리자 🛠️", "공무원 🏛️", "물류 관리자 🚚"],
    "ISFJ": ["간호사 ❤️", "교사 👩‍🏫", "행정/비서 🗂️", "박물관 큐레이터 🏺"],
    "ESTJ": ["관리자/팀장 👔", "운영 매니저 ⚙️", "군/경찰 조직 📯", "금융 담당자 💼"],
    "ESFJ": ["고객서비스 매니저 ☎️", "학교 행정 🏫", "이벤트 코디네이터 💐", "간호/복지 분야 🩺"],
    "ISTP": ["기계/설비 엔지니어 ⚙️", "파일럿 ✈️", "데이터 엔지니어 🧱", "응급구조대원 🚑"],
    "ISFP": ["디자이너 🎨", "요리사 🍳", "사진작가 📷", "플로리스트 🌸"],
    "ESTP": ["영업/딜러 💬", "스포츠 코치 🏃", "이벤트 프로듀서 🎪", "응급의료진 🚨"],
    "ESFP": ["승무원 ✈️", "배우/모델 🎭", "무대 연출가 🎬", "파티 플래너 🥳"],
}

mbti_descriptions = {
    "INTJ": "분석적이고 계획적인 성향. 큰 그림과 전략을 만드는 걸 좋아해요.",
    "INTP": "아이디어가 넘치고 논리적이며 이론을 탐구하는 걸 즐깁니다.",
    "ENTJ": "리더십과 추진력이 강해 조직을 이끄는 역할에 적합합니다.",
    "ENTP": "창의적이고 토론을 즐기며 새로운 시도를 두려워하지 않습니다.",
    "INFJ": "사람을 깊게 이해하고 돕는 일에 의미를 느낍니다.",
    "INFP": "내면의 가치와 창의성이 중요한 유형입니다.",
    "ENFJ": "사람들을 이끌며 돕는 데 탁월한 역량을 보입니다.",
    "ENFP": "에너지가 넘치고 사람들과의 교류에서 영감을 받습니다.",
    "ISTJ": "책임감이 강하고 규칙과 절차를 잘 따릅니다.",
    "ISFJ": "세심하고 배려심이 깊어 사람을 돌보는 역할에 적합합니다.",
    "ESTJ": "실용적이고 조직적인 운영에 강합니다.",
    "ESFJ": "사교적이고 조화를 중요시하여 사람 중심의 직무가 어울립니다.",
    "ISTP": "현실적 문제 해결을 빠르게 해내는 실전형입니다.",
    "ISFP": "감각적이고 예술적 표현을 통해 자신의 가치를 드러냅니다.",
    "ESTP": "즉흥적이고 실행력 강하며 현장의 리더가 되기 좋습니다.",
    "ESFP": "사람들 앞에서 빛나며 경험을 만들고 즐기는 데 강합니다.",
}

# ========== 유틸리티: MBTI 궁합 계산 ==========

def compatibility_score(m1: str, m2: str) -> int:
    """간단한 점수: 동일한 문자 수 (위치 무관) + 위치 일치 점수
    최대 8점 -> 100점 환산"""
    m1 = m1.upper()
    m2 = m2.upper()
    # 위치 일치
    position_matches = sum(1 for a, b in zip(m1, m2) if a == b)
    # 문자 공통 개수 (multiset)
    common = 0
    temp = list(m2)
    for ch in m1:
        if ch in temp:
            common += 1
            temp.remove(ch)
    score = position_matches * 2 + (common - position_matches)  # 위치 일치 더 가치있음
    # score range: 0..8
    return max(0, min(8, score))


def compatibility_text(score: int) -> str:
    pct = int(score / 8 * 100)
    if pct >= 85:
        return f"💖 궁합 최고! ({pct}%) — 함께 팀을 이루면 폭발적인 시너지를 낼 수 있어요! 🎉"
    if pct >= 65:
        return f"✨ 아주 좋음 ({pct}%) — 서로 보완하며 잘 맞아요. 👍"
    if pct >= 40:
        return f"🙂 보통 ({pct}%) — 장단점이 섞여 서로 배우는 관계가 될 수 있어요."
    return f"⚠️ 주의 필요 ({pct}%) — 서로 다른 스타일이 많아 조정이 필요할 수 있어요."

# ========== 사이드 데이터: MBTI 컬러/이모지 ==========
mbti_emoji = {
    "INTJ": "🧠✨", "INTP": "🔬💭", "ENTJ": "🏹🔥", "ENTP": "🎯💡",
    "INFJ": "🌙🤲", "INFP": "🌿🖋️", "ENFJ": "🌟🤝", "ENFP": "🎪🌈",
    "ISTJ": "📘🛡️", "ISFJ": "🕊️🧷", "ESTJ": "🛠️📊", "ESFJ": "🎀🍰",
    "ISTP": "🧰🏍️", "ISFP": "🎨🍃", "ESTP": "⚡🏁", "ESFP": "🎉🌞",
}

# ========== 앱 UI ==========
# 헤더
st.markdown('<div class="big-title">✨ MBTI 진로 추천 & 궁합 테스트 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">이모지 폭발! 🎊 예쁘고 화려한 교육용 진로 앱 — MBTI를 선택하면 나에게 딱 맞는 직업과 상대 MBTI와의 궁합을 보여줘요.</div>', unsafe_allow_html=True)
st.divider()

# 레이아웃: 왼쪽 입력, 오른쪽 결과
left, right = st.columns((1, 1))

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔎 나의 MBTI를 골라봐요!")
    all_mbti = list(mbti_jobs.keys())
    selected_mbti = st.selectbox("나의 MBTI 선택 ✨", options=all_mbti, index=all_mbti.index("ISFP") if "ISFP" in all_mbti else 0)
    st.markdown(f"<div style='margin-top:8px'><span class='emoji'>{mbti_emoji.get(selected_mbti,'')}</span> <strong>{selected_mbti}</strong> — {mbti_descriptions[selected_mbti]}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🎯 추천 직업 리스트")
    jobs = mbti_jobs[selected_mbti]
    # 예쁘게 배지로 표시
    job_html = ""
    for j in jobs:
        job_html += f"<span class='job-badge'>🔹 {j}</span>"
    st.markdown(job_html, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🧭 진로 팁 & 준비법")
    # 간단 팁 생성
    tips = {
        "default": [
            "포트폴리오를 꾸준히 만들기 📁",
            "관련 자격증/강의 수강하기 🎓",
            "인턴/현장 경험 쌓기 🧳",
            "네트워킹과 멘토 찾기 🤝",
        ]
    }
    for t in tips["default"]:
        st.write(f"- {t}")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💞 MBTI 궁합 테스트 (재미용)")
    st.write("내 MBTI와 궁합을 보고 싶은 상대 MBTI를 선택하세요. (교육용, 간단한 알고리즘으로 계산됩니다)")

    other_mbti = st.selectbox("상대 MBTI 선택 🧑‍🤝‍🧑", options=all_mbti, index=all_mbti.index("ENFP") if "ENFP" in all_mbti else 1)
    if st.button("🔮 궁합 확인하기!"):
        score = compatibility_score(selected_mbti, other_mbti)
        txt = compatibility_text(score)
        # show result with fun visuals
        st.markdown(f"### 🔗 {selected_mbti} + {other_mbti}")
        # progress bar style
        pct = int(score / 8 * 100)
        bar = st.progress(0)
        for i in range(pct + 1):
            bar.progress(i)
        st.write(txt)
        # 간단 해석
        st.markdown("**🔍 해석 포인트**")
        match_letters = [a==b for a,b in zip(selected_mbti, other_mbti)]
        details = []
        labels = ["에너지(E/I)", "인식(S/N)", "판단(T/F)", "생활(J/P)"]
        for i, same in enumerate(match_letters):
            status = "같음 ✅" if same else "다름 ❌"
            details.append(f"- {labels[i]}: {status}")
        for d in details:
            st.write(d)
        # 축하 이펙트
        if pct >= 65:
            st.balloons()

    st.markdown("---")
    st.subheader("🎲 랜덤 MBTI 뽑기 (재밌게) ")
    if st.button("🎲 운명 MBTI 뽑기"):
        pick = random.choice(all_mbti)
        st.success(f"오늘의 운명 MBTI은 {pick} {mbti_emoji.get(pick,'')} 이야!")
        st.write("그 MBTI의 추천 직업:")
        for j in mbti_jobs[pick]:
            st.write(f"- {j}")

    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ========== 추가 섹션: 전체 MBTI 요약 테이블 ==========
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header('📚 모든 MBTI 요약표')
summary = []
for m in all_mbti:
    summary.append({
        'MBTI': m,
        '이모지': mbti_emoji.get(m, ''),
        '설명': mbti_descriptions[m],
        '추천직업(샘플)': ", ".join(mbti_jobs[m][:3])
    })
df = pd.DataFrame(summary)

# show dataframe with Streamlit's native display
st.dataframe(df)

# CSV 다운로드
csv = df.to_csv(index=False).encode('utf-8-sig')
st.download_button(label="📥 MBTI 요약 CSV 다운로드", data=csv, file_name='mbti_summary.csv', mime='text/csv')
st.markdown('</div>', unsafe_allow_html=True)

# ========== 하단: 마무리 ==========
st.markdown("---")
st.markdown("### ✨ 사용법 & 배포\n1. 이 파일을 `mbti_streamlit_app.py`로 저장하세요.\n2. `pip install streamlit pandas` 설치.\n3. `streamlit run mbti_streamlit_app.py` 실행.\n\n즐겁게 사용하세요! 🎉")

# 작은 팁: 개발자 모드에서는 더 많은 CSS나 이미지, 애니메이션을 넣어 꾸밀 수 있어요.
