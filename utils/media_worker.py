from io import BytesIO
from pydub import AudioSegment

import requests


class MediaWorker:
    @staticmethod
    def ogg_to_wav(media):
        media = AudioSegment.from_file(media, format="ogg").export(format="wav")
        media = BytesIO(media.read())
        return media

    @staticmethod
    def get_media_bytes(media_path, bot_token):
        url = f"https://api.telegram.org/file/bot{bot_token}/{media_path}"
        media = requests.get(url)
        media = BytesIO(media.content)
        return media
