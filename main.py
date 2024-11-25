import tkinter as tk
from tkinter import ttk, filedialog
import requests


class Downloader:
    def __init__(self):
        self.savefile = ""
        self.window = tk.Tk()
        self.window.geometry("600x300")
        self.window.title("Downloader")
        self.window.config(bg="sky blue")
        self.label = tk.Label(text="Welcome to Downloader", font='Helvetica 15 bold', bg="sky blue")
        self.label.pack(pady=10)
        self.url_label = tk.Label(text="Enter URL : ", font='Helvetica 10 bold', bg="sky blue")
        self.url_label.pack()
        self.url_entry = tk.Entry(width=35)
        self.url_entry.pack()
        self.browse_button = tk.Button(text="Browse", command=self.browse_file, activebackground="dark slate gray",
                                       bg="DarkSlateGray1", width=15)
        self.browse_button.pack(pady=10)

        self.download_button = tk.Button(text="Download", command=self.download, activebackground="dark slate gray",
                                         bg="DarkSlateGray1", width=15)
        self.download_button.pack(pady=10)

        self.progressBar = ttk.Progressbar(self.window, orient="horizontal", maximum=100, length=350,
                                           mode="determinate")
        self.progressBar.pack(pady=10)
        self.author = tk.Label(text="This downloader is created by needi_developer", bg="sky blue", fg="red")
        self.author.pack(pady=10)
        self.window.mainloop()

    def browse_file(self):
        savefile = filedialog.asksaveasfilename(initialfile=self.url_entry.get().split("/")[-1].split("?")[0])
        self.savefile = savefile

    def download(self):
        url = self.url_entry.get()
        response = requests.get(url, stream=True)
        file_total_size_in_bytes = 100
        if response.headers.get("content-length"):
            file_total_size_in_bytes = int(response.headers.get("content-length"))
        block_size = 10000
        self.progressBar["value"] = 0
        fileName = self.url_entry.get().split("/")[-1].split("?")[0]
        if self.savefile == "":
            self.savefile = fileName
        with open(self.savefile, "wb") as f:
            for data in response.iter_content(block_size):
                self.progressBar["value"] += (100 * block_size) / file_total_size_in_bytes
                self.window.update()
                f.write(data)


Downloader()
