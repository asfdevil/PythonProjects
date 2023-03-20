from pytube import YouTube
a = input("enter link")
url = YouTube(a)
v = url.stream.first()
v.download
print("done")
