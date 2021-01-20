from __future__ import unicode_literals
import youtube_dl
import os

class Download(object):
    def __init__(self, url, opt='video'):
        self.url = url
        self.opt = opt
        self.save_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        self.song()

    def song(self):
        if self.opt == 'video':
            opts = {'outtmpl': self.save_path + '/%(title)s.%(ext)s'}
        else:
            opts = {
                'verbose': True,
                'fixup': 'detect_or_warn',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '1411',
                }],
                'extractaudio' : True,
                'outtmpl': self.save_path + '/%(title)s.%(ext)s',
                'noplaylist' : True
            }
        ydl = youtube_dl.YoutubeDL(opts)
        ydl.download([self.url])