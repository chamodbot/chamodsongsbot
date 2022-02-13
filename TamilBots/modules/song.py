from pyrogram import Client, filters
from config import OWNER_ID
from pyrogram import Client
from requests import get
from typing import Tuple
from json import JSONDecodeError
import asyncio
import shlex
import time
import wget
import wikipedia
import os
import requests
import youtube_dl
import yt_dlp
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
        InlineKeyboardButton(text="🍀  zoneunlimited  🍀", url=f"https://t.me/zoneunlimited") 
        ]]      
    )

        
def check_ws(message):
  request = message.text.split()
  if len(request) < 2 or request[0] not in "ws":
    return False
  else:
    return True

@app.on_message(filters.private & filters.text)
def wiki_search(message):
  pass

#basic_url = https://youtu.be/E-7RhUMBzi8 or https://www.youtube.com/watch?v=vC-ZjwxBnMg
#(basic_url.split("/")[2]) = youtu.be or www.youtube.com

def yt_downloader(query,message):
  try:
    text = query.message.text
    chat_id = message.chat.id
    app.send_message(chat_id,"Downloading audio may take some time, ⌛ ￣へ￣ " )
    video = pafy.new(text)
    vid_big = video.bigthumb
    best_audio = video.getbestaudio(preftype='m4a')
    check_length = int(video.duration.split(":")[1])
    hr_check = int(video.duration.split(":")[0])
    if check_length < 6 and hr_check == 0:
      best_audio.download(filepath = "music") 
      vid_loc = f'''music/{video.title}.m4a'''
      audio = open(vid_loc, 'rb')
      if message.chat.type == "private":
        app.send_audio(chat_id,audio,duration = video.duration, performer = video.author, title = video.title,thumb = vid_big)
      if message.chat.type == "group":
        app.send_audio(chat_id,audio,duration = video.duration, performer = video.author, title = video.title,thumb = vid_big)
    else:
        app.send_message(chat_id,f"Audio duration greater then 5 mins, duration: {check_length}")
  except:
    app.send_message(chat_id,"Something went wrong")


@app.on_message(filters.command(["song"]))
async def song(__, message):
    try:
        await message.reply_chat_action("import_history")
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @zoneunlimited Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
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
            InlineKeyboardButton("🌺 Watch On Youtube 🌺", url=f"{link}")
        ],
        [
            InlineKeyboardButton("🔍◇─◇Search Again◇─◇🔎", switch_inline_query_current_chat="")
        ]
    ]
    
    )
        rby = message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("**🎵 Sεαяcнıпɢ Mυƨıc Sανεяƨ ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("███████████████", callback_data="progress_msg")]]), reply_to_message_id = message.message_id)
        await msg.edit("**🌷 ƊօωղƖօąɗíղɠ Mυƨıc Sανεяƨ ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("███████████████", callback_data="progress_msg")]]))
        await message.reply_chat_action("record_audio")
        with YoutubeDL(ydl_opts) as ytdl:
            rep = f'**{title[:35]}**\n\n✅ Successfully Downloaded to MP3 🎵\n\n┏━━━━━━━━━━━━━━━━━┓\n\n┣★ Duration : {duration}\n\n┣★ Views : {views}\n\n┣★ 🌺 Requestor : {message.from_user.mention} \n\n┣★ 🌷 Downloaded by : [MUSIC FINDER BOT 🎵](https://t.me/The_song_finder_bot)\n\n┣★ [🍀 zoneunlimited 🍀](https://t.me/zoneunlimited)Corporation ©️\n\n┗━━━━━━━━━━━━━━━━━┛\n\n '
            ytdl_data = ytdl.extract_info(link, download=True)
            audio_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit("**😶 Oops Not Found !! ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("███████████████", callback_data="progress_msg")]]))
   
    preview = wget.download(thumbnail)
    await message.reply_chat_action("upload_audio")
    await msg.edit("**🍀 ᑌᑭᒪOᗩᗪIᑎG ᏆᎾ TᒪᕮGᖇᗩᗰ ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("███████████████", callback_data="progress_msg")]]))
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
