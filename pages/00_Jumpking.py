import streamlit as st
import time

# 초기화
if 'y' not in st.session_state:
    st.session_state.y = 300  # 캐릭터 시작 높이
    st.session_state.vy = 0   # 초기 속도
    st.session_state.jump = False
    st.session_state.score = 0
    st.session_state.game_over = False

# 물리 상수
GRAVITY = 1
JUMP_STRENGTH = -15
FLOOR_Y = 300

st.title("🦘 Streamlit 점프킹 미니게임")

canvas = st.empty()

# 점프 버튼
col1, col2 = st.columns([1, 3])
with col1:
    if st.button("⬆️ 점프", use_container_width=True) and not st.session_state.game_over:
        if st.session_state.y >= FLOOR_Y:
            st.session_state.vy = JUMP_STRENGTH

# 게임 루프
if not st.session_state.game_over:
    for _ in range(1):  # 1 frame per run
        st.session_state.vy += GRAVITY
        st.session_state.y += st.session_state.vy

        if st.session_state.y >= FLOOR_Y:
            st.session_state.y = FLOOR_Y
            st.session_state.vy = 0

        if st.session_state.y > 600:
            st.session_state.game_over = True

        st.session_state.score += 1

# 화면 렌더링
canvas.markdown(
    f"""
    <div style='position: relative; width: 400px; height: 600px; background: skyblue; border: 2px solid black;'>
        <div style='position: absolute; bottom: 0px; width: 100%; height: 20px; background: green;'></div>
        <div style='position: absolute; bottom: {st.session_state.y}px; left: 180px; width: 40px; height: 40px; background: red; border-radius: 10px;'></div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(f"🧮 점수: {st.session_state.score}")

if st.session_state.game_over:
    st.error("💀 게임 오버!")
    if st.button("🔁 다시 시작"):
        st.session_state.y = 300
        st.session_state.vy = 0
        st.session_state.score = 0
        st.session_state.game_over = False
