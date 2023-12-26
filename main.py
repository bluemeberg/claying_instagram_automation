from get_youtube_info import get_creator_channel_info
from get_youtube_info import get_creator_latest_videos
from get_youtube_info import get_creator_popular_videos
from classify_video_category import classify_video_category
from make_recommendations import make_creator_recommend_comment
from utils import extract_text_inside_braces
import json
# 댓글과 채널 타이틀 가져와야함
channel_title, channel_customUrl, thumbnail_url, channel_subs, channel_viewcount, channel_videocount =  get_creator_channel_info(channelId="UC-gHYajFU533TfLaDaw0PCA")
latest_video_infos,popular_comments = get_creator_latest_videos(channelId="UC5pbeFWTPAUdKu65kBROsBg")
print(latest_video_infos)
print(popular_comments)
# popular_video_infos, popular_comments = get_creator_popular_videos(channelId="UC-gHYajFU533TfLaDaw0PCA")
# make_creator_recommend_comment(data=popular_comments, channel_title=channel_title)
# print("latest result", latest_video_infos)
# # print("popular result", popular_video_infos)

for video in latest_video_infos :
    print(video)
    tags = video["tags"]
    title = video["title"]
    print(tags, title)
    category = classify_video_category(tags=tags, title=title)
    print(category)
    category_without_braces = extract_text_inside_braces(category)
    print(category_without_braces)
    video["category"] = category_without_braces

print(latest_video_infos)
# for video in popular_video_infos :
#     tags = video["tags"]
#     title = video["title"]
#     print(tags, title)
#     category = classify_video_category(tags=tags, title=title)
#     print(category)
#     category_without_braces = extract_text_inside_braces(category)
#     print(category_without_braces)
    
