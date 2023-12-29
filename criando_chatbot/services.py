from openai import OpenAI

client = OpenAI()

def get_chat_completion(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= [
            {
                "role": "user",
                "content": text
            }
        ],
        stream=True
    )

    return response.choices[0].message.content
