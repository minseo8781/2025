import streamlit as st
import random

st.set_page_config(page_title="🧳 여행 취향 테스트", page_icon="🌍", layout="centered")
st.title("🧳 여행 취향 테스트")
st.write("질문에 답하면 어울리는 여행지를 추천해드립니다!")

# 질문
q1 = st.radio("1️⃣ 자연환경 선호", ["산", "바다"])
q2 = st.radio("2️⃣ 계절 선호", ["여름", "겨울"])
q3 = st.radio("3️⃣ 여행 스타일", ["액티비티", "휴양"])
q4 = st.radio("4️⃣ 도시 vs 자연", ["도시", "자연"])

# 여행지 데이터 (사진 링크 확인 완료)
destinations = [
    {"name":"제주도","tags":["바다","여름","휴양","자연"],
     "image":"https://images.unsplash.com/photo-1507525428034-8143b6f0c4b2?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"한라산과 바다가 어우러진 자연 휴양지.",
     "spots":["성산일출봉","협재해수욕장","한라산 등반","카페 거리"]},
    {"name":"교토","tags":["도시","여름","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1562147870-7b0d6a5b0a4d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"일본 전통과 현대가 공존하는 역사 도시.",
     "spots":["기요미즈데라","후시미 이나리 신사","아라시야마 대나무숲"]},
    {"name":"홋카이도","tags":["산","겨울","액티비티","자연"],
     "image":"https://images.unsplash.com/photo-1551817958-6c8b9b1f2a1e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"스키와 온천 체험이 가능한 겨울 여행지.",
     "spots":["삿포로","노보리베츠 온천","후라노 라벤더"]},
    {"name":"골드코스트","tags":["바다","여름","액티비티","자연"],
     "image":"https://images.unsplash.com/photo-1520962911848-5cb2b9f0f3f7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"서핑과 해변 액티비티가 유명한 호주 여행지.",
     "spots":["서퍼스 파라다이스","버레이 헤드 비치","골드코스트 스카이라인"]},
    {"name":"하롱베이","tags":["바다","여름","휴양","자연"],
     "image":"https://images.unsplash.com/photo-1587911119470-13f3e38b2644?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"독특한 석회암 섬과 크루즈 체험 휴양지.",
     "spots":["하롱베이 크루즈","바이차이 마을","티톱섬"]},
    {"name":"호이안","tags":["도시","여름","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1580203369871-646c0de0b601?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"고전적 건축과 야경이 아름다운 소도시.",
     "spots":["호이안 올드타운","일본 다리","야시장"]},
    {"name":"베이징","tags":["도시","겨울","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1552434742-df383302ffd3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"역사와 문화를 즐길 수 있는 중국 수도.",
     "spots":["자금성","만리장성","이화원"]},
    {"name":"장가계","tags":["산","여름","액티비티","자연"],
     "image":"https://images.unsplash.com/photo-1580134511780-7b7e3aab1c56?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"기묘한 봉우리와 자연 액티비티 산악지.",
     "spots":["천문산","황석산","바오핑 협곡"]},
    {"name":"파리","tags":["도시","여름","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1522098543979-ffc7f79d6510?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"예술과 문화가 가득한 프랑스 수도.",
     "spots":["에펠탑","루브르 박물관","몽마르트 언덕"]},
    {"name":"로마","tags":["도시","여름","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1512453979798-5ea266f8880c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"고대 유적과 문화 체험이 가능한 이탈리아 도시.",
     "spots":["콜로세움","트레비 분수","스페인 계단"]},
]

# 추천 버튼
if st.button("🌟 여행지 추천 받기"):
    user_tags = [
        "산" if q1=="산" else "바다",
        "여름" if q2=="여름" else "겨울",
        "휴양" if q3=="휴양" else "액티비티",
        "도시" if q4=="도시" else "자연"
    ]

    matches = [d for d in destinations if all(tag in d["tags"] for tag in user_tags)]
    choice = random.choice(matches) if matches else random.choice(destinations)

    st.subheader(f"✈️ 추천 여행지: {choice['name']}")
    st.image(choice["image"], use_column_width=True)
    st.write(choice["description"])
    st.write("🏖️ 가볼 만한 장소:")
    for spot in choice["spots"]:
        st.markdown(f"- {spot}")

