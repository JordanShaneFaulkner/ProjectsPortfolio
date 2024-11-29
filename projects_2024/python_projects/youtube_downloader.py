#Jordan Faulkner 5-18-2024
#In this project, I will automate downloading youtube videos into a folder of my choice 

import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def download_video(url,path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True,file_extension='mp4')
        highest_res_steam = streams.get_highest_resolution()
        highest_res_steam.download(output_path=path)
        print('Video Downloaded Successfully!')
        
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f'Selected folder {folder}')
    return folder 

if __name__ == '__main__':
    root = tk.Tk() 
    root.withdraw()
    video_url = input('Enter Youtube url: ')
    path = open_file_dialog()
    if not path:
        print('Please select a folder...')
    else:
        download_video(video_url,path)
    
