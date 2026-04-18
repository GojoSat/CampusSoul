from openai import OpenAI

# 1. 用你的密钥初始化客户端
client = OpenAI(
    api_key="你的API密钥", # 这里换成你自己的Key
    base_url="https://api.deepseek.com" # DeepSeek的官方地址
)

# 2. 定义一个NPC，这里以一个“有些社恐的同桌”为例
npc_name = "内向的同桌 - 小雯"
system_prompt = f"""
你是{npc_name}，一个有些社恐、但内心善良的高中女生。你很少主动说话，但有人找你时，你会小声回应。
你说话时有些紧张，常常会脸红。记住，你是在和你的同桌说话。
"""

# 3. 开始对话！
while True:
    # 获取玩家输入
    user_input = input("你: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("对话结束，下次再聊吧。")
        break

    # 调用API，让AI生成回复
    response = client.chat.completions.create(
        model="deepseek-chat", # 选用通用对话模型
        messages=[
            {"role": "system", "content": system_prompt}, # NPC的“内心设定”
            {"role": "user", "content": user_input}       # 玩家说的内容
        ],
        temperature=0.8, # 控制回复的随机性（0-1），数字越大越“跳脱”
        max_tokens=200    # 限制每次回复的最大长度
    )

    # 打印NPC的回复
    npc_reply = response.choices[0].message.content
    print(f"{npc_name}: {npc_reply}")