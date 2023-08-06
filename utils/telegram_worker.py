from .openai_worker import AIWorker
from .media_worker import MediaWorker


class TelegramWorker:
    bot = None

    @staticmethod
    async def start(message):
        return await message.reply("send your voice, video, or video note and I will transcribe it")

    @staticmethod
    async def voice(message, media):
        media = MediaWorker.get_media_bytes(
            media_path=media.file_path,
            bot_token=TelegramWorker.bot._token
        )
        media = MediaWorker.ogg_to_wav(media)
        media.name = 'audio.wav'
        transcript = await AIWorker.whisper(media)
        await message.reply(transcript)

    @staticmethod
    async def video(message, media):
        media = MediaWorker.get_media_bytes(
            media_path=media.file_path,
            bot_token=TelegramWorker.bot._token
        )
        media.name = 'video.mp4'
        transcript = await AIWorker.whisper(media)
        await message.reply(transcript)

