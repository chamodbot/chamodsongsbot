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
        InlineKeyboardButton(text="🍀  zoneunlimited  🍀", url=f"https://t.me/zoneunlimited") 
        ]]      
    )


@app.on_message(filters.command(["video"]))
async def vsong(pbot, message):
    try:
        await message.reply_chat_action("typing")
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @zoneunlimited Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
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
        await message.reply_chat_action("record_video_note")
        with YoutubeDL(ydl_opts) as ytdl:
            rep = f'**{title[:35]}\n\n**✅ Successfully Downloaded to MP4 🎥\n\n┏━━━━━━━━━━━━━━━━━┓\n\n┣★ Duration : {duration}\n\n┣★ Views : {views}\n\n┣★ 🌺 Requestor : {message.from_user.mention} \n\n┣★ 🌷 Downloaded by : [MUSIC FINDER BOT 🎵](https://t.me/The_song_finder_bot)\n\n┣★ [🍀 zoneunlimited 🍀](https://t.me/zoneunlimited)Corporation ©️\n\n┗━━━━━━━━━━━━━━━━━┛\n\n '
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit("**😶 Oops Not Found !! ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("███████████████", callback_data="progress_msg")]]))
    preview = wget.download(thumbnail)
    await message.reply_chat_action("upload_video_note")
    await msg.edit("**🍀 ᑌᑭᒪOᗩᗪIᑎG ᏆᎾ TᒪᕮGᖇᗩᗰ ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("███████████████", callback_data="progress_msg")]]))
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
