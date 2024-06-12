import streamlit as st
from comments import fetch_comments
from utils import get_summary


st.title("Youtube Comments Summarizer")

st.write(
    "Use this tool to generate summaries from comments under any Youtube video."
    "The Tool uses Google Gemini paired with Lang Chain to generate the summaries."
)

st.write()

left, right = st.columns(2)
form = left.form("template_form")

url_input = form.text_input(
    "Enter Youtube video url",
    placeholder="",
    value="",
)

submit = form.form_submit_button("Get Summary")

gemini_api_key = st.secrets['GEMINI_API_KEY']

with st.container():
    if submit and url_input:
        with st.spinner("Fetching Summary..."):

            # Get Comments from Youtube API - INPUT
            text = fetch_comments(url_input)

            # Tokenization and Summarization  - MAIN CODE
            final_summary = get_summary(text)

            # Display the output on Streamlit - OUTPUT
            with right:
                right.write(f"{final_summary}")