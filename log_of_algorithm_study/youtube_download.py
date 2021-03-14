import youtube_dl


ydl_opt = {
    'listformats': True

    }
with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=wJWksPWDKOc'])