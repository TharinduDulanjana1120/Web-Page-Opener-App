import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser

class WebpageOpenerApp:
    def __init__(self, master):
        self.master = master
        master.title("Tharindus' AI Opener")

        style = ttk.Style()
        style.theme_use("clam")  # You can try other themes like "aquativo", "arc", etc.

        self.frame = ttk.Frame(master, padding="80")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.label = ttk.Label(self.frame, text="Open AI Shortcuts:", font=("Helvetica", 14))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.buttons = []

        urls = [
            'https://chat.openai.com/',
            'https://www.perplexity.ai/',
            'https://poe.com/',
            'https://labs.google/',
            'https://notebooklm.google.com/'
        ]

        button_names = [
            'Chat GPT',
            'Perplexity',
            'Poe',
            'Google Labs',
            'NotebookLM'
        ]

        for i, (url, name) in enumerate(zip(urls, button_names)):
            button = ttk.Button(self.frame, text=name, command=lambda u=url: self.open_single_webpage(u))
            button.grid(row=i+1, column=0, pady=10)
            self.buttons.append(button)

        self.open_all_button = ttk.Button(self.frame, text="Open All AIs", command=self.open_all_webpages)
        self.open_all_button.grid(row=len(urls) + 1, column=0, pady=20)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(len(urls) + 1, weight=1)

    def open_single_webpage(self, url):
        try:
            webbrowser.open_new_tab(url)
            messagebox.showinfo("Success", f"Webpage {url} opened successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def open_all_webpages(self):
        urls = [
            'https://chat.openai.com/',
            'https://www.perplexity.ai/',
            'https://poe.com/',
            'https://labs.google/',
            'https://notebooklm.google.com/'
        ]
        try:
            for url in urls:
                webbrowser.open_new_tab(url)
            messagebox.showinfo("Success", "All webpages opened successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def run_app():
    root = tk.Tk()
    app = WebpageOpenerApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
