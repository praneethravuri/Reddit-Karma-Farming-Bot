from pytube import Playlist, YouTube
import os


class YouTubeVideoDownloader:
    def __init__(self, youtube_playlist, save_location, link_file):
        self.youtube_playlist = youtube_playlist
        self.save_location = save_location
        self.link_file = link_file

    def download_video(self, video_link):
        yt = YouTube(video_link)
        print(f"Downloading -> {yt.title}")

        # getting the highest resolution of the video with the file extension -mp4
        # if a throttling error occurs, change the regex code in the pytube cipher file
        stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

        # downloading the videos in the specified location
        stream.download(self.save_location)
        print(f"Downloaded -> {yt.title}")

    def main(self):

        scanning = True

        while scanning:
            p = Playlist(self.youtube_playlist)
            video_urls = p.video_urls

            if len(video_urls) == 0:
                print("There are no videos in this playlist")
                continue
            elif len(video_urls) != 0:
                with open(self.link_file) as f:
                    first_line = f.readline()

                latest_video_url = video_urls[-1]

                if latest_video_url == first_line:
                    print("There are no 'new' videos in this playlist")

            latest_video_url = video_urls[-1]

            # if the file is empty, write last_video_link to the file
            if os.stat(self.link_file).st_size == 0:
                with open(self.link_file, 'w', encoding='utf-8') as f:
                    f.write(latest_video_url)
                f.close()
                self.download_video(latest_video_url)

            else:

                # If no new video is added, continue scanning
                if latest_video_url == first_line:
                    pass

                # If a new video is added, erase the link_file, download the latest video and write the link of the latest video into the link_file
                else:
                    open(self.link_file, 'w').close()
                    self.download_video(latest_video_url)
                    with open(self.link_file, 'w', encoding='utf-8') as f:
                        f.write(latest_video_url)
                    f.close()


youtube_playlist = "https://youtube.com/playlist?list=PL1dtuEdDUMi3Ie4iqksc0SxnMl7XYk3zR"
save_location = "D:\\Coding Projects\\YouTube-Playlist-Video-Downloader\\Videos"
link_file = "current_video_link.txt"
if __name__ == "__main__":
    youtube_video_downloader = YouTubeVideoDownloader(youtube_playlist, save_location, link_file)
    youtube_video_downloader.main()
