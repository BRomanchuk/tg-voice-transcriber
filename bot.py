from utils.config import Configuration
from utils.telegram_worker import TelegramWorker

from aiogram import Bot, Dispatcher, types


bot = Bot(token=Configuration.telegram_bot_token)
dp = Dispatcher(bot)

TelegramWorker.bot = bot


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def voice_handler(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action=types.ChatActions.TYPING)
    media = await bot.get_file(message.voice.file_id)
    await TelegramWorker.voice(message, media)


@dp.message_handler(content_types=[types.ContentType.VIDEO])
async def video_handler(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action=types.ChatActions.TYPING)
    media = await bot.get_file(message.video.file_id)
    await TelegramWorker.video(message, media)


@dp.message_handler(content_types=[types.ContentType.VIDEO_NOTE])
async def video_note_handler(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action=types.ChatActions.TYPING)
    media = await bot.get_file(message.video_note.file_id)
    await TelegramWorker.video(message, media)

