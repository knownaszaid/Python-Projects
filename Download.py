from pytube import YouTube
link =input("Enter Link Here")
youtube_1 = YouTube(link)


videos = youtube_1.streams.all()
vid =list(enumerate(videos))
for i in vid:
    print(i)

print()
strm = int(input("enter: "))
videos[strm].download()
print('successfully')
