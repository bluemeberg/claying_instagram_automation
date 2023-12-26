from googleapiclient.discovery import build
from utils import parse_duration
youtube_api_key = "AIzaSyBuYLIe-bOsTMtaHBX0Uft1vBSoV1RvBJQ"  # Replace with your actual API key
youtube_non_credentials = build('youtube', 'v3', developerKey=youtube_api_key)

import re

def get_youtube_video_comments(video) :
    video_comments = []
    next_page_token = None
    while True :
        request = youtube_non_credentials.commentThreads().list(
        part='snippet',
        videoId=video,
        order='relevance',
        pageToken = next_page_token
        )
        response = request.execute()
        comments=response['items']
        next_page_token = response.get('nextPageToken')
        # 유의미한 인기 코멘트 도출
        # 글자 수
        for comment in comments[1:] :
            temp_comments = {}
            if 'snippet' in comment and 'topLevelComment' in comment['snippet'] and 'snippet' in comment['snippet']['topLevelComment']:
                if len(comment['snippet']['topLevelComment']['snippet']['textOriginal']) >= 50 and len(comment['snippet']['topLevelComment']['snippet']['textOriginal']) <= 350:
                    # Check for 10 or more consecutive "ㅋ" characters
                    if not re.search(r"ㅋ{10,}", comment['snippet']['topLevelComment']['snippet']['textOriginal']) :
                        temp_comments['comment'] = comment['snippet']['topLevelComment']['snippet']['textOriginal']
                        temp_comments['likeCount'] = comment['snippet']['topLevelComment']['snippet']['likeCount']
                        temp_comments['updatedAt'] = comment['snippet']['topLevelComment']['snippet']['updatedAt']
                        video_comments.append(temp_comments)
        if not next_page_token:
            break
    top_comments = sorted(video_comments, key=lambda x: x['likeCount'], reverse=True)[:5]
    return top_comments

# tags가 존재하고 영상 길이가 62초인 영상만 리턴한다
def get_youtube_video_info(video) :
    request = youtube_non_credentials.videos().list(
    part='snippet,statistics,contentDetails',
    id=video,
    )
    response = request.execute()
    video_infos=response['items']
    if 'tags' in video_infos[0]['snippet'] :
        video_duration_str = video_infos[0]['contentDetails']['duration']
        video_duration = parse_duration(video_duration_str)
        print(video_duration)
        print(video_infos[0]['snippet'])
        if (video_duration > 62) :
            published_at = video_infos[0]['snippet']['publishedAt']
            thumbnails = video_infos[0]['snippet']['thumbnails']
            thumbnail_url = thumbnails.get('standard', {}).get('url', '') or \
                thumbnails.get('high', {}).get('url', '') or \
                thumbnails.get('medium', {}).get('url', '')
            title = video_infos[0]['snippet']['title']
            tags = video_infos[0]['snippet'].get("tags", None)
            view_count = video_infos[0]['statistics']['viewCount']
            like_count = video_infos[0]['statistics']['likeCount']
            comment_count = video_infos[0]['statistics']['commentCount']
            temp_video = {}
            temp_video['published_at'] = published_at
            temp_video['thumbnail_url'] = thumbnail_url
            temp_video['title'] = title
            temp_video['tags'] = tags
            temp_video['view_count'] = view_count
            temp_video['like_count'] = like_count
            temp_video['comment_count'] = comment_count
            return temp_video