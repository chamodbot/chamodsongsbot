from config import OWNER_ID
from pyrogram import idle, filters
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
        InlineKeyboardButton(text="π  zoneunlimited  π", url=f"https://t.me/zoneunlimited") 
        ]]      
    )


@app.on_message(filters.command("start"))
async def start_(client: Client, message: Message):
    try:
        await message.reply_chat_action("typing")
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**βοΈ Access Denied βοΈ**\n\nπββοΈ **Hey There** {message.from_user.mention}, You Must **Join** @zoneunlimited  Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Againπ€. **Thank** You π€", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
    )
        return
    await message.reply_sticker(sticker = "CAACAgIAAxkBAAIDTGIH_M97rDk5mOb2z2fa1mCHDeHVAAK4AAMw1J0R92WGDc8M6xUjBA")
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c14ff832c44a277759bd4.jpg",
        caption = """
π Hello There 

πββοΈ I am MUSIC FINDER BOT π΅,I can 

π΅ Downloading All song 
π· Downloading All Video 
π Downloading All TikTok
π Find Song Ditels 
β­οΈ Inline search 
πΊ Group Supported
π― 24 horse active

π₯ Bot Commands π₯

/song
/video
/find
/help
/about

πΏ Developer : @chamod_deshan

π₯ [π  zoneunlimited  π](https://t.me/Zu_Project) Corporation Β©οΈ
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β β° α΄α΄α΄ α΄α΄ α΄α΄ Ι’Κα΄α΄α΄ β± β", url=f"https://t.me/The_song_finder_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π  zoneunlimited  π", url=f"https://t.me/zoneunlimited"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π zoneunlimited chat π", url="https://t.me/zoneunlimitedchat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π·  Bot Developer  π·", url=f"https://t.me/chamod_deshan"
                    )
                ],
                [
                    InlineKeyboardButton(text=
                       "ββββββπ Search Here Song πββββββ", switch_inline_query_current_chat="new sinhala Dj song"
                    )
                ]
           ]
        )
    )

@app.on_message(filters.command("help"))
async def help(client, message):
    try:
        await message.reply_chat_action("typing")
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**βοΈ Access Denied βοΈ**\n\nπββοΈ **Hey There** {message.from_user.mention}, You Must **Join** @zoneunlimited Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Againπ€. **Thank** You π€", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
    )
        return
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "send you song name... π₯π\n /song (song name) π₯³"
    await message.reply(text)

OWNER_ID.append(1901997764)
app.start()
LOGGER.info("my music finder bot Is Now Successfully loaded β")
idle()
