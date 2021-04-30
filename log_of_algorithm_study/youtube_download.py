import youtube_dl


ydl_opt = {
    # 'listformats': True
    'format': '299'

    }
with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=OexnAyRQnOs&t=1994s'])