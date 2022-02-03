from pyrogram import Client, filters
from config import OWNER_ID
import asyncio
import os
from funcs.download import Descargar
from pyrogram.errors.exceptions import MessageNotModified
from pytube import YouTube
from pyrogram.types import InlineKeyboardMarkup, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, CallbackQuery
from pyrogram.types import InlineKeyboardButton
from youtubesearchpython import VideosSearch
from TamilBots.TamilBots import ignore_blacklisted_users, get_arg
from TamilBots import app, LOGGER
from TamilBots.sql.chat_sql import add_chat_to_db
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1901997764 1474804964").split())


def yt_search(song):
    videosSearch = VideosSearch(song, limit=1)
    result = videosSearch.result()
    if not result:
        return False
    else:
        video_id = result["result"][0]["id"]
        url = f"https://youtu.be/{video_id}"
        return url


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("songjsj"))
async def song(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    add_chat_to_db(str(chat_id))
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("**😶 Oops Not Found !! ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◉◑◒◓◔◕◉◑◒◓◔◕◉", callback_data="progress_msg")]]))
        return ""
    await message.reply_chat_action("typing")
    status = await message.reply("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓░░░░░░░░░░", callback_data="progress_msg")]]))
    await message.reply_chat_action("record_audio")
    await status.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░", callback_data="progress_msg")]]))
    await status.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", callback_data="progress_msg")]]))
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
        caption=f"\n\n╠《》《》《》《》《》《》《》《》《》╣\n\n◇───────────────◇\n\n**✅ Successfully Downloaded to MP3 🎵**\n\n🌺 Requestor : [Requestor](tg://settings)\n🌷 Downloaded by : [MUSIC FINDER BOT 🎵](https://t.me/The_song_finder_bot)\n[🍀 zoneunlimited 🍀](https://t.me/zoneunlimited)Corporation ©️\n\n╠《》《》《》《》《》《》《》《》《》╣\n\n◇───────────────◇\n\n",
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
        await message.reply("**😶 Oops Not Found !! ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("☸◉◑◒◓◔◕◉◑◒◓◔◕◉☸", callback_data="progress_msg")]]))
        return ""
    await message.reply_chat_action("typing")
    status = await message.reply("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓░░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓░░░░░░░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌷 Downloading Music Savers ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓░░░░░░░░░░", callback_data="progress_msg")]]))
    await message.reply_chat_action("record_video_note")
    await status.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓░░░░░░", callback_data="progress_msg")]]))
    await status.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░", callback_data="progress_msg")]]))
    await status.edit("**🌺 Uploading To Telegram ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓", callback_data="progress_msg")]]))
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
        caption=f"\n\n╠《》《》《》《》《》《》《》《》《》╣\n\n◇───────────────◇\n\n**✅ Successfully Downloaded to mp4 🎥**\n\n🌺 Requestor : [Requestor](tg://settings)\n🌷 Downloaded by : [MUSIC FINDER BOT 🎵](https://t.me/The_song_finder_bot)\n[🍀 zoneunlimited 🍀](https://t.me/zoneunlimited)Corporation ©️\n\n╠《》《》《》《》《》《》《》《》《》╣\n\n◇───────────────◇\n\n",
        reply_to_message_id=message.message_id,
    )
    await status.delete()
    os.remove(f"{str(user_id)}.mp4")


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("tools"))
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

@app.on_message(
    filters.command(['song'],prefixes=['/', '!'])
    & (filters.group | filters.private)
    & ~ filters.edited)
async def song_dl(_, msg: Message):

    if len(msg.command) == 1:
        return await msg.reply(text=text, parse_mode='md')

    r_text = await msg.reply('Processing...')
    url = msg.text.split(None, 1)[1]
    url = extract_the_url(url=url)
    
    if url == 0:return await r_text.edit('I could not find that song. Try with another keywords...')

    await r_text.edit('Downloading...')

    ytinfo = descargar.mp3_viaPytube(url)

    if ytinfo == 0:
        await r_text.edit(f'Something Wrong\n\n☕️Take a Coffee and come again... :(')
        return

    try:
        await r_text.edit_text('Uploading...')
    except MessageNotModified:
        pass

    await msg.reply_audio(
            audio=f'downloads/{ytinfo.title.replace("/","|")}-{ytinfo.video_id}.mp3', 
            thumb='src/Medusa320px.png',
            duration=int(ytinfo.length),
            performer=str(ytinfo.author),
            title=f'{str(ytinfo.title)}',
            caption=f"<a href='{url}'>__{ytinfo.title}__</a>\n\n__Downloaded by @MedusaMousikibot__"
        )

    await r_text.delete()
    os.remove(f'downloads/{ytinfo.title.replace("/","|")}-{ytinfo.video_id}.mp3')
    

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
