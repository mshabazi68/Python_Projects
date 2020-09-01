from tkinter.messagebox import *
from threading import *
from tkinter.filedialog import *
from tkinter import *
from pytube import YouTube



url = input ("Enter the Link: ")
yt = YouTube(url)


## Youtube information
print("Title:" , yt.title)

print("View counts: " , yt.views)
print("Length of clip: ", yt.length , "seconds")
print("Description:" , yt.description)
print("Ratings: ", yt.rating)
ys = yt.streams.get_highest_resolution()
print("Downloading...")
ys.download("./Users/Shah/Desktop")
print("Download completed!!")