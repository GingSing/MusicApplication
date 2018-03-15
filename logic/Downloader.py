import youtube_dl


class Downloader:

    def __init__(self):
        self.data = []

    def download(self, input, ext):
        if ext == 'mp3':
            ydl_opts = {
                'outtmpl': 'C://Users/Garwhy/Desktop/Music/%(title)s.%(ext)s',
                'audioformat': 'mp3',
                'extractaudio': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        elif ext == 'mp4':
            ydl_opts = {}

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([input])
