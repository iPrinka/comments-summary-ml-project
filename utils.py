import os
import nltk
import openai
import transformers
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)
from dotenv import load_dotenv
from typing import List


load_dotenv()
nltk.download('punkt')

openai.api_key = os.getenv('OPENAI_API_KEY')

def text_to_chunks(input_text: str, tokenizer: transformers.PreTrainedTokenizer, max_token_sz: int = 1024, overlapping_sentences: int = 10) -> List[str]:
    sentences = nltk.sent_tokenize(input_text)
    chunks = []

    first_sentence = 0
    last_sentence = 0
    while last_sentence <= len(sentences) - 1:
        last_sentence = first_sentence
        chunk_parts = []
        chunk_size = 0
        for sentence in sentences[first_sentence:]:
            sentence_sz = len(tokenizer.encode(sentence))
            if chunk_size + sentence_sz > max_token_sz:
                break
            
            chunk_parts.append(sentence)
            chunk_size += sentence_sz
            last_sentence += 1

        chunks.append(" ".join(chunk_parts))
        first_sentence = last_sentence - overlapping_sentences
    return chunks

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
def completion_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)


def summarize_chunk(chunk: str, max_tokens: int = 512, temperature: int = 0) -> str:
    response = completion_with_backoff(
        model="text-davinci-003",
        prompt=f'Provide a summary of the comments."'
        f"\n###\nComments:{chunk}\n###\n-",
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response['choices'][0]['text'].strip()