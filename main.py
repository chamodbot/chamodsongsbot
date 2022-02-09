import asyncio
from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@app.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/740f6f319246b5e175bdb.jpg",
        caption=f"""**
🍀 hello There,
     
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
                        "🍀  zoneunlimited chat 🍀", url="https://t.me/zoneunlimitedchat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌷  Bot Developer  🌷", url=f"https://t.me/chamod_deshan"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧿  You Tech  🧿", url=f"https://t.me/YouTech_VPN_HUB"
                    )
                ],
                [  InlineKeyboardButton(text=
                       "◇────────🔍 Search Again 🔎───────◇", switch_inline_query_current_chat="")
                   
                ]
                
           ]
        ),
    )
    
    
@app.on_message(filters.command("start") & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/740f6f319246b5e175bdb.jpg",
        caption=f"""🍀 hello There,
     
                 🎧 MUSIC FINDER BOT 🎧

🔥 This bot most advanced nikone music finder bot,keyword search & also voice search sport 🔥

🍀 FRO MUSIC LOVERS ⚡️

◇───────────────◇

✅ Voice music search supported 🎤
🏵 keyword music search 
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
    
@app.on_message(command(["chalani", "tharushika"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/740f6f319246b5e175bdb.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://github.com/ITZ-ZAID/Zaid-Vc-Player")
                ]
            ]
        ),
    )
