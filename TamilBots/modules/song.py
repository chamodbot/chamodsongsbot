from pyrogram import Client, filters
import asyncio
import os
import json, requests, os, shlex, asyncio, uuid, shutil
from typing import Tuple
from pytube import YouTube
from pyrogram.types import InlineKeyboardMarkup, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, CallbackQuery
from pyrogram.types import InlineKeyboardButton
from youtubesearchpython import VideosSearch
from TamilBots.TamilBots import ignore_blacklisted_users, get_arg
from TamilBots import app, LOGGER
from TamilBots.sql.chat_sql import add_chat_to_db


API_HASH = os.environ['API_HASH']
API_ID = int(os.environ['APP_ID'])
BOT_TOKEN = os.environ['BOT_TOKEN']
downloads = './downloads/{}/'

def yt_search(song):
    videosSearch = VideosSearch(song, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("song"))
async def song(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    add_chat_to_db(str(chat_id))
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("**😶 Oops Not Found ...**")
        return ""
    await message.reply_chat_action("typing")
    status = await message.reply("** Searching music Savers ...**")
    await status.edit_reply_markup(
        InlineKeyboardMarkup([[InlineKeyboardButton("🔍 Searching Music ... 🔎", callback_data="down")]]))
    await status.edit("**🌷 Downloading music savers ...**")
    await status.edit_reply_markup(
        InlineKeyboardMarkup([[InlineKeyboardButton("╠《》《》《》《》《》《》《》《》《》╣", callback_data="down")]]))
    await message.reply_chat_action("record_audio")
    await status.edit("**🍀 Uploading To Telegram ...**")
    await status.edit_reply_markup(
        InlineKeyboardMarkup([[InlineKeyboardButton("╠《》《》《》《》《》《》《》《》《》╣", callback_data="down")]]))
    video_link = yt_search(args)
    if not video_link:
        await status.edit("**😶 Oops Not Found ...**")
        return ""
    yt = YouTube(video_link)
    audio = yt.streams.filter(only_audio=True).first()
    try:
        download = audio.download(filename=f"{str(user_id)}")
    except Exception as ex:
        await status.edit("Failed to download song 😶")
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
        caption=f"\n\n╠《》《》《》《》《》《》《》《》《》╣\n\n◇───────────────◇\n\n**✅ Successfully Downloaded to MP3 🎵**\n\n🌺 Requestor : [Requestor](tg://settings)\n🌷 Downloaded by : [Music Finder Bot](https://t.me/The_song_finder_bot)\n[🍀 zoneunlimited 🍀](https://t.me/zoneunlimited)Corporation ©️\n\n╠《》《》《》《》《》《》《》《》《》╣\n\n◇───────────────◇\n\n",
        reply_to_message_id=message.message_id,
    )
    await status.delete()
    os.remove(f"{str(user_id)}.mp3")


def yt_search(video):
    videosSearch = VideosSearch(video, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("video"))
