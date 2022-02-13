from pyrogram import Client, filters
from config import OWNER_ID
from pyrogram import Client
from requests import get
from typing import Tuple
from json import JSONDecodeError

import sys
import telepot
import pafy

import asyncio
import shlex
import time
import wget
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

        
TOKEN = "5149412762:AAF1w1IwWC65J5_7Lj5yCs-6iRBhhaP2qvM"

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    flavor = telepot.flavor(msg)
    summary = telepot.glance(msg, flavor=flavor)
    print (flavor, summary)
    
    order = msg['text'].split(' ')
    title = ''
    url = ''
    flag_URL = 0
    flag_VIDEO = 0

    for text in order:
    	if text.startswith('https://') or text.startswith('www.') or text.startswith('youtu'):
    		url = text
    		flag_URL = 1
    	elif text.lower().startswith('video'):
    		flag_VIDEO = 1

    if flag_URL == 0:
    	bot.sendMessage(chat_id, 'Please enter a video link to download.')

    else:
        video = pafy.new(url)
        best = video.getbest()
        message = video.title + '\t(' + video.duration + ')'
        bot.sendMessage(chat_id, message)
        if flag_VIDEO == 1:
            r = requests.get('http://tinyurl.com/api-create.php?url=' + best.url)
            message = 'Download Video: ' + str(r.text)
            bot.sendMessage(chat_id, message)

        else :
            bestaudio = video.getbestaudio(preftype="m4a")
            r = requests.get('http://tinyurl.com/api-create.php?url=' + bestaudio.url)
            message = 'Download Audio: ' + str(r.text)
            bot.sendMessage(chat_id, message)
            message = 'IMPORTANT: After downloading, rename the file to (anyname).m4a.\nNOTE: You could also save in .mp3 extension, but m4a provides better quality!'
            bot.sendMessage(chat_id, message)

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

while 1:
    time.sleep(10)

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
