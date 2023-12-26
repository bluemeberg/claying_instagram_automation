# 크리에이터 채널 정보
# 크리에이터 최신 영상 정보
# 크리에이터 인기 영상 정보

from datetime import datetime
from googleapiclient.discovery import build
import numpy as np
import re
from utils import parse_duration
from youtube_api import get_youtube_video_comments, get_youtube_video_info
youtube_api_key = "AIzaSyBuYLIe-bOsTMtaHBX0Uft1vBSoV1RvBJQ"  # Replace with your actual API key
youtube_non_credentials = build('youtube', 'v3', developerKey=youtube_api_key)

# 채널 명, 채널 개인 설정명, 채널 썸네일, 구독자 수, 총 조회 수, 총 영상 갯수
def get_creator_channel_info(channelId) :
    try :
        request = youtube_non_credentials.channels().list(
            part='snippet,statistics',
            id=channelId,
        )
        response = request.execute()
        channel_info = response['items'][0]
        channel_title = channel_info['snippet']['title']
        channel_customUrl = channel_info['snippet'].get("customUrl")
        thumbnails = channel_info["snippet"]["thumbnails"]
        thumbnail_url = thumbnails.get("high", thumbnails.get("medium"))["url"]
        channel_viewcount = channel_info['statistics']['viewCount']
        channel_subs = channel_info['statistics']['subscriberCount']
        channel_videocount = channel_info['statistics']['videoCount']
    except : 
        print("에러")
    return channel_title, channel_customUrl, thumbnail_url, channel_subs, channel_viewcount, channel_videocount

# 최신 영상 10개에 대한 정보, 영상 업로드 평균 주기
# 최신 영상 10개에 대한 정보 : 영상 업로드 날짜, 영상 제목, 영상 태그, 영상 조회수, 영상 좋아요 수, 영상 댓글 수
def get_creator_latest_videos(channelId) :
    try :
        popular_comments = []
        request = youtube_non_credentials.search().list(
            part='snippet',
            channelId=channelId,
            order='date',
            maxResults= 50
        )
        response = request.execute()
        latest_videos=response['items']
        latest_video_ids = []
        latest_video_infos = []
        # videoId를 가져오는 코드 작성
        cnt = 0
        for item in latest_videos : 
            if 'id' in item and 'videoId' in item['id'] :
                temp_video = get_youtube_video_info(video=item['id']['videoId'])
                print(temp_video)
                if (temp_video != None) :
                    latest_video_infos.append(temp_video)
                    latest_video_ids.append(item['id']['videoId'])
                    if len(latest_video_ids) == 10 :
                        break
        # 최근 업로드 평균 주기는 최신 영상 5개 기준으로 영상 별 업로드 기간 차이에 대한 평균 기간을 산출
        print(f"쇼츠 제외 한 최신 5개 영상ID : {latest_video_ids}")
        print(f"최신 5개 영상들에 대한 영상 정보 : {latest_video_infos}")
        # 댓글 코멘트 전체 받아오기 위한 페이지네이션 
        for video in latest_video_ids :
            top_comments = get_youtube_video_comments(video=video)
            popular_comments.extend(top_comments)
        print(f"최신 10개 영상들의 인기 댓글 중 글자 수 50개 이상 350개 이하 댓글 중 좋아요 수 높은 TOP5 댓글들 영상 별 모음 : {popular_comments}")
        #최신 영상에 대한 썸네일, 태그, 타이틀, 업로드 날짜, 조회수 가져오기
        # latest_published_ats = []
        # print(latest_published_ats)
        # dates = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ') for date in latest_published_ats]
        # dates.sort()
        # # 날짜 간 차이 계산
        # differences = [dates[i+1] - dates[i] for i in range(len(dates)-1)]
        # # 평균 주기 계산 (초 단위로 변환 후 평균 계산)
        # average_period_seconds = np.mean([diff.total_seconds() for diff in differences])

        # # 결과 출력 (일 단위로 변환)
        # average_period_days = average_period_seconds / (60 * 60 * 24)
        # print(f"Average period: {average_period_days} days")
        return latest_video_infos, popular_comments
    except :
        print("채널 에러")


# 인기 영상 10개에 대한 정보 및 인기 코멘트 가져오기
# 인기 영상 정보 : 영상 업로드 날짜, 영상 제목, 영상 태그, 영상 조회수, 영상 좋아요 수, 영상 코멘트 수
# 인기 코멘트 : 코멘트 길이 50글자 이상, 200글자 이하인 코멘트 대상으로 댓글, 댓글 좋아요 수, 댓글 게시일 가져오기
# 인기 영상 중 1M1S 이상의 최초 영상에 대한 정보를 리턴한다
def get_creator_popular_videos(channelId) :
    try :
        # 크리레이터 추천 사유에 해당하는 댓글
        popular_comments = []
        request = youtube_non_credentials.search().list(
            part='snippet',
            channelId=channelId,
            order='viewCount',
            maxResults= 50
        )
        response = request.execute()
        popular_videos=response['items']
        # 댓글을 가지고 오기 위한 인기 영상 ID 추출 배열
        popular_video_ids = []
        # 필터링 된 영상 ID 별 정보를 담는 배열
        popular_video_infos = []
        # videoId를 가져오는 코드 작성
        cnt = 0
        for item in popular_videos : 
            if 'id' in item and 'videoId' in item['id'] :
                    temp_video = get_youtube_video_info(video=item['id']['videoId'])
                    if (temp_video != None) :
                        popular_video_infos.append(temp_video)
                        popular_video_ids.append(item['id']['videoId'])
                        if len(popular_video_ids) == 10 :
                            break
        # videoId 별로 인기 코멘트 5개씩 가져오기
        print(f"쇼츠 제외 한 TOP5 인기 영상ID : {popular_video_ids}")
        print(f"TOP5 인기 영상들에 대한 영상 정보 : {popular_video_infos}")
        # 댓글 코멘트 전체 받아오기 위한 페이지네이션
        for video in popular_video_ids :
            top_comments = get_youtube_video_comments(video=video)
            popular_comments.extend(top_comments)
        # 인기 영상에 대한 썸네일, 태그, 타이틀, 업로드 날짜, 조회수 가져오기
        print(f"TOP10 인기 영상들의 인기 댓글 중 글자 수 50개 이상 200개 이하 댓글 중 좋아요 수 높은 TOP5 댓글들 영상 별 모음 : {popular_comments}")
        # 인기순, 최신 videoId 별로 tags와 title 정보 추출하고 gpt통해서 상세 카테고리 분석하기
        # 상세 카테고리, 영상 썸네일, 영상 업로드, 조회수 정보를 묶음으로 최신, 인기순, 인기 급상승 순 카테고리로 재 묶음하기
        return popular_video_infos, popular_comments
    except :
        print("채널 에러 ")

