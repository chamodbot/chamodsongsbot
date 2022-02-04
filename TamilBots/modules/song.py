from pyrogram import Client, filters
from config import OWNER_ID
import asyncio
import os
import requests
import yt_dlp
from funcs.download import Descargar
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from pyrogram.errors.exceptions import MessageNotModified
from pytube import YouTube
from pyrogram.types import InlineKeyboardMarkup, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, CallbackQuery
from pyrogram.types import InlineKeyboardButton
from youtubesearchpython import VideosSearch
from youtubesearchpython import SearchVideos
from TamilBots.TamilBots import ignore_blacklisted_users, get_arg
from TamilBots import app, LOGGER
from TamilBots.sql.chat_sql import add_chat_to_db
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1901997764 1474804964").split())

@app.on_message(filters.command("tools"))
async def song(client, message):
    chat_id = message.chat.id
    if message.from_user.id not in AUTH_USERS:
        await message.reply("**⛔️ Access Denied ⛔️**\n\n**Please Contact** @chamod_deshan to **Get Access** or Join [zoneunlimited](https://t.me/zoneunlimited) to Access **This Service** 🌷")
        return ""
    add_chat_to_db(str(chat_id))
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("**🧐 My owner is not admin this group or chanle !! ..**")
        return ""
    status = await message.reply("**🌷 Updating Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Updating Music Savers ....\n m.youtube.com**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Updating Music Savers ....\n m.youtube.com\n Update Successfully 🌷..**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Updating Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Updating Music Savers ....\n www.spotify.com**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Updating Music Savers ....\n www.spotify.com \n Update Successfully 🌷**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Updating Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Updating Music Savers ....\n www.deezer.com**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Updating Music Savers ....\n www.deezer.com \n Update Successfully 🌷..**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Updating Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Updating Music Savers ....\n www.shazam.com**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓▓▓░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Updating Music Savers .... www.shazam.com \n Update Successfully 🌷..**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", callback_data="progress_msg")]]))
    await status.edit("**✅ Music Savers Update Successfully ...**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("♻️ Update Now Music Savers", callback_data="command_tools")]]))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("song"))
def song(_, message):
    query = " ".join(message.text[1:])
    m = message.reply_chat_action("record_audio")
    m = message.reply("**🎵 Searching Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        views = results[0]["views"]

    except Exception as e:
        m.edit("**😶 Oops Not Found !! ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☬༒༺༄༆☬༻༄༆༒☬", callback_data="progress_msg")]])) 
        print(str(e))
        return
    m.edit("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    m.edit("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓░░░░░░░░░░░░", callback_data="progress_msg")]]))
    m.edit("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓░░░░░░░░░░", callback_data="progress_msg")]]))
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"[{title[:35]}]({link})\n\n┏━━━━━━━━━━━━━━━━━┓\n\n┣★ Duration: `{duration}`\n\n┣★ Views: {views}\n\n┣★ **✅ Successfully Downloaded to MP3 🎵**\n\n┣★ 🌺 Requestor : \n\n┣★ 🌷 Downloaded by : [MUSIC FINDER BOT 🎵](https://t.me/The_song_finder_bot)\n\n┣★ [🍀 zoneunlimited 🍀](https://t.me/zoneunlimited)Corporation ©️\n\n┗━━━━━━━━━━━━━━━━━┛\n\n"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓░░░░░░", callback_data="progress_msg")]]))
        m.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░", callback_data="progress_msg")]]))
        m.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", callback_data="progress_msg")]]))
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit("**😶 Oops Not Found !! ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☬༒༺༄༆☬༻༄༆༒☬", callback_data="progress_msg")]])) 
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

@app.on_message(filters.command("audio"))
async def song(client, message):
    chat_id = message.chat.id
    status = await message.reply("🚀 🔎 🔎 𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐭𝐡𝐞 𝐬𝐨𝐧𝐠.")
    link = message.text.split('audio', maxsplit=1)[1]
    try:
        yt = YouTube(link)
        audio = yt.streams.get_audio_only().download('res')
        title = yt.title
        app.send_chat_action(message.chat.id, "upload_audio")
        app.send_audio(
        chat_id=message.chat.id,
        audio=f"{str(user_id)}.mp3",
        duration=int(yt.length),
        title=str(yt.title),
        performer=str(yt.author),
        reply_to_message_id=message.message_id,
    )
   
