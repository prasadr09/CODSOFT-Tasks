import re
import requests
import tkinter as tk
from tkinter import ttk, messagebox

# Define the weather API (Replace `your_api_key` with your actual OpenWeatherMap API key)
API_KEY = "your_api_key"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(WEATHER_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            return f"Sorry, I couldn't find weather information for '{city}'."

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]

        return f"The weather in {city} is {weather} with a temperature of {temp}°C, feeling like {feels_like}°C."
    except Exception as e:
        return "I'm sorry, I couldn't fetch the weather data right now. Please try again later."


def chatbot_response(user_input):
    user_input = user_input.lower()

    # Check for exit condition
    if user_input == 'exit':
        return "Goodbye! Have a great day!"

    # Rule-based responses
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I assist you today?"

    elif re.search(r'\b(bye|goodbye)\b', user_input):
        return "Goodbye! Take care!"

    elif re.search(r'\b(how are you|how are you doing)\b', user_input):
        return "I'm just a bot, but I'm doing great! How about you?"

    elif re.search(r'\b(name|who are you)\b', user_input):
        return "I am Zook, your friendly chatbot."

    elif re.search(r'\b(weather in ([a-zA-Z\s]+))\b', user_input):
        match = re.search(r'weather in ([a-zA-Z\s]+)', user_input)
        city = match.group(1).strip()
        return get_weather(city)

    elif re.search(r'\b(help|assist)\b', user_input):
        return "Sure! You can ask me about my name, the weather in your city, or just have a friendly chat."

    elif re.search(r'\b(joke|funny)\b', user_input):
        return "Why don’t scientists trust atoms? Because they make up everything!"

    elif re.search(r'\b(hobby|do for fun)\b', user_input):
        return "I love chatting with you and learning new things!"

    elif re.search(r'\b(fact|tell me something interesting)\b', user_input):
        return "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!"

    else:
        return "I'm sorry, I didn't quite understand that. Could you please rephrase?"


def send_message():
    user_message = user_input.get()
    if user_message.strip() == "":
        return

    chat_window.insert(tk.END, "You: " + user_message + "\n", "user")
    user_input.delete(0, tk.END)

    # Get chatbot response
    response = chatbot_response(user_message)
    chat_window.insert(tk.END, "Chatbot: " + response + "\n", "bot")

    # Exit application if the user types 'exit'
    if user_message.lower() == "exit":
        root.destroy()


def clear_chat():
    """Clears the chat window."""
    chat_window.delete(1.0, tk.END)
    chat_window.insert(tk.END, "Chatbot: Hello! I am Zook chatbot. Type 'exit' to end the conversation.\n", "bot")


def toggle_theme():
    """Toggles between light and dark mode."""
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        root.style.theme_use("clam")
        chat_window.config(bg="#222831", fg="#EEEEEE")
        user_input.config(bg="#393E46", fg="#EEEEEE")
        theme_button.config(text="Switch to Light Mode")
    else:
        root.style.theme_use("alt")
        chat_window.config(bg="#FFFFFF", fg="#000000")
        user_input.config(bg="#F0F0F0", fg="#000000")
        theme_button.config(text="Switch to Dark Mode")


# Create the main application window
root = tk.Tk()
root.title("Zook Chatbot")
root.geometry("500x600")

# Add ttk style
root.style = ttk.Style()
root.style.theme_use("clam")

# Create a frame for the chat window
chat_frame = ttk.Frame(root, padding=10)
chat_frame.pack(fill=tk.BOTH, expand=True)

# Create a text area for displaying the chat
chat_window = tk.Text(chat_frame, wrap=tk.WORD, height=20, bg="#222831", fg="#EEEEEE", font=("Arial", 12))
chat_window.pack(fill=tk.BOTH, expand=True)
chat_window.insert(tk.END, "Chatbot: Hello! I am Zook chatbot. Type 'exit' to end the conversation.\n", "bot")

# Define custom tags for styling
chat_window.tag_config("user", foreground="#00ADB5")
chat_window.tag_config("bot", foreground="#EEEEEE")

# Create a frame for user input
input_frame = ttk.Frame(root, padding=10)
input_frame.pack(fill=tk.X, side=tk.BOTTOM)

# Create an entry box for user input
user_input = ttk.Entry(input_frame, font=("Arial", 14))
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

# Create a send button
send_button = ttk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

# Create a clear chat button
clear_button = ttk.Button(root, text="Clear Chat", command=clear_chat)
clear_button.pack(pady=5)

# Create a theme toggle button
dark_mode = True
theme_button = ttk.Button(root, text="Switch to Light Mode", command=toggle_theme)
theme_button.pack()

# Start the Tkinter event loop
root.mainloop()
