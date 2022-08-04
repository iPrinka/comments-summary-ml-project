from config.config import YOUTUBE_API_KEY
from pyyoutube import Api
from pytube import extract

api = Api(api_key=YOUTUBE_API_KEY)

def extract_video_id_from_link(url):
    return extract.video_id(url)

def get_comments(video_link):
    video_id = extract_video_id_from_link(video_link)
    comments = api.get_comment_threads(video_id=video_id, count=None)
    return comments

response = get_comments("https://www.youtube.com/watch?v=2jkvr8cHzr4")
print(response.items[0].to_json())