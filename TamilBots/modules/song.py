from pyrogram import Client, filters
from pyrogram import filters, types
import asyncio
import os
from pytube import YouTube
from youtube_search import YoutubeSearch
from pyrogram.types import InlineKeyboardMarkup
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


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("ssh"))
async def song(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    add_chat_to_db(str(chat_id))
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("async def song(client, message)\n**✅ SUCCESSFULLY CREATED ✅**\n\n======================\n\n=**❌NO SPAM**\n=**❌NO DDOS**\n=**❌NO HACKING**\n=**❌NO CARDING**\n=**❌NO TORRENT**\n=**❌NO OVER DOWNLOAD**\n=**❌NO MULTILOGIN**\n=======================\n\n**ᗚ IP • ๛ :** `20.210.210.41`\n**ᗚ Username • ๛ :** `zussh`\n**ᗚ Password • ๛ :** `zussh`\n**ᗚ Expire • ๛ : ** 2022/01/30\n**ᗚ Limit • ๛ : ** 2 \n\n**࿂ SSH • **  22\n**࿂ SSL • **  443\n**࿂ Squid  • **  8080\n**࿂ Dropbear • **  80\n[-] ═───────◇───────═\n**࿂ Badvpn • **  7300\n[-] ═───────◇───────═\n** ☬[•] SCRIPTS ═◇ DARKSSH ◇═ [•]☬ **\n\n**🔥 Created by : ** [chamoddeshanbot🌷](https://t.me/chamod_deshanbot)\n**🌺 Requestor : ** [Created User](tg://settings)\n\n🍀 @zoneunlimited 🍀")
        return ""
    status = await message.reply("**⚙️ Creating Your ssh Account....**")
    await status.edit("**✅ SUCCESSFULLY CREATED ✅**\n\n======================\n\n=**❌NO SPAM**\n=**❌NO DDOS**\n=**❌NO HACKING**\n=**❌NO CARDING**\n=**❌NO TORRENT**\n=**❌NO OVER DOWNLOAD**\n=**❌NO MULTILOGIN**\n=======================\n\n**ᗚ IP • ๛ :** `20.210.210.41`\n**ᗚ Username • ๛ :** `zussh`\n**ᗚ Password • ๛ :** `zussh`\n**ᗚ Expire • ๛ : ** 2022/01/30\n**ᗚ Limit • ๛ : ** 2 \n\n**࿂ SSH • **  22\n**࿂ SSL • **  443\n**࿂ Squid  • **  8080\n**࿂ Dropbear • **  80\n[-] ═───────◇───────═\n**࿂ Badvpn • **  7300\n[-] ═───────◇───────═\n** ☬[•] SCRIPTS ═◇ DARKSSH ◇═ [•]☬ **\n\n**🔥 Created by : ** [chamoddeshanbot🌷](https://t.me/chamod_deshanbot)\n**🌺 Requestor : ** [Created User](tg://settings)\n\n🍀 @zoneunlimited 🍀")
    video_link = yt_search(args)
    if not video_link:
        await status.edit("✖️ 𝐅𝐨𝐮𝐧𝐝 𝐍𝐨𝐭𝐡𝐢𝐧𝐠. 𝐒𝐨𝐫𝐫𝐲.\n\n𝐓𝐫𝐲 𝐀𝐧𝐨𝐭𝐡𝐞𝐫 𝐊𝐞𝐲𝐰𝐨𝐫𝐤 𝐎𝐫 𝐌𝐚𝐲𝐛𝐞 𝐒𝐩𝐞𝐥𝐥 𝐈𝐭 𝐏𝐫𝐨𝐩𝐞𝐫𝐥𝐲.\n\nEg.`/song Faded`")
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
        reply_to_message_id=message.message_id,
    )
    await status.delete()
    os.remove(f"{str(user_id)}.mp3")
