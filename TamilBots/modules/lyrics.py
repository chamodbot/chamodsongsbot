import os
import requests
from pyrogram import Client, filters
from TamilBots import app, LOGGER

@app.on_message(filters.command("lyrics"))
async def lyrics(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("» **give a lyric name too.**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("🔎 **searching lyrics...**")
        resp = requests.get(
            f"https://api-tede.herokuapp.com/api/lirik?l={query}"
        ).json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("❌ **lyrics not found.**\n\n» **please give a valid song name.**")
