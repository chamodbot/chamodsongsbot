from pyrogram import Client, filters
from config import OWNER_ID
from config import GROUP_ID
import asyncio
import time
import os
import requests
import yt_dlp
from funcs.download import Descargar
from yt_dlp import YoutubeDL
from mixpanel import Mixpanel
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
MIXPANEL_TOKEN = os.environ.get('df25e802e5515ec5a943c5e654d3006c')
MUSIC_CHATS = set(int(x) for x in os.environ.get("MUSIC_CHATS", "1901997764 1474804964").split())

def yt_search(song):
    videosSearch = VideosSearch(song, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url

text_filter = (filters.update)

@app.on_message(text_filter)
async def update(Client, message):
    if message.from_user.id not in AUTH_USERS:
        await message.reply("**⛔️ Access Denied ⛔️**\n\n**Please Contact** @chamod_deshan to **Get Access** or Join @zoneunlimited to Access **This Service** 🌷")
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
                    InlineKeyboardButton("🌐 Update Now Music Savers 🎶", callback_data="")
                 ],[
                    InlineKeyboardButton("🚫   close   🚫", callback_data="close")
            ]
          ]
        )
   )

@app.on_message(filters.command("song"))
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
                    InlineKeyboardButton("▓▓▓▓░░░░░░░░░░░░", callback_data="tools")
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
                    InlineKeyboardButton("▓▓▓▓▓▓▓░░░░░░░░░░", callback_data="tools")
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
                    InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░", callback_data="tools")
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
                    InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░", callback_data="tools")
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
                    InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", callback_data="tools")
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



REGEX_SITES = (
    r"^((?:https?:)?\/\/)"
    r"?((?:www|m)\.)"
    r"?((?:youtube\.com|youtu\.be|soundcloud\.com|mixcloud\.com))"
    r"(\/)([-a-zA-Z0-9()@:%_\+.~#?&//=]*)([\w\-]+)(\S+)?$"
)
REGEX_EXCLUDE_URL = (
    r"\/channel\/|\/playlist\?list=|&list=|\/sets\/"
)

main_filter = (
    filters.text
    & filters.command("audio")
    & filters.incoming
    & ~filters.edited
)


@app.on_message(main_filter
                & filters.regex(REGEX_SITES)
                & ~filters.regex(REGEX_EXCLUDE_URL))
async def music_downloader(_, message: Message):
    await _fetch_and_send_music(message)


async def _fetch_and_send_music(message: Message):
    await message.reply_chat_action("typing")
    try:
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': '%(title)s - %(extractor)s-%(id)s.%(ext)s',
            'writethumbnail': True
        }
        ydl = YoutubeDL(ydl_opts)
        info_dict = ydl.extract_info(message.text, download=False)
        # send a link as a reply to bypass Music category check
        if not message.reply_to_message \
                and _youtube_video_not_music(info_dict):
            inform = ("This video is not under Music category, "
                      "you can resend the link as a reply "
                      "to force download it")
            await _reply_and_delete_later(message, inform,
                                          DELAY_DELETE_INFORM)
            return
        if info_dict['duration'] > MUSIC_MAX_LENGTH:
            readable_max_length = str(timedelta(seconds=MUSIC_MAX_LENGTH))
            inform = ("This won't be downloaded because its audio length is "
                      "longer than the limit `{}` which is set by the bot"
                      .format(readable_max_length))
            await _reply_and_delete_later(message, inform,
                                          DELAY_DELETE_INFORM)
            return
        d_status = await message.reply_text("Downloading...", quote=True,
                                            disable_notification=True)
        ydl.process_info(info_dict)
        audio_file = ydl.prepare_filename(info_dict)
        task = asyncio.create_task(_upload_audio(message, info_dict,
                                                 audio_file))
        await message.reply_chat_action("upload_document")
        await d_status.delete()
        while not task.done():
            await asyncio.sleep(4)
            await message.reply_chat_action("upload_document")
        await message.reply_chat_action("cancel")
        if message.chat.type == "private":
            await message.delete()
    except Exception as e:
        await message.reply_text(repr(e))


def _youtube_video_not_music(info_dict):
    if info_dict['extractor'] == 'youtube' \
            and 'Music' not in info_dict['categories']:
        return True
    return False


async def _reply_and_delete_later(message: Message, text: str, delay: int):
    reply = await message.reply_text(text, quote=True)
    await asyncio.sleep(delay)
    await reply.delete()


async def _upload_audio(message: Message, info_dict, audio_file):
    basename = audio_file.rsplit(".", 1)[-2]
    if info_dict['ext'] == 'webm':
        audio_file_opus = basename + ".opus"
        ffmpeg.input(audio_file).output(audio_file_opus, codec="copy").run()
        os.remove(audio_file)
        audio_file = audio_file_opus
    thumbnail_url = info_dict['thumbnail']
    if os.path.isfile(basename + ".jpg"):
        thumbnail_file = basename + ".jpg"
    else:
        thumbnail_file = basename + "." + \
            _get_file_extension_from_url(thumbnail_url)
    squarethumb_file = basename + "_squarethumb.jpg"
    make_squarethumb(thumbnail_file, squarethumb_file)
    webpage_url = info_dict['webpage_url']
    title = info_dict['title']
    caption = f"<b><a href=\"{webpage_url}\">{title}</a></b>"
    duration = int(float(info_dict['duration']))
    performer = info_dict['uploader']
    await message.reply_audio(audio_file,
                              caption=caption,
                              duration=duration,
                              performer=performer,
                              title=title,
                              parse_mode='HTML',
                              thumb=squarethumb_file)
    for f in (audio_file, thumbnail_file, squarethumb_file):
        os.remove(f)

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
