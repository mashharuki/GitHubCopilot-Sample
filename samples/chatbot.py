import tkinter as tk
from tkinter import messagebox, Scrollbar, END

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("400x500")  # Set the size of the window
        self.root.resizable(width=False, height=False)  # Make the window not resizable

        self.chat_window = tk.Text(root, bd=1, bg="black", width="50", height="8", font=("Arial", 23), foreground="#00ffff")
        self.chat_window.place(x=6, y=6, height=385, width=370)

        self.scrollbar = Scrollbar(root, command=self.chat_window.yview, cursor="star")
        self.scrollbar.place(x=375, y=5, height=385)

        self.entry = tk.Entry(root, bd=1, bg="black", width="30", font=("Arial", 23), foreground="#00ffff")
        self.entry.place(x=128, y=400, height=88, width=260)

        self.send_button = tk.Button(root, text="Send", width="12", height=5, bd=0, bg="#0080ff", activebackground="#00bfff", foreground='#ffffff', font=("Arial", 12), command=self.respond)
        self.send_button.place(x=6, y=400, height=88)

        self.responses = {
            "hello": "Hello, how can I help you?",
            "bye": "Goodbye!"
        }

    def respond(self):
        message = self.entry.get()
        self.chat_window.insert(END, "You: " + message + '\n\n')
        self.entry.delete(0, END)
        response = self.responses.get(message.lower(), "I don't understand.")
        self.chat_window.insert(END, "Bot: " + response + '\n\n')

root = tk.Tk()
chat_bot = ChatBot(root)
root.mainloop()