import openai
import json
openai.organization = "org-g1clsGKfmkgQ4GfKhAn8TVAE"
openai.api_key = "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"

# 영상 카테고리 분석
def classify_video_category(title, tags) :
    with open('youtube_detail_category_v3.json', 'r') as file:
        data = json.load(file)
    # print(data)
    # 모든 값들을 하나의 리스트에 추가
    values_list = []
    for key, values in data.items():
        values_list.extend(values)
    result_string = ', '.join(values_list)
    # print(result_string)
    system_video_analysis = "유투브 영상의 제목과 태그들이 주어지며 귀하의 임무는 영상의 카테고리를 분류하여 답변을 {}기호 사이에 넣어서 제공하세요. 예를들면 {Car} 이런 형식입니다. 여기에 제공된 카테고리 목록에서만 선택하십시오(단 하나의 카테고리만 선택하십시오):" + result_string
    message = f"영상 제목 : {title}, 영상 태그 : {tags}"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,        
        messages=[{"role": "system", "content": system_video_analysis},
                {"role": "user", "content": message}],
        )
    # print("----------")
    # print(completion.choices[0].message["content"])
    # print("----------")
    return completion.choices[0].message["content"]