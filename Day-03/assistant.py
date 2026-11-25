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

roles = {
    "1": "You are a friendly teacher. Explain every concept in simple language with the real-life examples.",
    "2": "You are a senior python developer. Explain every concept in simple language including python examples.",
    "3": "You are an experienced travel guide. Recommend places,food, transportation and travel tips.",
    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",
    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer.",
    }

print("\nChoose Your Assistant\n")

print("1. Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")

choice = input("\nEnter your choice:")

messages = [
    {
        "role": "system",
        "content": roles.get(
            choice,
            "You are a helpful AI assistant."
        )
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


