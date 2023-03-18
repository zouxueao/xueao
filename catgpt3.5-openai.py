import os
import openai
openai.api_key = "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"


conversation=[{"role": "system", "content": "You are a helpful assistant."}]

while True:
    prompt = (input("请输入您的内容："))
    conversation.append({"role": "user","content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = conversation,
        temperature=1,
        max_tokens=1024,
        top_p=0.9
    )
    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    print("\n" + response['choices'][0]['message']['content'] + "\n")


