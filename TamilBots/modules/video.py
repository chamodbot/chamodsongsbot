import os
import wget
import requests
from yt_dlp import YoutubeDL
from TamilBots import app, LOGGER
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
from youtube_search import YoutubeSearch

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="π  zoneunlimited  π", url=f"https://t.me/zoneunlimited") 
        ]]      
    )


@app.on_message(filters.command(["video"]))
async def vsong(pbot, message):
    try:
        await message.reply_chat_action("typing")
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**βοΈ Access Denied βοΈ**\n\nπββοΈ **Hey There** {message.from_user.mention}, You Must **Join** @zoneunlimited Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Againπ€. **Thank** You π€", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
    )
        return
    await message.reply_chat_action("typing")
    ydl_opts = {
        'format':'best',
        'keepvideo':True,
        'prefer_ffmpeg':False,
        'geo_bypass':True,
        'outtmpl':'%(title)s.%(ext)s',
        'quite':True
    }
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
        await message.reply_chat_action("record_video_note")
        with YoutubeDL(ydl_opts) as ytdl:
            rep = f'**{title[:35]}\n\n**β Successfully Downloaded to MP4 π₯\n\nβββββββββββββββββββ\n\nβ£β Duration : {duration}\n\nβ£β Views : {views}\n\nβ£β πΊ Requestor : {message.from_user.mention} \n\nβ£β π· Downloaded by : [MUSIC FINDER BOT π΅](https://t.me/The_song_finder_bot)\n\nβ£β [π zoneunlimited π](https://t.me/zoneunlimited)Corporation Β©οΈ\n\nβββββββββββββββββββ\n\n '
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit("**πΆ Oops Not Found !! ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("βββββββββββββββ", callback_data="chamod")]]))
    preview = wget.download(thumbnail)
    await message.reply_chat_action("upload_video_note")
    await msg.edit("**π αα­αͺOα©αͺIαG ααΎ Tαͺα?Gαα©α° ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("βββββββββββββββ", callback_data="chamod")]]))
    await message.reply_chat_action("upload_video_note")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=rep,
        reply_markup= button)
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)
