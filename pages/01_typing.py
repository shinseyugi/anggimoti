import streamlit as st
import random

# 예시 기출 어휘
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
    st.session_state.correct_count = 0
    st.session_state.total = len(vocab)

# 현재 문장
current = vocab[st.session_state.index]
target_text = f"{current['word']}: {current['meaning']}"

st.markdown("### ✍️ 다음 문장을 그대로 입력하세요:")
st.markdown(f"#### `{target_text}`")

# 사용자 입력
typed = st.text_input("💬 여기 입력:", key=f"input_{st.session_state.index}")

# 확인
if typed.strip() == target_text:
    st.success("✅ 정확하게 입력했어요!")
    st.session_state.correct_count += 1
    st.session_state.index += 1

    # 끝났는지 확인
    if st.session_state.index >= st.session_state.total:
        st.balloons()
        st.markdown("### 🎉 모든 단어 입력 완료!")
        st.markdown(f"- 정확 입력 수: {st.session_state.correct_count} / {st.session_state.total}")
        if st.button("🔁 다시 시작"):
            st.session_state.index = 0
            st.session_state.correct_count = 0
    else:
        st.experimental_rerun()
elif typed:
    if not target_text.startswith(typed):
        st.error("❌ 오타가 있는 것 같아요. 다시 확인해보세요.")

