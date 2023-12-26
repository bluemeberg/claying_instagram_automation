# 크리에이터 메인 한줄 소개 생성
# 크리에이터 키 포인트 3개 생성

import openai
import json

recommend_template = """{"1st": "","1st_comments": [{'comment' : "", 'likeCount' : "", "updatedAt" : ""}],"2nd": "","2nd_comments": [{'comment' : "", 'likeCount' : "", "updatedAt" : ""}],"3rd": "","3rd_comments": [{'comment' : "", 'likeCount' : "", "updatedAt" : ""}]}"""
short_template = "''크리에이터는 ''크리에이터로, ''콘텐츠를 선사합니다. 예를들어 최씨네는 일상의 진정성과 유쾌함을 담은 브이로그와 먹방으로 시청자의 마음을 사로잡는 크리에이터로, 맛있는 요리와 따뜻한 가족 분위기로 가득 찬 콘텐츠를 선사합니다."

def make_creator_short_comment(data, channel_title) :
    message = f"인기 콘텐츠들에 대해서 {data}의 시청자 코멘트를 가지고 있는 {channel_title} 크리에이터를 소개하는 한줄 코멘트를 작성해줘"
    system_video_analysis = f"응답을 {short_template} 형태로 제공하세요."
    try :
        completion = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        temperature=0,
        messages=[{"role": "system", "content": system_video_analysis},
                        #   {"rol   e": "user", "content": message1},
                        #   {"role" : "assistant", "content" : message2},
            {"role": "user", "content": message}],
        )
        print("----------")
        print(completion.choices[0].message["content"])
        print("----------")
    except :
        print(f"error")

def make_creator_recommend_comment(data, channel_title) :
    message = f"인기 콘텐츠들에 대해서 {data}의 시청자 코멘트를 가지고 있는 {channel_title} 크리에이터에 대한 매력 포인트 3가지를 시청자 코멘트들 2개 이상으로 맵핑해서 알려줘"
    system_video_analysis = f"응답을 {recommend_template} 형태로 제공하세요."
    try :
        completion = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        temperature=0,
        messages=[{"role": "system", "content": system_video_analysis},
                        #   {"rol   e": "user", "content": message1},
                        #   {"role" : "assistant", "content" : message2},
            {"role": "user", "content": message}],
        )
        print("----------")
        print(completion.choices[0].message["content"])
        data = completion.choices[0].message["content"]
        data_json = json.loads(data)
        print(data_json)
        # 첫 번째 매력 포인트
        first_recommendation = data_json["1st"]
        # 첫 번째 매력 포인트에 대한 상위 인기 댓글 2개
        first_recommendation_comments = data_json["1st_comments"]
        first_recommendation_comments_sorted = sorted(first_recommendation_comments, key=lambda x: x['likeCount'], reverse=True)[:2]
        # 두 번째 매력 포인트
        second_recommendation = data_json["2nd"]
        # 두 번째 매력 포인트에 대한 상위 인기 댓글 2개
        second_recommendation_comments = data_json["2nd_comments"]
        second_recommendation_comments_sorted = sorted(second_recommendation_comments, key=lambda x: x['likeCount'], reverse=True)[:2]
        # 세 번째 매력 포인트
        third_recommendation = data_json["3rd"]
        third_recommendation_comments = data_json["3rd_comments"]
        third_recommendation_comments_sorted = sorted(third_recommendation_comments, key=lambda x: x['likeCount'], reverse=True)[:2]
        print(data_json["1st"])
        print(data_json["1st_comments"])
        print("----------")
    except :
        print(f"error")
    return first_recommendation, first_recommendation_comments_sorted, second_recommendation, second_recommendation_comments_sorted, third_recommendation, third_recommendation_comments_sorted