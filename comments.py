import os
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

def load_comments_in_format(comments):
    all_comments = []
    all_comments_string = ""
    for thread in comments["items"]:
        comment = {}
        comment['content'] = thread['snippet']['topLevelComment']['snippet']['textOriginal']
        all_comments_string = all_comments_string + comment['content']+"\n"
        replies = []
        if 'replies' in thread:
            for reply in thread['replies']['comments']:
                reply_text = reply['snippet']['textOriginal']
                all_comments_string = all_comments_string + reply_text+"\n"
                replies.append(reply_text)
            comment['replies'] = replies
        
        all_comments.append(comment)
    return all_comments_string

def fetch_comments(url):
    youtube = start_youtube_service()
    video_id = extract_video_id_from_link(url)
    next_page_token = ''
   
    data = get_comments_thread(youtube, video_id, next_page_token)
    if "nextPageToken" in data:
        next_page_token = data["nextPageToken"]
    all_comments = load_comments_in_format(data)

    while next_page_token:
        data = get_comments_thread(youtube, video_id, next_page_token)
        if "nextPageToken" in data:
            next_page_token = data["nextPageToken"]
        else:
            next_page_token = ''
        all_comments = all_comments + load_comments_in_format(data)

    return all_comments