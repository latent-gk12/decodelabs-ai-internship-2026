from chatbot import get_response

print("=" * 50)
print("      DecodeLabs Rule-Based AI Chatbot")
print("=" * 50)

while True:

    user = input("\nYou : ")

    reply = get_response(user)

    if reply is None:
        print("Bot : Goodbye!")
        break

    print("Bot :", reply)