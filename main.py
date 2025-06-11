import streamlit as st
import folium
from streamlit_folium import st_folium

# 여행지 데이터
travel_data = [
    {
        "name": "경복궁",
        "region": "서울",
        "lat": 37.579617,
        "lon": 126.977041,
        "description": "조선시대의 정궁으로, 고궁 투어와 한복 체험으로 유명합니다."
    },
    {
        "name": "부산 해운대",
        "region": "부산",
        "lat": 35.158698,
        "lon": 129.160384,
        "description": "한국을 대표하는 해변으로 여름철 피서지로 인기가 높습니다."
    },
    {
        "name": "경주 불국사",
        "region": "경상북도",
        "lat": 35.790144,
        "lon": 129.331504,
        "description": "세계문화유산으로 등재된 신라시대의 대표적인 사찰입니다."
    },
    {
        "name": "제주 성산일출봉",
        "region": "제주도",
        "lat": 33.458759,
        "lon": 126.941402,
        "description": "제주의 대표 명소로, 일출이 아름답기로 유명합니다."
    },
]

# Streamlit 사이드바에서 지역 선택
st.sidebar.title("여행지 필터")
regions = list(set(place["region"] for place in travel_data))
selected_region = st.sidebar.selectbox("지역 선택", ["전체"] + regions)

# 본문
st.title("🇰🇷 한국 여행지 가이드")
st.write("아래 지도와 설명을 통해 한국의 주요 관광지를 알아보세요!")

# 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# 선택한 지역에 따라 필터링
if selected_region != "전체":
    filtered_data = [place for place in travel_data if place["region"] == selected_region]
else:
    filtered_data = travel_data

# 지도에 마커 추가
for place in filtered_data:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"<b>{place['name']}</b><br>{place['description']}",
        tooltip=place["name"],
    ).add_to(m)

# 지도 출력
st_data = st_folium(m, width=700, height=500)

# 여행지 설명 목록 출력
st.subheader("📌 여행지 정보")
for place in filtered_data:
    st.markdown(f"### {place['name']} ({place['region']})")
    st.write(place['description'])
