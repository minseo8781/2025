import streamlit as st
import random

st.set_page_config(page_title="🧳 여행 취향 테스트", page_icon="🌍", layout="centered")
st.title("🧳 여행 취향 테스트")
st.write("질문에 답하면 어울리는 여행지와 가볼 만한 장소까지 추천해드립니다! ✨")

# -------------------- 질문 --------------------
q1 = st.radio("1️⃣ 자연환경 선호", ["🏔️ 산", "🏖️ 바다"])
q2 = st.radio("2️⃣ 계절 선호", ["☀️ 여름", "❄️ 겨울"])
q3 = st.radio("3️⃣ 여행 스타일", ["🏄‍♂️ 액티비티", "🛌 휴양"])
q4 = st.radio("4️⃣ 도시 vs 자연", ["🏙️ 도시", "🌲 자연"])

# -------------------- 여행지 데이터 --------------------
destinations = [
    {"name":"제주도","tags":["바다","여름","휴양","자연"],
     "image":"https://images.unsplash.com/photo-1507525428034-b723cf961d3e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"맑은 바다와 한라산이 어우러진 자연 휴양지.",
     "spots":["성산일출봉","협재해수욕장","한라산 등반","제주 카페 거리"]},
    {"name":"교토","tags":["도시","여름","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1562147870-7b0d6a5b0a4d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"전통과 현대가 공존하는 일본의 역사 도시.",
     "spots":["기요미즈데라","후시미 이나리 신사","아라시야마 대나무숲","교토 거리"]},
    {"name":"홋카이도","tags":["산","겨울","액티비티","자연"],
     "image":"https://images.unsplash.com/photo-1551817958-6c8b9b1f2a1e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"눈 덮인 산과 스키, 온천 체험이 가능한 겨울 여행지.",
     "spots":["삿포로","노보리베츠 온천","후라노 라벤더","오타루 운하"]},
    {"name":"골드코스트","tags":["바다","여름","액티비티","자연"],
     "image":"https://images.unsplash.com/photo-1507525428034-b723cf961d3e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"서핑과 해변 액티비티가 유명한 호주 여행지.",
     "spots":["서퍼스 파라다이스","버레이 헤드 비치","골드코스트 스카이라인","트위드 밸리"]},
    {"name":"하롱베이","tags":["바다","여름","휴양","자연"],
     "image":"https://images.unsplash.com/photo-1587911119470-13f3e38b2644?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"독특한 석회암 섬과 크루즈 체험이 가능한 베트남 휴양지.",
     "spots":["하롱베이 크루즈","바이차이 마을","뚱탕 동굴","티톱섬"]},
    {"name":"호이안","tags":["도시","여름","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1580203369871-646c0de0b601?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"고전적 건축과 야경이 아름다운 베트남 소도시.",
     "spots":["호이안 올드타운","일본 다리","푸른시장","야시장"]},
    {"name":"베이징","tags":["도시","겨울","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1552434742-df383302ffd3?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"중국의 수도, 역사와 문화 체험이 가능한 도시.",
     "spots":["자금성","만리장성","이화원","천안문 광장"]},
    {"name":"장가계","tags":["산","여름","액티비티","자연"],
     "image":"https://images.unsplash.com/photo-1580134511780-7b7e3aab1c56?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"기묘한 봉우리와 자연 액티비티로 유명한 중국 산악지.",
     "spots":["천문산","아바 통로","황석산","바오핑 협곡"]},
    {"name":"파리","tags":["도시","여름","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1522098543979-ffc7f79d6510?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"예술과 문화의 도시. 관광, 쇼핑, 카페 투어 가능.",
     "spots":["에펠탑","루브르 박물관","몽마르트 언덕","샹젤리제 거리"]},
    {"name":"로마","tags":["도시","여름","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1512453979798-5ea266f8880c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"고대 로마 유적과 문화 체험 가능한 이탈리아 도시.",
     "spots":["콜로세움","포로 로마노","트레비 분수","스페인 계단"]},
    {"name":"런던","tags":["도시","겨울","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1562259945-bd18e785fa87?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"역사와 현대가 공존하는 영국의 수도.",
     "spots":["빅벤","버킹엄 궁전","런던아이","타워브리지"]},
    {"name":"뉴질랜드 남섬","tags":["산","여름","액티비티","자연"],
     "image":"https://images.unsplash.com/photo-1504215680853-026ed2a45def?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"하이킹, 번지점프, 자연 경관 체험 가능한 액티비티 여행지.",
     "spots":["퀸스타운","밀포드 사운드","루트번지점프","테카포 호수"]},
    {"name":"하와이","tags":["바다","여름","액티비티","자연"],
     "image":"https://images.unsplash.com/photo-1507525428034-b723cf961d3e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"서핑, 스노클링, 화산 트레킹 등 다양한 액티비티 가능.",
     "spots":["와이키키 해변","마우나케아","할레아칼라","하나로드"]},
    {"name":"이탈리아 베니스","tags":["도시","여름","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1519397155452-c1c3b4d1872e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"운하와 곤돌라가 매력적인 이탈리아 소도시.",
     "spots":["산마르코 광장","리알토 다리","곤돌라 투어","무라노 섬"]},
    {"name":"아이슬란드","tags":["산","겨울","액티비티","자연"],
     "image":"https://images.unsplash.com/photo-1501451987227-32f9ee814e19?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"화산, 빙하, 오로라 등 자연 경관이 압도적인 여행지.",
     "spots":["골든서클","셀포스 폭포","레이캬비크","요쿨살론 빙하호"]},
    {"name":"캐나다 밴프","tags":["산","여름","액티비티","자연"],
     "image":"https://images.unsplash.com/photo-1516728778615-2d590ea1856f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"로키 산맥과 호수가 아름다운 캐나다 자연 여행지.",
     "spots":["밴프 국립공원","루이스호","모레인호","샤토 레이크루이스"]},
    {"name":"태국 방콕","tags":["도시","여름","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1565030271388-7c7874345f3b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"활기찬 도시와 전통 사원이 매력적인 태국 수도.",
     "spots":["왓 아룬","왓 포","카오산 로드","짜오프라야 강"]},
    {"name":"터키 이스탄불","tags":["도시","겨울","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1528909514045-2fa4ac7a08ba?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"동서양이 만나는 역사와 문화의 도시.",
     "spots":["아야 소피아","블루 모스크","그랜드 바자르","보스포루스 해협"]},
    {"name":"스페인 바르셀로나","tags":["도시","여름","휴양","도시"],
     "image":"https://images.unsplash.com/photo-1528909514045-2fa4ac7a08ba?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080",
     "description":"가우디 건축과 해변을 즐길 수 있는 도시.",
     "spots":["사그라다 파밀리아","구엘 공원","람블라스 거리","바르셀로네타 비치"]},
]

# -------------------- 추천 --------------------
if st.button("🌟 여행지 추천 받기"):
    # 사용자가 선택한 태그
    user_tags = [
        "산" if q1=="🏔️ 산" else "바다",
        "여름" if q2=="☀️ 여름" else "겨울",
        "휴양" if q3=="🛌 휴양" else "액티비티",
        "도시" if q4=="🏙️ 도시" else "자연"
    ]

    # 선택된 태그와 맞는 여행지 필터링
    matches = [d for d in destinations if all(tag in d["tags"] for tag in user_tags)]
    if matches:
        choice = random.choice(matches)
    else:
        choice = random.choice(destinations)

    # 결과 표시
    st.subheader(f"✈️ 추천 여행지: {choice['name']}")
    st.image(choice["image"], use_column_width=True)
    st.write(choice["description"])

    st
