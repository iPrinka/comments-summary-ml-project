import streamlit as st
import pandas as pd
from src.comments import fetch_comments
from src.utils import text_to_chunks, summarize_chunk
import transformers
import io

st.title("Youtube Comments Summarizer")

st.write(
    "Use this tool to generate summaries from comments under any Youtube video."
    "The Tool uses OpenAI's APIs to generate the summaries"
)
st.write(
    "The app is currently a POC. It extracts comments from the selected Youtube video, "
    "chunks the text, summarizes it and then returns the same."
)

left, right = st.columns(2)
form = left.form("template_form")

url_input = form.text_input(
    "Enter Youtube url",
    placeholder="",
    value="",
)

submit = form.form_submit_button("Get Summary")

# text = ""
with open('comments.txt') as fp:
    text = fp.read()
    # for entry in contents:
    #     "/n".join(entry)

with st.container():
    target = io.open("summary.txt", 'w', encoding='utf-8')
    if submit and url_input:
        with st.spinner("Fetching Summary..."):
            fetch_comments(url_input)
            # text = pd.read_clipboard('comments.txt')
            tokenizer = transformers.GPT2TokenizerFast.from_pretrained("gpt2")
            chunks = text_to_chunks(text, tokenizer)
            summaries = []
            for chunk in chunks:
                summary = summarize_chunk(chunk)
                summaries.append(summary)

            for summ in summaries:
            #     # fp = "summary.txt"
            #     # with open(mode='w') as f:
            #     #     summary = "\n".join(summs)
            #     #     print(summary)
            #     print(summs)
            #     target.write(summs+"\n")

            # print("Reached Here")
            # # text = pd.read_csv('summary.txt')
            # with open('summary.txt') as fp:
            #     summ= fp.read()
                with right:
                    right.write(f"{summ}")