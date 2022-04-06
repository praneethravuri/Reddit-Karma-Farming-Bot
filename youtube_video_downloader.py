from pytube import Playlist, YouTube
import os

YOUTUBE_PLAYLIST = "https://youtube.com/playlist?list=PL1dtuEdDUMi1yver8hPLGK3rIAH8Pnim2"
SAVE_LOCATION = "D:\\Coding Projects\\Reddit Karma Farming Bot\\Videos"
LINK_FILE = "current_video_link.txt"


# Download the YouTube video
def download_video(yt):
    stream = yt.streams.get_by_itag(22)
    stream.download(SAVE_LOCATION)
    print(yt.title + " -> Downloaded!")


scanning = True

while scanning:
    p = Playlist(YOUTUBE_PLAYLIST)

    video_urls = p.video_urls

    if len(video_urls) == 0:
        print("There are no videos in this playlist")
        continue

    last_link = video_urls[-1]

    # if the file is empty, write last_video_link to the file
    if os.stat(LINK_FILE).st_size == 0:
        with open(LINK_FILE, 'w', encoding='utf-8') as f:
            f.write(last_link)
        f.close()
        yt = YouTube(last_link)
        print(f"Downloading {yt.title} \r")
        download_video(yt)

    # if the file is not empty, check if the link in the file is same as the current video link
    else:
        with open(LINK_FILE) as f:
            first_line = f.readline()

        # If no new video is added, continue scanning
        if last_link == first_line:
            pass

        # If a new video is added, erase the LINK_FILE, download the latest video and write the link of the latest video into the LINK_FILE
        else:
            open(LINK_FILE, 'w').close()
            yt = YouTube(last_link)
            print(f"Downloading {yt.title} \r")
            download_video(yt)
            with open(LINK_FILE, 'w', encoding='utf-8') as f:
                f.write(last_link)
            f.close()
