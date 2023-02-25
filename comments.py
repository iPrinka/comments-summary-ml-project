import json, io, os
from googleapiclient.discovery import build
from pytube import extract

from dotenv import load_dotenv

load_dotenv()

api_server_name = os.getenv('API_SERVICE_NAME')
api_version = os.getenv('API_VERSION')
youtube_api_key = os.getenv('YOUTUBE_API_KEY')

def start_youtube_service():
     return build(api_server_name, api_version, developerKey=youtube_api_key)

def extract_video_id_from_link(url):
    return extract.video_id(url)

def get_comments_thread(youtube, video_id, next_page_token):
    results = youtube.commentThreads().list(
        part="snippet,replies",                     
        videoId=video_id,
        textFormat='plainText',
        maxResults=100,
        pageToken = next_page_token
    ).execute()
    return results

def load_comments_in_format(comments, mode):
    target = io.open("comments.txt", mode, encoding='utf-8')
    all_comments = []
    for thread in comments["items"]:
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

def fetch_comments(url):
    youtube = start_youtube_service()
    video_id = extract_video_id_from_link(url)
    next_page_token = ''
   
    data = get_comments_thread(youtube, video_id, next_page_token)
    if "nextPageToken" in data:
        next_page_token = data["nextPageToken"]
    load_comments_in_format(data, 'w')

    while next_page_token:
        data = get_comments_thread(youtube, video_id, next_page_token)
        if "nextPageToken" in data:
            next_page_token = data["nextPageToken"]
        else:
            next_page_token = ''
        load_comments_in_format(data, 'a')

# https://www.youtube.com/watch?v=hj7da0sljvs