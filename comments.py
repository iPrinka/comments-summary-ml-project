import json, io, os
from googleapiclient.discovery import build
from pytube import extract

from dotenv import load_dotenv

load_dotenv()

api_server_name = os.getenv('API_SERVICE_NAME')
api_version = os.getenv('API_VERSION')
youtube_api_key = os.getenv('YOUTUBE_API_KEY')

def get_comments_from_url(video_link):
    youtube = start_youtube_service()
    video_id = extract_video_id_from_link(video_link)
   
    request = youtube.commentThreads().list(
        part="snippet,replies",                     
        videoId=video_id,
        textFormat='plainText',
        maxResults=5000
    )
    response = request.execute()
    response_json = json.loads(json.dumps(response,indent=2))
    return response_json['items']

def start_youtube_service():
     return build(api_server_name, api_version, developerKey=youtube_api_key)

def extract_video_id_from_link(url):
    return extract.video_id(url)

def fetch_comments(url):
    target = io.open("comments.txt", 'w', encoding='utf-8')
    comments = get_comments_from_url(url)
    all_comments = []
    for thread in comments:
        comment = {}
        comment['content'] = thread['snippet']['topLevelComment']['snippet']['textOriginal']
        target.write(comment['content']+"\n")
        replies = []
        if 'replies' in thread:
            for reply in thread['replies']['comments']:
                reply_text = reply['snippet']['textOriginal']
                target.write(reply_text+"\n")
                replies.append(reply_text)
            comment['replies'] = replies
        
        all_comments.append(comment)

# https://www.youtube.com/watch?v=hj7da0sljvs