from pytube import YouTube

url = "https://youtu.be/Y5NTgZA-xWE" # replace the URL with what Vid you want to download
video = YouTube(url)
all_list = []
print(video.title) # .title to print the title of the YT video

print(video.thumbnail_url) # .title to get the thumbnail of the YT video

print("===============================================")
print(all_list)

stream = video.streams.filter(res="1080p")
print(stream)
mp4_highest = YouTube(url).streams.get_highest_resolution().download()