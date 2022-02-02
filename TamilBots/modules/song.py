from pyrogram import Client, filters
from config import OWNER_ID
import asyncio
import os
from typing import Tuple
from pytube import YouTube
from pyrogram.types import InlineKeyboardMarkup, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, CallbackQuery
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
        caption=f"\n\n╠《》《》《》《》《》《》《》《》《》╣\n\n◇───────────────◇\n\n**✅ Successfully Downloaded to mp4 🎥**\n\n🌺 Requestor : [Requestor](tg://settings)\n🌷 Downloaded by : [Music Finder Bot](https://t.me/The_song_finder_bot)\n[🍀 zoneunlimited 🍀](https://t.me/zoneunlimited)Corporation ©️\n\n╠《》《》《》《》《》《》《》《》《》╣\n\n◇───────────────◇\n\n",
        reply_to_message_id=message.message_id,
    )
    await status.delete()
    os.remove(f"{str(user_id)}.mp4")

@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("tool"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text="**🌷 Restarting Music Savers ....**"
    btn = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="✪❖◈◈◈❖◈◈◈❖◈◈◈❖✪", callback_data="progress_msg")]])
    await message.edit("**🌷 Restarting Music Savers ....**"
    await message.edit_reply_markup(
        InlineKeyboardMarkup([[InlineKeyboardButton("☯◈◈◈☬◈◈◈☬◈◈◈☯, callback_data="down")]]))

    await message.reply(text, reply_markup=btn)

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
