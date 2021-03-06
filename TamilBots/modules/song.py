from pyrogram import Client, filters, types
from config import OWNER_ID
from pyrogram import Client
from requests import get
from typing import Tuple
from json import JSONDecodeError
import asyncio
import shlex
import time
import wget
import os
import requests
import youtube_dl
import yt_dlp
from pytube import YouTube
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, CallbackQuery
from pyrogram.types import InlineKeyboardButton
from youtubesearchpython import VideosSearch
from youtubesearchpython import SearchVideos
from TamilBots.TamilBots import ignore_blacklisted_users, get_arg
from TamilBots import app, LOGGER
from TamilBots.sql.chat_sql import add_chat_to_db
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1901997764 1474804964").split())


FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="π  zoneunlimited  π", url=f"https://t.me/zoneunlimited") 
        ]]      
    )

        
@app.on_message(filters.command(["songjaja"]))
async def song(__, message):
    try:
        await message.reply_chat_action("import_history")
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**βοΈ Access Denied βοΈ**\n\nπββοΈ **Hey There** {message.from_user.mention}, You Must **Join** @zoneunlimited Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Againπ€. **Thank** You π€", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
    )
        return
    await message.reply_chat_action("typing")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        views = results[0]["views"]
        results[0]["url_suffix"]
        results[0]["views"]
        button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("πΊ Watch On Youtube πΊ", url=f"{link}")
        ],
        [
            InlineKeyboardButton("πβββSearch Againβββπ", switch_inline_query_current_chat="")
        ]
    ]
    
    )
        rby = message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("**π΅ SΞ΅Ξ±ΡcΠ½Δ±ΠΏΙ’ MΟΖ¨Δ±c SΞ±Ξ½Ξ΅ΡΖ¨ ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("βββββββββββββββ", callback_data="chamod")]]), reply_to_message_id = message.message_id)
        await msg.edit("**π· ΖΦΟΥ²ΖΦΔΙΓ­Υ²Ι  MΟΖ¨Δ±c SΞ±Ξ½Ξ΅ΡΖ¨ ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("βββββββββββββββ", callback_data="chamod")]]))
        await message.reply_chat_action("record_audio")
        with YoutubeDL(ydl_opts) as ytdl:
            rep = f'**{title[:35]}**\n\nβ Successfully Downloaded to MP3 π΅\n\nβββββββββββββββββββ\n\nβ£β Duration : {duration}\n\nβ£β Views : {views}\n\nβ£β πΊ Requestor : {message.from_user.mention} \n\nβ£β π· Downloaded by : [MUSIC FINDER BOT π΅](https://t.me/The_song_finder_bot)\n\nβ£β [π zoneunlimited π](https://t.me/zoneunlimited)Corporation Β©οΈ\n\nβββββββββββββββββββ\n\n '
            ytdl_data = ytdl.extract_info(link, download=True)
            audio_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit("**πΆ Oops Not Found !! ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("βββββββββββββββ", callback_data="chamod")]]))
   
    preview = wget.download(thumbnail)
    await message.reply_chat_action("upload_audio")
    await msg.edit("**π αα­αͺOα©αͺIαG ααΎ Tαͺα?Gαα©α° ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("βββββββββββββββ", callback_data="chamod")]]))
    await message.reply_chat_action("upload_audio")
    await message.reply_audio(
        audio_file,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=rep,
        reply_markup= button, reply_to_message_id = message.message_id)
    try:
        os.remove(audio_file)
        await msg.delete()
    except Exception as e:
        print(e)

def yt_search(song):
    videosSearch = VideosSearch(song, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url


@app.on_message(filters.command("song"))
async def song(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    add_chat_to_db(str(chat_id))
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("Enter a song name. Check /help")
        return ""
    status = await message.reply("**π΅ SΞ΅Ξ±ΡcΠ½Δ±ΠΏΙ’ MΟΖ¨Δ±c SΞ±Ξ½Ξ΅ΡΖ¨ ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("βββββββββββββββ", callback_data="chamod")]]), reply_to_message_id = message.message_id)
    await status.edit("**π· ΖΦΟΥ²ΖΦΔΙΓ­Υ²Ι  MΟΖ¨Δ±c SΞ±Ξ½Ξ΅ΡΖ¨ ....**",
    reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("βββββββββββββββ", callback_data="chamod")]]))
    await message.reply_chat_action("record_audio")
    video_link = yt_search(args)
    if not video_link:
        await status.edit("**πΆ Oops Not Found !! ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("βββββββββββββββ", callback_data="chamod")]]))
        return ""
    yt = YouTube(video_link)
    audio = yt.streams.filter(only_audio=True).first()
    try:
        download = audio.download(filename=f"{str(user_id)}")
    except Exception as ex:
        await status.edit("**πΆ Oops Not Found !! ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("βββββββββββββββ", callback_data="chamod")]]))
        LOGGER.error(ex)
        return ""
    rename = os.rename(download, f"{str(user_id)}.mp3")
    await app.send_chat_action(message.chat.id, "upload_audio")
    await app.send_audio(
        chat_id=message.chat.id,
        audio=f"{str(user_id)}.mp3",
        duration=int(yt.length),
        title=str(yt.title),
        performer=str(yt.author),
        reply_to_message_id=message.message_id,
    )
    await status.delete()
    os.remove(f"{str(user_id)}.mp3")

@app.on_callback_query(filters.regex(r"chamod"))
def audio_callback(client: "Client", callback_query: types.CallbackQuery):
    callback_query.answer(f"π zoneunlimited π Corporation Β©οΈ")

@app.on_callback_query()
async def button(app, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(app, update.message)
      elif "close" in cb_data:
        await update.message.delete() 
      elif "zone_ms" in cb_data:
        await update.message.delete()
        await zone_ms(app, update.message)
