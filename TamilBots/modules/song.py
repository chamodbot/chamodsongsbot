from pyrogram import Client, filters
from config import OWNER_ID
from config import GROUP_ID
import asyncio
import os
import requests
import yt_dlp
from funcs.download import Descargar
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from pyrogram.errors.exceptions import MessageNotModified
from pytube import YouTube, exceptions
from pyrogram.types import InlineKeyboardMarkup, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, CallbackQuery
from pyrogram.types import InlineKeyboardButton
from youtubesearchpython import VideosSearch
from youtubesearchpython import SearchVideos
from TamilBots.TamilBots import ignore_blacklisted_users, get_arg
from TamilBots import app, LOGGER
from TamilBots.sql.chat_sql import add_chat_to_db
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1901997764 1474804964").split())
GROUP_ID = set(int(x) for x in os.environ.get("GROUP_ID", "-1001615594988").split())

def yt_search(song):
    videosSearch = VideosSearch(song, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url

@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("tools"))
async def song(client, message):
    chat_id = message.chat.id
    if message.from_user.id not in AUTH_USERS:
        await message.reply("**⛔️ Access Denied ⛔️**\n\n**Please Contact** @chamod_deshan to **Get Access** or Join @zoneunlimited to Access **This Service** 🌷")
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
    await status.edit("**⭕️ Music Savers Update Successfully ...**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🌐 Update Now Music Savers 🎶", callback_data="tools")
                 ],[
                    InlineKeyboardButton("🚫   close   🚫", callback_data="close")
            ]
          ]
        )
   )

@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("song"))
def song(_, message):
    chat_id = message.chat.id
    query = " ".join(message.text[1:])
    m = message.reply_chat_action("record_audio")
    m = message.reply("**🎵 Searching Music Savers ...**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("░░░░░░░░░░░░░░░░", callback_data="tools")
                 ],[
                    InlineKeyboardButton("░░░░░░░░░░░░░░░░", callback_data="close")
            ]
          ]
        )
   )
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
            [
                [
                    InlineKeyboardButton("▓▓░░░░░░░░░░░░░░", callback_data="tools")
                 ],[
                    InlineKeyboardButton("░░░░░░░░░░░on ©️", callback_data="close")
            ]
          ]
        )
   )

    m.edit("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("▓▓░░░░░░░░░░░░░░", callback_data="tools")
                 ],[
                    InlineKeyboardButton("░░░░░░░░░░░tion ©️", callback_data="close")
            ]
          ]
        )
   )
    m.edit("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("▓▓░░░░░░░░░░░░░░", callback_data="tools")
                 ],[
                    InlineKeyboardButton("░░░░░░░░ Coration ©️", callback_data="close")
            ]
          ]
        )
   )
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"[{title[:35]}]({link})\n\n┏━━━━━━━━━━━━━━━━━┓\n\n┣★ Duration : `{duration}`\n\n┣★ Views : {views}\n\n┣★ **✅ Successfully Downloaded to MP3 🎵**\n\n┣★ 🌺 Requestor :  \n\n┣★ 🌷 Downloaded by : [MUSIC FINDER BOT 🎵](https://t.me/The_song_finder_bot)\n\n┣★ [🍀 zoneunlimited 🍀](https://t.me/zoneunlimited)Corporation ©️\n\n┗━━━━━━━━━━━━━━━━━┛\n\n"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("▓▓░░░░░░░░░░░░░░", callback_data="tools")
                 ],[
                    InlineKeyboardButton("░░░░░mited 🍀 Corporation ©️", callback_data="close")
            ]
          ]
        )
   )
        m.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("▓▓░░░░░░░░░░░░░░", callback_data="tools")
                 ],[
                    InlineKeyboardButton("░░unlimited 🍀 Corporation ©️", callback_data="close")
            ]
          ]
        )
   )
        m.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("▓▓░░░░░░░░░░░░░░", callback_data="tools")
                 ],[
                    InlineKeyboardButton("🍀 zoneunlimited 🍀 Corporation ©️", callback_data="close")
            ]
          ]
        )
   )
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

@app.on_inline_query()
async def inline(client: Client, query: InlineQuery):
    answers = []
    search_query = query.query.lower().strip().rstrip()

    if search_query == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text="🔍 Search YouTube 🔎",
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        search = VideosSearch(search_query, limit=50)

        for result in search.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description="{}, {} views.".format(
                        result["duration"],
                        result["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "https://www.youtube.com/watch?v={}".format(
                            result["id"]
                        )
                    ),
                    thumb_url=result["thumbnails"][0]["url"]
                )
            )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="😶 Oops Not Found ...",
                switch_pm_parameter="",
            )
