# Imports for clipboard, youtube dl, tkinter for saveas dialog
import pyperclip
import yt_dlp
from tkinter import * 
from tkinter.filedialog import asksaveasfilename

# Get current clipboard contents and shove it into url variable
url = pyperclip.paste()

# Lets make an invisible tkinter window so we can choose where to save the file, then destroy it
root = Tk()
root.withdraw()
filename = (asksaveasfilename())
root.destroy()

# Our options, use the name we decided on in the dialog
ydl_opts = {
    'outtmpl': filename
}

# Download time
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])