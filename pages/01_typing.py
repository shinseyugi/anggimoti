import streamlit as st
import random
import time

# 기출 단어 예시
vocab = [
    {"word": "도식화", "meaning": "복잡한 개념이나 내용을 도표나 그림으로 나타냄"},
    {"word": "귀납", "meaning": "개별적인 사실에서 일반적인 결론을 이끌어냄"},
    {"word": "환기", "meaning": "주의를 불러일으킴 또는 공기 순환"},
    {"word": "반추", "meaning": "지난 일을 되새김"},
    {"word": "은유", "meaning": "직접적으로 비유하는 표현"},
]

# 상태 초기화
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.start_time = time.time()
    st.session_state.correct_count = 0
    st.session_state.total = len(vocab)

# 현재 단어 불러오기
current = vocab[st.session_state.index]
st.markdown(f"### 🧠 의미: {current['meaning']}")
user_input = st.text_input("💬 단어를 입력하세요:", key=f"input_{st.session_state.index}")

# 정답 체크
if user_input:
    if user_input.strip() == current["word"]:
        st.success("✅ 정답입니다!")
        st.session_state.correct_count += 1
        st.session_state.index += 1
        if st.session_state.index >= st.session_state.total:
            end_time = time.time()
            total_time = round(end_time - st.session_state.start_time, 2)
            accuracy = (st.session_state.correct_count / st.session_state.total) * 100
            st.markdown("### 🎉 연습 완료!")
            st.markdown(f"- 걸린 시간: {total_time}초")
            st.markdown(f"- 정확도: {accuracy:.1f}%")
            st.button("🔁 다시 시작", on_click=lambda: st.session_state.clear())
        else:
            st.experimental_rerun()
    else:
        st.error("❌ 오타가 있어요! 다시 확인해보세요.")
