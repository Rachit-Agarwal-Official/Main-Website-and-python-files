responses = {
    "hi": "Hello!",
    "how are you": "I'm good, thanks for asking.",
    "what is your name": "My name is Chatbot.",
    "bye": "Goodbye!"
}

def get_response(user_input):
    if user_input not in responses:
        print("Sorry I can't get it")
    elif user_input in responses:
        return responses[user_input]

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        break
    response = get_response(user_input)
    print("Chatbot:", response)