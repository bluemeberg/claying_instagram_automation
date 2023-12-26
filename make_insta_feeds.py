import requests
from utils import change_date
from utils import convert_number_format

def make_key_comments_feed(creator_title, first_recommendation, first_recommendation_comments, second_recommendation,second_recommendation_comments, third_recommendation, third_recommendation_comments, channel_title, channel_thumbnail ) :
    print(creator_title, first_recommendation, second_recommendation, first_recommendation_comments, second_recommendation_comments)
    # 22개 변수 세팅
    param1_1st_key_point = first_recommendation
    param2_1st_key_point_comment_1_date = change_date(first_recommendation_comments[0]['updatedAt'])
    param3_1st_key_point_comment_1_like_number = str(convert_number_format(first_recommendation_comments[0]['likeCount']))
    param4_1st_key_point_comment_1_content = first_recommendation_comments[0]['comment']
    param5_1st_key_point_comment_2_date =  change_date(first_recommendation_comments[1]['updatedAt']) if len(first_recommendation_comments) >1 else None
    param6_1st_key_point_comment_2_like_number = str(convert_number_format(first_recommendation_comments[1]['likeCount'])) if len(first_recommendation_comments) >1 else None
    param7_1st_key_point_comment_2_content = first_recommendation_comments[1]['comment'] if len(first_recommendation_comments) >1 else None
    param8_2nd_key_point = second_recommendation
    param9_2nd_key_point_comment_1_date = change_date(second_recommendation_comments[0]['updatedAt'])
    param10_2nd_key_point_comment_1_like_number = str(convert_number_format(second_recommendation_comments[0]['likeCount']))
    param11_2nd_key_point_comment_1_content = second_recommendation_comments[0]['comment']
    param12_2nd_key_point_comment_2_date = change_date(second_recommendation_comments[1]['updatedAt']) if len(second_recommendation_comments) >1 else None
    param13_2nd_key_point_comment_2_like_number = str(convert_number_format(second_recommendation_comments[1]['likeCount'])) if len(second_recommendation_comments) >1 else None
    param14_2nd_key_point_comment_2_content = second_recommendation_comments[1]['comment'] if len(second_recommendation_comments) >1 else None
    param15_3rd_key_point = third_recommendation
    param16_3rd_key_point_comment_1_date = change_date(third_recommendation_comments[0]['updatedAt'])
    param17_3rd_key_point_comment_1_like_number = str(convert_number_format(third_recommendation_comments[0]['likeCount']))
    param18_3rd_key_point_comment_1_content = third_recommendation_comments[0]['comment']
    param19_3rd_key_point_comment_2_date = change_date(third_recommendation_comments[1]['updatedAt']) if len(third_recommendation_comments) >1 else None
    param20_3rd_key_point_comment_2_number = str(convert_number_format(third_recommendation_comments[1]['likeCount'])) if len(third_recommendation_comments) >1 else None
    param21_3rd_key_point_comment_2_content =  third_recommendation_comments[1]['comment'] if len(third_recommendation_comments) >1 else None
    param22_creator_thumbnail = channel_thumbnail
    param23_creator_title = channel_title
    # bannerbear api call
    bannerbear_api_key = "bb_pr_e999f30ac6febcf2fbe3b0fd80bc68"
    headers = {
    'Authorization': f'Bearer {bannerbear_api_key}'
    }
    payload = {
  "template": "RnxGpW5lvjB0bEXrJ1",
  "modifications": [
    {
      "name": "background",
      "color": None
    },
    {
      "name": "logo",
      "text": "CLAYING",
      "color": None,
      "background": None
    },
    {
      "name": "logo_catchphrase",
      "text": "크리에이티브한 플레잉, 클레잉",
      "color": None,
      "background": None
    },
    {
      "name": "logo_boundary_line",
      "color": None
    },
    {
      "name": "title",
      "text": "Key Comments",
      "color": None,
      "background": None
    },
    {
      "name": "sub_title",
      "text": "구독자들과 어떻게 소통하고 있을까요?",
      "color": None,
      "background": None
    },
    {
      "name": "title_boundary_line",
      "color": None
    },
    {
      "name": "1st_key_point_indicator_box",
      "color": None
    },
    {
      "name": "1st_key_point_indicator",
      "text": "1",
      "color": None,
      "background": None
    },
    {
      "name": "param1_1st_key_point",
      "text": param1_1st_key_point,
      "color": None,
      "background": None
    },
    {
      "name": "1st_key_point_comment#1_box",
      "color": None
    },
    {
      "name": "param2_1st_key_point_comment#1_date",
      "text": param2_1st_key_point_comment_1_date,
      "color": None,
      "background": None
    },
    {
      "name": "thumbs_image#1",
      "image_url": "https://claying.io/thumbs-up.png"
    },
    {
      "name": "param3_1st_key_point_comment#1_like_number",
      "text": param3_1st_key_point_comment_1_like_number,
      "color": None,
      "background": None
    },
    {
      "name": "param4_1st_key_point_comment#1_content",
      "text": param4_1st_key_point_comment_1_content,
      "color": None,
      "background": None
    },
    {
      "name": "1st_key_point_comment#2_box",
      "color": None
    },
    {
      "name": "param5_1st_key_point_comment#2_date",
      "text": param5_1st_key_point_comment_2_date,
      "color": None,
      "background": None
    },
    {
      "name": "thumbs_image#2",
      "image_url": "https://claying.io/thumbs-up.png"
    },
    {
      "name": "param6_1st_key_point_comment#2_like_number",
      "text": param6_1st_key_point_comment_2_like_number,
      "color": None,
      "background": None
    },
    {
      "name": "param7_1st_key_point_comment#2_content",
      "text": param7_1st_key_point_comment_2_content,
      "color": None,
      "background": None
    },
    {
      "name": "2nd_key_point_indicator_box",
      "color": None
    },
    {
      "name": "2nd_key_point_indicator",
      "text": "2",
      "color": None,
      "background": None
    },
    {
      "name": "param8_2nd_key_point",
      "text": param8_2nd_key_point,
      "color": None,
      "background": None
    },
    {
      "name": "2nd_key_point_comment#1_box",
      "color": None
    },
    {
      "name": "param9_2nd_key_point_comment#1_date",
      "text": param9_2nd_key_point_comment_1_date,
      "color": None,
      "background": None
    },
    {
      "name": "thumbs_image#3",
      "image_url": "https://claying.io/thumbs-up.png"
    },
    {
      "name": "param10_2nd_key_point_comment#1_like_number",
      "text": param10_2nd_key_point_comment_1_like_number,
      "color": None,
      "background": None
    },
    {
      "name": "param11_2nd_key_point_comment#1_content",
      "text": param11_2nd_key_point_comment_1_content,
      "color": None,
      "background": None
    },
    {
      "name": "2nd_key_point_comment#2_box",
      "color": None
    },
    {
      "name": "param12_2nd_key_point_comment#2_date",
      "text": param12_2nd_key_point_comment_2_date,
      "color": None,
      "background": None
    },
    {
      "name": "thumbs_image#4",
      "image_url": "https://claying.io/thumbs-up.png"
    },
    {
      "name": "param13_2nd_key_point_comment#2_like_number",
      "text": param13_2nd_key_point_comment_2_like_number,
      "color": None,
      "background": None
    },
    {
      "name": "param14_2nd_key_point_comment#2_content",
      "text": param14_2nd_key_point_comment_2_content,
      "color": None,
      "background": None
    },
    {
      "name": "3rd_key_point_indicator_box",
      "color": None
    },
    {
      "name": "3rd_key_point_indicator",
      "text": "3",
      "color": None,
      "background": None
    },
    {
      "name": "param15_3rd_key_point",
      "text": param15_3rd_key_point,
      "color": None,
      "background": None
    },
    {
      "name": "3rd_key_point_comment#1_box",
      "color": None
    },
    {
      "name": "param16_3rd_key_point_comment#1_date",
      "text": param16_3rd_key_point_comment_1_date,
      "color": None,
      "background": None
    },
    {
      "name": "thumbs_image#5",
      "image_url": "https://claying.io/thumbs-up.png"
    },
    {
      "name": "param17_3rd_key_point_comment#1_like_number",
      "text": param17_3rd_key_point_comment_1_like_number,
      "color": None,
      "background": None
    },
    {
      "name": "param18_3rd_key_point_comment#1_content",
      "text": param18_3rd_key_point_comment_1_content,
      "color": None,
      "background": None
    },
    {
      "name": "3rd_key_point_comment#2_box",
      "color": None
    },
    {
      "name": "param19_3rd_key_point_comment#2_date",
      "text": param19_3rd_key_point_comment_2_date,
      "color": None,
      "background": None
    },
    {
      "name": "thumbs_image#6",
      "image_url": "https://claying.io/thumbs-up.png"
    },
    {
      "name": "param20_3rd_key_point_comment#2_number",
      "text": param20_3rd_key_point_comment_2_number,
      "color": None,
      "background": None
    },
    {
      "name": "param21_3rd_key_point_comment#2_content",
      "text": param21_3rd_key_point_comment_2_content,
      "color": None,
      "background": None
    },
    {
      "name": "param22_creator_thumbnail",
      "image_url": param22_creator_thumbnail
    },
    {
      "name": "param23_creator_title",
      "text": param23_creator_title,
      "color": None,
      "background": None
    }
  ],
  "webhook_url": None,
  "transparent": False,
  "metadata": None
}
    response = requests.post('https://sync.api.bannerbear.com/v2/images',json=payload , headers=headers)
    print(response)
    if response.status_code == 200:
        image_url = response.json()['image_url']
        print("이미지가 생성되었습니다:", image_url)
        return image_url
    else:
        print("오류 발생:", response.status_code, response.text)
        return {"오류 발생 :", response.status_code, response.text}
    

