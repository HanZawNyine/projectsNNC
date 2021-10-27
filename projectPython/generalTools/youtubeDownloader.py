from pytube import Playlist
from pytube import Channel
from pytube import YouTube

#download Channel
# url = 'https://www.youtube.com/channel/UCvVZ19DRSLIC2-RUOeWx8ug'
# c = Channel(url)
# print(c.video_urls)


def playlistDownload(url):
    p = Playlist(url)
    #print(p.video_urls)
    for a in p.video_urls:
        print(a)
        youtubeDownload(url)

def youtubeDownload(url):
    myVideo = YouTube(url)
    fileSizeInBytes = myVideo.streams.filter(progressive="True").get_highest_resolution()
    print(myVideo.title)

    MaxFileSize = fileSizeInBytes.filesize / 1024000
    MB = str(MaxFileSize) + " MB"
    print("File Size : {:00.00f} MB".format(MaxFileSize))

    fileSizeInBytes.download()
    print(myVideo.title+"...Completed")

youtubeDownload("https://www.youtube.com/watch?v=TJ8dqvpus-Q")