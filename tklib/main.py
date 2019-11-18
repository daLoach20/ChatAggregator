import tkinter as tk
from .labels import ChatLine
import twitch_irc

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        twitch_irc.irc.start()
        self.chat_list = []
        self.chat_line = ChatLine(self, name_text="LeadCoder", message="I suck at python")
        self.chat_line.grid(row=0, column=0)
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def loop(self):
        message = twitch_irc.irc.last_message
        if message is not None:
            chat_line = ChatLine(self, name_text=message.get('display_name'), message=message.get('message'))
            chat_line.grid(row=len(self.chat_list), column=0)
            self.chat_list.append(chat_line)
        self.after(5, self.loop())
    
    def on_close(self):
        twitch_irc.irc.quit()
        self.master.destroy()