# 최다 조회수 영상 정보, 최신 영상 정보 2개, 인기 급상승 영상 정보
    
def make_main_topics(popular_video_info, latest_video_infos, hot_video_info, creator_thumbnail, creator_title) :
    param1_todays_hot_video_category = ""
    param2_todays_hot_video_thumbnail = ""
    param3_todays_hot_video_title = ""
    param4_todays_hot_video_view_count = ""
    param5_todays_hot_video_upload_date= ""
    param6_todays_hot_video_like_count = ""
    param7_popular_video_category = popular_video_info["category"]
    param8_popular_video_thumbnail = popular_video_info["thumbnail_url"]
    param9_popular_video_title = popular_video_info["title"]
    param10_popular_video_view_count = popular_video_info["view_count"]
    param11_popular_video_upload_date = popular_video_info["published_at"]
    param12_popular_video_like_count = popular_video_info["like_count"]
    param13_latest_video1_category = latest_video_infos[0]["category"]
    param14_latest_video1_thumbanail = latest_video_infos[0]["thumbnail_url"]
    param15_latest_video1_title = latest_video_infos[0]["title"]
    param16_latest_video1_view_count =latest_video_infos[0]["view_count"]
    param17_latest_video1_upload_date =latest_video_infos[0]["published_at"]
    param18_latest_video1_like_count= latest_video_infos[0]["like_count"]
    param19_latest_video2_category =latest_video_infos[1]["category"]
    param20_lateet_video2_thumbnail =  latest_video_infos[1]["thumbnail_url"]
    param21_latest_video2_title = latest_video_infos[1]["title"]
    param22_latest_video2_view_count = latest_video_infos[1]["view_count"]
    param23_latest_video2_upload_date= latest_video_infos[1]["published_at"]
    param24_latest_video2_like_count = latest_video_infos[1]["like_count"]
    param25_creator_thumbnail = creator_thumbnail
    param26_creator_title = creator_title
    bannerbear_api_key = "bb_pr_e999f30ac6febcf2fbe3b0fd80bc68"
    headers = {
    'Authorization': f'Bearer {bannerbear_api_key}'
    }
    payload = {
  "template": "1oMJnB5rPPjQbl2wqL",
  "modifications": [
    {
      "name": "background",
      "color": None
    },
    {
      "name": "logo",
      "text": "CLAYING",
      "color": None,
      "background": None
    },
    {
      "name": "logo_catchphrase",
      "text": "크리에이티브한 플레잉, 클레잉",
      "color": None,
      "background": None
    },
    {
      "name": "logo_boundary_line",
      "color": None
    },
    {
      "name": "title",
      "text": "Main Topics",
      "color": None,
      "background": None
    },
    {
      "name": "sub_title",
      "text": "크리에이터가 주로 다루는 주제입니다.",
      "color": None,
      "background": None
    },
    {
      "name": "title_boundary_line",
      "color": None
    },
    {
      "name": "sub_title_todays_hot_videos",
      "text": "오늘 인기 급상승 영상",
      "color": None,
      "background": None
    },
    {
      "name": "param1_todays_hot_video_category",
      "text": param1_todays_hot_video_category,
      "color": None,
      "background": None
    },
    {
      "name": "param2_todays_hot_video_thumbnail",
      "image_url": param2_todays_hot_video_thumbnail
    },
    {
      "name": "param3_todays_hot_video_title",
      "text": param3_todays_hot_video_title,
      "color": None,
      "background": None
    },
    {
      "name": "param4_todays_hot_video_view_count",
      "text": param4_todays_hot_video_view_count,
      "color": None,
      "background": None
    },
    {
      "name": "param5_todays_hot_video_upload_date",
      "text": param5_todays_hot_video_upload_date,
      "color": None,
      "background": None
    },
    {
      "name": "param6_todays_hot_video_like_count",
      "text": param6_todays_hot_video_like_count,
      "color": None,
      "background": None
    },
    {
      "name": "sub_title_popular_video",
      "text": "최다 조회수 영상",
      "color": None,
      "background": None
    },
    {
      "name": "param7_popular_video_category",
      "text": param7_popular_video_category,
      "color": None,
      "background": None
    },
    {
      "name": "param8_popular_video_thumbnail",
      "image_url": param8_popular_video_thumbnail
    },
    {
      "name": "param9_popular_video_title",
      "text": param9_popular_video_title,
      "color": None,
      "background": None
    },
    {
      "name": "param10_popular_video_view_count",
      "text": param10_popular_video_view_count,
      "color": None,
      "background": None
    },
    {
      "name": "param11_popular_video_upload_date",
      "text": param11_popular_video_upload_date,
      "color": None,
      "background": None
    },
    {
      "name": "param12_popular_video_like_count",
      "text": param12_popular_video_like_count,
      "color": None,
      "background": None
    },
    {
      "name": "sub_title_latest_video",
      "text": "You can change this text",
      "color": None,
      "background": None
    },
    {
      "name": "param13_latest_video1_category",
      "text": param13_latest_video1_category,
      "color": None,
      "background": None
    },
    {
      "name": "param14_latest_video1_thumbanail",
      "image_url": param14_latest_video1_thumbanail
    },
    {
      "name": "param15_latest_video1_title",
      "text": param15_latest_video1_title,
      "color": None,
      "background": None
    },
    {
      "name": "param16_latest_video1_view_count",
      "text": param16_latest_video1_view_count,
      "color": None,
      "background": None
    },
    {
      "name": "param17_latest_video1_upload_date",
      "text": param17_latest_video1_upload_date,
      "color": None,
      "background": None
    },
    {
      "name": "param18_latest_video1_like_count",
      "text": param18_latest_video1_like_count,
      "color": None,
      "background": None
    },
    {
      "name": "param19_latest_video2_category",
      "text": param19_latest_video2_category,
      "color": None,
      "background": None
    },
    {
      "name": "param20_lateet_video2_thumbnail",
      "image_url": param20_lateet_video2_thumbnail
    },
    {
      "name": "param21_latest_video2_title",
      "text": param21_latest_video2_title,
      "color": None,
      "background": None
    },
    {
      "name": "param22_latest_video2_view_count",
      "text": param22_latest_video2_view_count,
      "color": None,
      "background": None
    },
    {
      "name": "param23_latest_video2_upload_date",
      "text": param23_latest_video2_upload_date,
      "color": None,
      "background": None
    },
    {
      "name": "param24_latest_video2_like_count",
      "text": param24_latest_video2_like_count,
      "color": None,
      "background": None
    },
    {
      "name": "image_hot_video_badge",
      "image_url": "https://claying.io/hot_video_badge.png"
    },
    {
      "name": "image_view_icon1", 
      "image_url": "https://claying.io/view_icon.png"
    },
    {
      "name": "image_like_icon1",
      "image_url": "https://claying.io/like_icon.png"
    },
    {
      "name": "image_view_icon2",
      "image_url": "https://claying.io/view_icon.png"
    },
    {
      "name": "image_like_icon2",
      "image_url": "https://claying.io/like_icon.png"
    },
    {
      "name": "image_view_icon3",
      "image_url": "https://claying.io/view_icon.png"
    },
    {
      "name": "image_like_icon3",
      "image_url": "https://claying.io/like_icon.png"
    },
    {
      "name": "image_view_icon4",
      "image_url": "https://claying.io/view_icon.png"
    },
    {
      "name": "image_like_icon4",
      "image_url": "https://claying.io/like_icon.png"
    },
    {
      "name": "param25_creator_thumbnail",
      "image_url":param25_creator_thumbnail
    },
    {
      "name": "param26_creator_title",
      "text": param26_creator_title,
      "color": None,
      "background": None
    },
    {
      "name": "small_boundary",
      "color": None
    },
    {
      "name": "small_boundary2",
      "color": None
    }
  ],
  "webhook_url": None,
  "transparent": False,
  "metadata": None
}
    response = requests.post('https://sync.api.bannerbear.com/v2/images',json=payload , headers=headers)
    print(response)
    if response.status_code == 200:
        image_url = response.json()['image_url']
        print("이미지가 생성되었습니다:", image_url)
        return image_url
    else:
        print("오류 발생:", response.status_code, response.text)
        return {"오류 발생 :", response.status_code, response.text}
    
    