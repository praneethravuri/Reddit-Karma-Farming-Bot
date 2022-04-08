from pytube import Playlist, YouTube
import os

YOUTUBE_PLAYLIST = "https://youtube.com/playlist?list=PL1dtuEdDUMi1yver8hPLGK3rIAH8Pnim2"
SAVE_LOCATION = "D:\\Coding Projects\\YouTube-Playlist-Video-Downloader\\Videos"
LINK_FILE = "current_video_link.txt"


def download_video(video_link):

    yt = YouTube(video_link)
    print(f"Downloading {yt.title}")

    # getting the highest resolution of the video with the file extension -mp4
    stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

    # downloading the videos in the specified location
    stream.download(SAVE_LOCATION)
    print(f"Downloaded {yt.title}")


def main():
    scanning = True

    while scanning:
        p = Playlist(YOUTUBE_PLAYLIST)
        video_urls = p.video_urls

        if len(video_urls) == 0:
            print("There are no videos in this playlist")
            continue

        latest_video_url = video_urls[-1]

        # if the file is empty, write last_video_link to the file
        if os.stat(LINK_FILE).st_size == 0:
            with open(LINK_FILE, 'w', encoding='utf-8') as f:
                f.write(latest_video_url)
            f.close()
            download_video(latest_video_url)

        else:
            with open(LINK_FILE) as f:
                first_line = f.readline()

            # If no new video is added, continue scanning
            if latest_video_url == first_line:
                pass

            # If a new video is added, erase the LINK_FILE, download the latest video and write the link of the latest video into the LINK_FILE
            else:
                open(LINK_FILE, 'w').close()
                download_video(latest_video_url)
                with open(LINK_FILE, 'w', encoding='utf-8') as f:
                    f.write(latest_video_url)
                f.close()


if __name__ == "__main__":
    main()
