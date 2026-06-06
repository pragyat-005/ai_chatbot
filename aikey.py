

import openai
from openai import OpenAI

# A.I module using deepseek-chat api instead deepseek-R1 free

client = OpenAI(api_key="your api key",
                base_url="https://openrouter.ai/api/v1")

chat = client.chat.completions.create(
    model="deepseek/deepseek-chat",
    messages=[
        {
            "role": "user",
            "content": f"2+2"
        }
    ]
)

print(chat.choices[0].message.content)  # only response is printed



