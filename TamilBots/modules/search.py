import json

from pyrogram import Client, filters
from pyrogram.types import Message
from TamilBots import app, LOGGER
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from youtube_search import YoutubeSearch

@app.on_message(filters.command("search")) 
async def ytsearch(_, message: Message):
    
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🚫  Close  🚫", callback_data="close",
                )
            ]
        ]
    )
    
    try:
        if len(message.command) < 2:
            await message.reply("**😶 Oops Not Found !!...**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("████████████", callback_data="convert")]]), reply_to_message_id = message.message_id)
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply("**🎵 Searching In YouTube ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("░░░░░░░░░░░░", callback_data="convert")]]), reply_to_message_id = message.message_id)
        await m.edit("**🎵 Searching In YouTube ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("███████░░░░░", callback_data="convert")]]))
        await m.edit("**🎵 Searching In YouTube ....**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("████████████", callback_data="convert")]]))
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"🎵 **Name:** __{results[i]['title']}__\n"
            text += f"🌷 **Duration:** `{results[i]['duration']}`\n"
            text += f"👀 **Views:** `{results[i]['views']}`\n"
            text += f"🚀 **Channel:** {results[i]['channel']}\n"
            text += f"🔗: https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, reply_markup=keyboard, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))
