import streamlit as st
from engine import Engine
from annotated_text import annotated_text

st.set_page_config(page_title="Naive ContextCue", layout="centered")


@st.cache_resource
def get_engine():
    return Engine()


def main():
    if len(st.session_state) == 0:
        st.session_state["engine"] = get_engine()

    st.title("Naive ContextCue")

    st.subheader("Input Option")
    input_option = st.radio("Input Option", ("Manual entry", "Pick sample"), horizontal=True, label_visibility="collapsed")

    st.subheader("Input Text")
    if input_option == "Pick sample":
        st.selectbox(
            "Samples",
            [
                "Autonomous cars shift insurance liability toward manufacturers.",
                "Basic Linear Algebra Subprograms is a specification that prescribes a set of low-level routines for performing common linear algebra operations such as vector addition, scalar multiplication, dot products, linear combinations, and matrix multiplication.",
            ],
            key="input_text",
            label_visibility="collapsed",
        )
    else:
        st.text_area("Input Text", placeholder="Type or paste the text here.", key="input_text", label_visibility="collapsed")

    if st.button("Run"):
        with st.spinner("Running..."):
            output = st.session_state["engine"](st.session_state["input_text"])
        st.subheader("Output Text")
        annotated_text(output)


if __name__ == "__main__":
    main()
