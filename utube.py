from pytube import Playlist
from pytube import YouTube

#want = [] #list of links of playlists that u wish to download

pl = Playlist(want[0])
number = 10 #number of videos in that playlist
i = 1
all = len(pl)

for url in pl:
    print (i,"/",all)
    if (i >= number):
        print ("fetching video", i)
        video = YouTube(url)
        print ("downloading video", i)
        print (video.title)
        video.streams.get_highest_resolution().download()
        print ("finished video", i)
    
    i += 1
    
print("finished")


# pl.download_all()
