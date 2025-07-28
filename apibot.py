from openai import OpenAI

client= OpenAI(
    api_key="Enter you groq key",
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input= input("you: ")
    if user_input == "quit":
        print("bot: Goodbye!")
        break
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "you are a trending tech news expert, Response only with latest AI news and opinion"},
            {"role": "user", "content": user_input} 
        ]
    )
    print("Bot:, ", response.choices[0].message.content)