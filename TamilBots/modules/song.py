from pyrogram import Client, filters
from bot import bot, max_file


from pyrogram import filters, types
import asyncio
import os
from pytube import YouTube
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from youtubesearchpython import VideosSearch
from TamilBots.TamilBots import ignore_blacklisted_users, get_arg
from TamilBots import app, LOGGER
from TamilBots.sql.chat_sql import add_chat_to_db

def yt_search(song):
    videosSearch = VideosSearch(song, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url


@app.on_message(filters.audio | filters.video | filters.voice)
async def voice_handler(_, message):
    file_size = message.audio or message.video or message.voice
    if max_file < file_size.file_size :
        await message.reply_text(
            "**⚠️ Max file size has been reached.**"
        )
        return
    file = await message.download(f'{bot.rnd_id()}.mp3')
    r = (await bot.recognize(file)).get('track', None)
    os.remove(file)
    if r is None:
        await message.reply_text(
            '**⚠️ Cannot recognize the audio**'
        )
        return
    out = f'**Title**: `{r["title"]}`\n'
    out += f'**Artist**: `{r["subtitle"]}`\n'
    buttons = [
            [
                types.InlineKeyboardButton(
                    '🎼 Related Songs',
                    switch_inline_query_current_chat=f'related {r["key"]}',
                ),
                types.InlineKeyboardButton(
                    '🔗 Share',
                    url=f'{r["share"]["html"]}'
                )
            ],
            [
                types.InlineKeyboardButton(
                    '🎵 Listen',
                    url=f'{r["url"]}'
                )
            ],        
        ]
    response = r.get('artists', None)
    if response:
        buttons.append(
            [
                types.InlineKeyboardButton(
                    f'💿 More Tracks from {r["subtitle"]}',
                    switch_inline_query_current_chat=f'tracks {r["artists"][0]["id"]}',
                )
            ]
        )
    await message.reply_photo(
        r['images']['coverarthq'],
        caption=out,
        reply_markup=types.InlineKeyboardMarkup(buttons)
    )
    await status.delete()
    os.remove(f"{str(user_id)}.mp3")
