from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "Voce é um categarizador de produtos."
    },
    {
      "role": "user",
      "content": "escova de dentes"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  n=5
)

for i in range(5):
    print(response.choices[i].message.content)
    print("\n------------------------\n")