async def video(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    add_chat_to_db(str(chat_id))
    args = get_arg(message) + " " + "video"
    if args.startswith(" "):
        await message.reply("**😶 Oops Not Found ...**")
        return ""
    await message.reply_chat_action("typing")
    status = await message.reply("** Searching music Savers ...**")
    await status.edit_reply_markup(
        InlineKeyboardMarkup([[InlineKeyboardButton("🔍 Searching Music ... 🔎", callback_data="down")]]))
    await status.edit("**🌷 Downloading music savers ...**")
    await status.edit_reply_markup(
        InlineKeyboardMarkup([[InlineKeyboardButton("╠《》《》《》《》《》《》《》《》《》╣", callback_data="down")]]))
    await message.reply_chat_action("record_video_note")
    await status.edit("**🍀 Uploading To Telegram ...**")
    await status.edit_reply_markup(
        InlineKeyboardMarkup([[InlineKeyboardButton("╠《》《》《》《》《》《》《》《》《》╣", callback_data="down")]]))
    video_link = yt_search(args)
    if not video_link:
        await status.edit("**😶 Oops Not Found ...**")
        return ""
    yt = YouTube(video_link)
    video = yt.streams.filter(only_video=True).first()
    try:
        download = video.download(filename=f"{str(user_id)}")
    except Exception as ex:
        await status.edit("Failed to download song 😶")
        LOGGER.error(ex)
        return ""
    rename = os.rename(download, f"{str(user_id)}.mp4")
    await app.send_chat_action(message.chat.id, "upload_video_note")
    await app.send_video(
        chat_id=message.chat.id,
        video=f"{str(user_id)}.mp4",
        duration=int(yt.length),
        caption=f"\n\n╠《》《》《》《》《》《》《》《》《》╣\n\n◇───────────────◇\n\n**✅ Successfully Downloaded to MP3 🎵**\n\n🌺 Requestor : [Requestor](tg://settings)\n🌷 Downloaded by : [Music Finder Bot](https://t.me/The_song_finder_bot)\n[🍀 zoneunlimited 🍀](https://t.me/zoneunlimited)Corporation ©️\n\n╠《》《》《》《》《》《》《》《》《》╣\n\n◇───────────────◇\n\n",
        reply_to_message_id=message.message_id,
    )
    await status.delete()
    os.remove(f"{str(user_id)}.mp4")

DL_BUTTONS=[
    [
        InlineKeyboardButton('🌷 No Watermark 🌷', callback_data='nowm'),
        InlineKeyboardButton('🌺 Watermark 🌺', callback_data='wm'),
    ],
    [InlineKeyboardButton('🎵 Audio 🎵', callback_data='audio')],
]

@app.on_message(filters.regex(pattern='.*http.*') & filters.private)
async def _tiktok(bot, update):
  url = update.text
  session = requests.Session()
  resp = session.head(url, allow_redirects=True)
  if not 'tiktok.com' in resp.url:
    return
  await update.reply('Select the buttons below..🌷', True, reply_markup=InlineKeyboardMarkup(DL_BUTTONS))

# Callbacks
@app.on_callback_query()
async def _callbacks(bot, cb: CallbackQuery):
  if cb.data == 'nowm':
    dirs = downloads.format(uuid.uuid4().hex)
    os.makedirs(dirs)
    cbb = cb
    update = cbb.message.reply_to_message
    await cb.message.delete()
    url = update.text
    session = requests.Session()
    resp = session.head(url, allow_redirects=True)
    if '?' in resp.url:
      tt = resp.url.split('?', 1)[0]
    else:
      tt = resp.url
    ttid = dirs+tt.split('/')[-1]
    r = requests.get('https://api.reiyuura.me/api/dl/tiktok?url='+tt)
    result = r.text
    rs = json.loads(result)
    link = rs['result']['nowm']
    resp = session.head(link, allow_redirects=True)
    r = requests.get(resp.url, allow_redirects=True)
    open(f'{ttid}.mp4', 'wb').write(r.content)
    await bot.send_video(update.chat.id, f'{ttid}.mp4',)
    shutil.rmtree(dirs)
  elif cb.data == 'wm':
    dirs = downloads.format(uuid.uuid4().hex)
    os.makedirs(dirs)
    cbb = cb
    update = cbb.message.reply_to_message
    await cb.message.delete()
    url = update.text
    session = requests.Session()
    resp = session.head(url, allow_redirects=True)
    if '?' in resp.url:
      tt = resp.url.split('?', 1)[0]
    else:
      tt = resp.url
    ttid = dirs+tt.split('/')[-1]
    r = requests.get('https://api.reiyuura.me/api/dl/tiktok?url='+tt)
    result = r.text
    rs = json.loads(result)
    link = rs['result']['wm']
    resp = session.head(link, allow_redirects=True)
    r = requests.get(resp.url, allow_redirects=True)
    open(f'{ttid}.mp4', 'wb').write(r.content)
    await bot.send_video(update.chat.id, f'{ttid}.mp4',)
    shutil.rmtree(dirs)
  elif cb.data == 'audio':
    dirs = downloads.format(uuid.uuid4().hex)
    os.makedirs(dirs)
    cbb = cb
    update = cbb.message.reply_to_message
    await cb.message.delete()
    url = update.text
    session = requests.Session()
    resp = session.head(url, allow_redirects=True)
    if '?' in resp.url:
      tt = resp.url.split('?', 1)[0]
    else:
      tt = resp.url
    ttid = dirs+tt.split('/')[-1]
    r = requests.get('https://api.reiyuura.me/api/dl/tiktok?url='+tt)
    result = r.text
    rs = json.loads(result)
    link = rs['result']['wm']
    resp = session.head(link, allow_redirects=True)
    r = requests.get(resp.url, allow_redirects=True)
    open(f'{ttid}.mp4', 'wb').write(r.content)
    cmd = f'ffmpeg -i "{ttid}.mp4" -vn -ar 44100 -ac 2 -ab 192 -f mp3 "{ttid}.mp3"'
    await run_cmd(cmd)
    await bot.send_audio(update.chat.id, f'{ttid}.mp3',)
    shutil.rmtree(dirs)


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
