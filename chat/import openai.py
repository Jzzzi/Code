# 导入OpenAI的Python SDK。
import openai

# 设置OpenAI API的密钥，该密钥必须在OpenAI的网站上注册并获取。
openai.api_key = "sk-bUQeskc00tsTp************5i5Dop8BxAL1n7"

# 指定使用的语言模型。此处选择GPT-3.5 Turbo模型。
response = openai.ChatCompletion.create(
    # 指定使用的语言模型。此处选择GPT-3.5 Turbo模型。
    model="gpt-3.5-turbo",
    # 以列表形式提供对话中的每个消息。
    messages=[
        # 第一条消息，表示系统向用户打招呼。
        {"role": "system", "content": "Hello!"},
        # 第二条消息，表示用户提出了一个问题。
        {"role": "user","content": "请告诉我你的脑容量有多大？"},
    ]
)

# 创建一个名为“result”的空字符串变量，用于存储机器生成的回答。
result = ''
# 循环遍历GPT-3 API返回的response中的所有回答选项。
for choice in response.choices:
    # 将每个回答选项的文本内容加入到“result”字符串变量中。
    result += choice.message.content
# 打印机器生成的回答。
print(result)
