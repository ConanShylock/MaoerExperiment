# -*- coding: utf-8 -*-
import os
import openai
# import nltk
# from nltk.tokenize import word_tokenize
# import nltk


# 输入文件
file = '../content_feature_GPT/'
file_path = file + "content_feature_GPT_finetune_prompt.json"


# 直接输出
# openai.api_base = "https://openkey.cloud/v1" # 换成代理，一定要加v1
# openai.api_key = "sk-WO7BUmh8G7C4lJUFCc71Fb9cC5124e4fBdE76dAb164bEfDc"
#
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system",
#          "content": "你是一个能分辨文本内容类型的助手。"},
#         {"role": "user",
#          "content": "下面将输入一段文本，这是来源于一些长或短的故事简介。根据输入的文本内容，判断这段文本所指的故事可能所属的性向分类、时代分类、故事类型及标签。具体的性向分类有：言情,纯爱,无CP；时代分类有：近代现代,古色古香,架空历史,幻想未来；故事类型有：爱情,武侠,奇幻,仙侠,游戏,传奇,科幻,童话,惊悚,悬疑,剧情,轻小说,古典衍生,东方衍生,西方衍生,其他衍生,儿歌,散文,寓言,童谣；标签有：甜文,爽文,情有独钟,穿越时空,穿书,强强,天作之合,系统,豪门世家,天之骄子,娱乐圈,成长,重生,都市,宫廷侯爵,种田文,快穿,年代文,无限流,升级流,业界精英,直播,仙侠修真,幻想空间,灵异神怪,破镜重圆,先婚后爱,综漫,万人迷,星际,打脸,女强,励志,基建,逆袭,异能,校园,赛博朋克,日常,游戏网游,惊悚,电竞,团宠,追爱火葬场,美食,末世,ABO,群像,悬疑推理,复仇虐渣,现代架空,美强惨,生子,灵气复苏,暗恋,萌宠,群像,废土,青梅竹马,玄学,相爱相杀,清穿,马甲文,正剧,综艺,机甲,虫族,朝堂,科举,宫斗。根据上述四种分类的取值范围，判断文本所属的这四种分类结果。要求：每种分类都必须有答案输出,请勿给出取值范围外的结果；前三种是单选，第四种是多选且至少三个。请给出明确的四种分类结果，以以下形式作为输出：\"这段文本所属分类结果如下：【性向= xx；时代= nn；类型= yy；标签=mm、kk、zz】\" 。以下为输入文本：十三岁那年，桑稚偷偷喜欢上一个男人。\n男人的模样冷淡慵懒，说起话来吊儿郎当的，经常来她家，一个下午窝在她哥哥房间里打游戏。\n偶尔见她进来送水果零食，也只是漫不经心地掀起眼皮，笑得像个妖孽：“小孩，你怎么回事啊？一见到哥哥就脸红。”\n\n*妖孽腹黑x乖张少女\n微博@小竹已"
#          }]
# )
# print(response['choices'][0]['message']['content'])

# 使用 HTTP requests 请求调用 ChatGPT
import requests

# url = "https://api.openai.com/v1/chat/completions"
url = "https://openkey.cloud/v1/chat/completions"

headers = {
  'Content-Type': 'application/json',
  # 填写OpenKEY生成的令牌/KEY，注意前面的 Bearer 要保留，并且和 KEY 中间有一个空格。
  'Authorization': 'Bearer sk-WO7BUmh8G7C4lJUFCc71Fb9cC5124e4fBdE76dAb164bEfDc'
}

data = {
  "model": "gpt-3.5-turbo",
  "messages": [
            {
                "role": "system",
                "content": "你是一个能分辨文本内容类型的助手。"
            },
            {
                "role": "user",
                "content": "请先学习以下任务，学习完后只需回复已完成学习,等待后续的任务即可。下面将输入一段文本，这是来源于一些长或短的故事简介。根据输入的文本内容，判断这段文本所指的故事可能所属的性向分类、时代分类、故事类型及标签。具体的性向分类有：言情,纯爱,无CP；时代分类有：近代现代,古色古香,架空历史,幻想未来；故事类型有：爱情,武侠,奇幻,仙侠,游戏,传奇,科幻,童话,惊悚,悬疑,剧情,轻小说,古典衍生,东方衍生,西方衍生,其他衍生,儿歌,散文,寓言,童谣；标签有：甜文,爽文,情有独钟,穿越时空,穿书,强强,天作之合,系统,豪门世家,天之骄子,娱乐圈,成长,重生,都市,宫廷侯爵,种田文,快穿,年代文,无限流,升级流,业界精英,直播,仙侠修真,幻想空间,灵异神怪,破镜重圆,先婚后爱,综漫,万人迷,星际,打脸,女强,励志,基建,逆袭,异能,校园,赛博朋克,日常,游戏网游,惊悚,电竞,团宠,追爱火葬场,美食,末世,ABO,群像,悬疑推理,复仇虐渣,现代架空,美强惨,生子,灵气复苏,暗恋,萌宠,群像,废土,青梅竹马,玄学,相爱相杀,清穿,马甲文,正剧,综艺,机甲,虫族,朝堂,科举,宫斗。根据上述四种分类的取值范围，判断文本所属的这四种分类结果。要求：每种分类都必须有答案输出,请勿给出取值范围外的结果；前三种是单选，第四种是多选且至少三个。请给出明确的四种分类结果，以以下json形式作为输出，要求包含标题、性向、时代、类型、标签,以下为输入文本的标题：偷偷藏不住,输入文本为：十三岁那年，桑稚偷偷喜欢上一个男人。\n男人的模样冷淡慵懒，说起话来吊儿郎当的，经常来她家，一个下午窝在她哥哥房间里打游戏。\n偶尔见她进来送水果零食，也只是漫不经心地掀起眼皮，笑得像个妖孽：“小孩，你怎么回事啊？一见到哥哥就脸红。”\n\n*妖孽腹黑x乖张少女\n微博@小竹已。输出结果为：result = {\"标题\": \"偷偷藏不住\",\"性向\": \"言情\",\"时代\": \"近代现代\",\"类型\": \"爱情\",\"标签\": \"['情有独钟', '励志', '甜文', '轻松']\"}"
            }
        ]
}

response = requests.post(url, headers=headers, json=data)
json_data = response.json()

print("Status Code", response.status_code)
print("JSON Response ", json_data)
# 访问解析后的 JSON 数据
print(type(json_data))  # 输出数据类型，可能是字典或列表
print(json_data[0])  # 输出列表中的第一个元素
print(json_data['result'])  # 输出字典中的指定键对应的值
