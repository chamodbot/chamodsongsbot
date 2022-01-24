from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """**
👋 hello There, [{}](tg://user?id={})
     
                 SSH CRETOR BOT 

🔥 This bot most advanced SSH CRETOR BOT

🍀 FRO SSH LOVERS ⚡️

◇───────────────◇

🏆 Automatically lyrics create (all lang.)

◇───────────────◇ 

🚀 inbox supported

◇───────────────◇ 

📡 sported fro group 

◇───────────────◇ 

🧿 more Fast creating

◇───────────────◇ 

🔗 24 Hour activet 

◇───────────────◇ 


◇───────────────◇

🍀 Developer @chamod_deshan


🔥 🍀 @zoneunlimited 🍀 Corporation ©️ **"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="➕    ADD TO GROUP     ➕ ", url="http://t.me/chamod_deshanbot?startgroup=true"),
            
            ],
            [
             InlineKeyboardButton(text="🍀 zoneunlimited 🍀", url="http://t.me/zoneunlimited")

            ],
            [InlineKeyboardButton(text="🍀 zoneunlimited chat 🍀", url="http://t.me/zoneunlimitedchat")
            
            ],
            [InlineKeyboardButton(text="🧿YOU  Tech🧿", url="https://t.me/YouTech_VPN_HUB")
            
            ],
            [InlineKeyboardButton(text="🌺 Subzero Ehi Team 🌺", url="https://t.me/subzeroehiteam")
        
            ],
            [InlineKeyboardButton(text="🌷 Developer 🌷", url="http://t.me/chamod_deshan"
               
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
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "send you song name... 🔥🚀\n /song (song name) 🥳"
    await message.reply(text)

OWNER_ID.append(1901997764)
app.start()
LOGGER.info("nikonemusicfinder Is Now Working🚀🔥🚀")
idle()
