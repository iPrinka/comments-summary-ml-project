# youtube-comments-summary-project

Please find my Streamlit app hosted [here](https://iprinka-comments-summary-ml-project-app-xobtj4.streamlit.app/)
<br/>
Please note that if you face an error, the Open AI API credits on my account might have expired :D

## Project Summary

The goal of this model is to provide a summary of comment threads for any given Youtube video.

## Flow Diagram

![Flow Diagram](https://github.com/Priyanka-Gangadhar-Palshetkar/comments-summary-ml-project/blob/main/assets/flow-chart.png?raw=true)

## Approach

* In this project, I will be using [Youtube API V3](https://developers.google.com/youtube/v3) to fetch all comment threads for any given youtube video id.
* I used Streamlit to build this application. It takes a Youtube video url as input. Using the Youtube API, I fetch all the comment threads under that video and provide it to the Tokenizer to break the text into chunks. 
* Then I provide each chunk as an input to the Completions API with the prompt - “Provide a summary of the comments below.” followed by the chunk of comments. The model then returns a brief summary of how people are reacting to that video.

## How to use

1. Create a virtual environment (python3 -m venv venv && source venv/bin/activate)

2. Download all the dependencies by running `make requirements` in your terminal

3. Create a project on Google cloud console and enable Youtube API V3 for your project. Follow instructions [here.](https://console.developers.google.com/apis/api/youtube.googleapis.com/overview)

4. Create a .streamlit folder at the source level and add a secrets.toml file to it.

5. Ensure your Youtube API keys are set as `API_SERVICE_NAME`, `API_VERSION`, `YOUTUBE_API_KEY` in the secrets.toml file (check the secrets.toml.example file for reference). Please find the details to generate the API key [here.](https://developers.google.com/youtube/registering_an_application)

6. Ensure your OpenAI API key is set as an environment variable `OPENAI_API_KEY` in the secrets.toml file (check the secrets.toml.example file for reference). (see best practices around API key safety [here](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety))

7. Run the [streamlit](https://streamlit.io/) app by running `make run`

8. Open the app in your browser at `http://localhost:8501`

## Example

![App_Demo](https://github.com/Priyanka-Gangadhar-Palshetkar/comments-summary-ml-project/blob/main/assets/video_100_comments.png?raw=true)
