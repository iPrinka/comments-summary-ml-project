import json
from googleapiclient.discovery import build
from config.config import YOUTUBE_API_KEY, API_SERVICE_NAME, API_VERSION
from pyyoutube import Api
from pytube import extract

api = Api(api_key=YOUTUBE_API_KEY)

def extract_video_id_from_link(url):
    return extract.video_id(url)

def get_comments(video_link):
    video_id = extract_video_id_from_link(video_link)

    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=YOUTUBE_API_KEY)
    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=video_id,
        textFormat='plainText',
        maxResults=100
    )
    response = request.execute()
    response_json = json.dumps(response,indent=2)
    return(response_json)


def main():
    # test = get_comments("https://www.youtube.com/watch?v=2jkvr8cHzr4&t=5s")
    test = get_comments("https://www.youtube.com/watch?v=EYncNbM9HMs")
    print(test)

if __name__ == "__main__":
    main()