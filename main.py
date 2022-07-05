# Imports for clipboard, youtube dl, tkinter for saveas dialog
import pyperclip
import yt_dlp
from tkinter import Tk 
from tkinter.filedialog import asksaveasfilename
import os, sys, subprocess

# Get current clipboard contents and shove it into url variable
URL = pyperclip.paste()

# Get the preferred file extension
with yt_dlp.YoutubeDL() as ydl:
    info = ydl.extract_info(URL, download=False)
    file_extension = '.' + info['ext']

# Lets make an invisible tkinter window so we can choose where to save the file, then destroy it
root = Tk()
root.withdraw()
filename = (asksaveasfilename(filetypes=[( file_extension + " File", file_extension)],defaultextension=file_extension))
root.destroy()

# Our options, use the name we decided on in the dialog
ydl_opts = {
    'outtmpl': filename,
}

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

# Download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])

open_file(filename)
