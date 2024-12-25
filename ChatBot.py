import re


def chatbot():
    print("Hello! I am a Zook chatbot. Type 'exit' to end the conversation.")

    while True:
        # Get user input
        user_input = input("You: ").lower()

        # Check for exit condition
        if user_input == 'exit':
            print("Goodbye! Have a great day!")
            break

        # Rule-based responses using simple if-else statements
        elif re.search(r'\b(hi|hello|hey)\b', user_input):
            print("Chatbot: Hello! How can I assist you today?")

        elif re.search(r'\b(bye|goodbye)\b', user_input):
            print("Chatbot: Goodbye! Take care!")

        elif re.search(r'\b(how are you|how are you doing)\b', user_input):
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")

        elif re.search(r'\b(name|who are you)\b', user_input):
            print("Chatbot: I am a zook chatbot created to help you.")

        elif re.search(r'\b(weather)\b', user_input):
            print("Chatbot: I can't check the weather right now, but you can check it on your preferred weather app.")

        elif re.search(r'\b(help|assist)\b', user_input):
            print(
                "Chatbot: Sure! I can help you with some basic questions. You can ask me about my name, weather, or just say hi.")

        else:
            print("Chatbot: I'm sorry, I didn't quite understand that. Could you please rephrase?")


# Run the chatbot
chatbot()
