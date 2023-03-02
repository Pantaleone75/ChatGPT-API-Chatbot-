import openai
import tkinter as tk
from tkinter import scrolledtext

# Set up the OpenAI API key
openai.api_key = "KEY"

# Define the messages list
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

# Define the function for sending messages
def send_message():
    # Get the user's input message from the entry box
    user_input = user_input_box.get()
    if user_input:
        # Append the user's message to the messages list
        messages.append({"role": "user", "content": user_input})
        # Set the prompt for the OpenAI chatbot
        prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
        # Get the chatbot's response
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages,
        )
        reply = chat.choices[0].message.content
        # Append the chatbot's response to the messages list
        messages.append({"role": "assistant", "content": reply})
        # Clear the user's input box
        user_input_box.delete(0, tk.END)
        # Append the user's input and the chatbot's response to the scrolled text widget
        chat_history.insert(tk.END, f"User: {user_input}\n", "user")
        chat_history.insert(tk.END, f"Chatbot: {reply}\n", "chatbot")
        chat_history.see(tk.END)

# Create the main window
window = tk.Tk()
window.title("Chatbot")

# Create the scrolled text widget for displaying the chat history
chat_history = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=20, font=("Helvetica", 12))
chat_history.tag_configure("user", justify="right")
chat_history.tag_configure("chatbot", justify="left")
chat_history.pack()

# Create the entry box for the user's input
user_input_box = tk.Entry(window, width=60, font=("Helvetica", 12))
user_input_box.pack()

# Create the button for sending the user's input
send_button = tk.Button(window, text="Send", font=("Helvetica", 12), command=send_message)
send_button.pack()

# Start the main event loop
window.mainloop()
