from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration
load_dotenv()

# Create AI client
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("=" * 40)
print("      My AI Assistant")
print("=" * 40)

messages = [
    {
        "role": "system",
        "content": "You're a friendly AI Teacher. Explain every concept in simple language with the real-life examples."
    }
]

while True:

    user_input = input("\nYou : ")

    messages.append({
        "role": "user",
        "content": user_input
    })

    if user_input.lower() == "quit":
        print("\nAI  : Goodbye! Have a great day.")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages= messages
    )

    ai_reply = response.choices[0].message.content

    print("\nAI :", ai_reply)

    # Save the AI's Reply
    messages.append({
            "role": "assistant",
            "content": ai_reply
        })

    # print("\n----------------Conversation Memory -----------------------------------")
    # for message in messages:
    #     print(message)
    # print("-------------------------------------------------------------------------")

    
    # print("\n===================== Conversation Memory =============================")
    # for message in messages:
    #     print(f"{message['role'].title()}: {message['content']}")
    # print("==========================================================================")


