# youtube-comments-summary-project

## Project Summary

The goal of this model is to provide a summary of comment threads for any given Youtube video in the following formats:

* Paragraph highlighting the key points - "actual summary"
* Word cloud of reactions on the video

## Approach

* In this project, I will be using [Youtube API V3](https://developers.google.com/youtube/v3) to fetch all comment threads for any given youtube video id.

## How to use

1. Download all the dependencies by running the following pip command in your terminal

        pip install -r requirements.txt

2. Create a project on Google cloud console and enable Youtube API V3 for your project. Follow instructions [here.](https://console.developers.google.com/apis/api/youtube.googleapis.com/overview)

3. Ensure your Youtube API keys are set as environment variables `API_SERVICE_NAME`, `API_VERSION`, `YOUTUBE_API_KEY`. Please find the details to generate the API key [here.](https://developers.google.com/youtube/registering_an_application)

4. Ensure your OpenAI API key is set as an environment variable `OPENAI_API_KEY` (see best practices around API key safety [here](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety))

5. Run the [streamlit](https://streamlit.io/) app by running `make run`

6. Open the app in your browser at `http://localhost:8501`

## Example

![alt text](https://github.com/Priyanka-Gangadhar-Palshetkar/comments-summary-ml-project/assets/example.png?raw=true)
