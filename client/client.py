import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

class ClientGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Multithreaded Client with Nickname")
        self.master.geometry('400x300')

        # Chat display
        self.chat_display = scrolledtext.ScrolledText(master, wrap=tk.WORD, state='disabled')
        self.chat_display.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

        # Message entry
        self.message_entry = tk.Entry(master, width=40)
        self.message_entry.grid(column=0, row=1, padx=10, pady=10)
        self.message_entry.bind('<Return>', self.send_message)

        # Send button
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(column=1, row=1)

        # Initialize client connection
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '127.0.0.1'
        self.port = 12345
        self.nickname = None  # Nickname will be stored here
        self.connect_to_server()

        # Ask for nickname
        self.prompt_for_nickname()

        # Start receiving messages in a separate thread
        self.running = True
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def prompt_for_nickname(self):
        self.nickname = simpledialog.askstring("Nickname", "Please enter your nickname:", parent=self.master)
        if self.nickname:
            self.update_chat_display(f"You are now known as {self.nickname}\n")
        else:
            self.nickname = "Anonymous"  # Default nickname if user skips

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.host, self.port))
        except Exception as e:
            print(f"Unable to connect to server: {e}")
            self.master.quit()

    def send_message(self, event=None):
        message = self.message_entry.get()
        self.message_entry.delete(0, tk.END)
        formatted_message = f"{self.nickname}: {message}"
        self.client_socket.send(formatted_message.encode('utf-8'))
        self.update_chat_display(formatted_message + "\n")  # Display the message on the GUI

    def receive_messages(self):
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.update_chat_display(message + "\n")
            except:
                print("An error occurred!")
                self.client_socket.close()
                break

    def update_chat_display(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message)
        self.chat_display.yview(tk.END)
        self.chat_display.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    client_gui = ClientGUI(root)
    root.mainloop()
