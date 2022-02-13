import os
import requests
from pyrogram import Client, filters

@app.on_message(filters.command(["lyrics"]))
async def lirik(_, message):
    rep = await message.reply_text("🔎 **searching your lyrics...**")
    try:
        if len(message.command) < 2:
            await message.reply_text("**give a lyric name too !**")
            return
        query = message.text.split(None, 1)[1]
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"🎼 **lyrics  search Successfully**✅\n\n◇───────────────◇ `{resp['data']}´\n\n◇───────────────◇\n\n🔥**Downloaded by**:@szsongbot  \n🌷 **Requestor** : {message.from_user.username}\n⚡️ **Powered By**   : 【SZ™】\n\©2021【SZ™】 team  **All Right Reserved**⚠️️   "
        await message.reply_text(result, disable_web_page_preview=True)
        await rep.delete()
    except Exception as ex:
        print(ex)
        await rep.edit("**Lyrics not found.** please give a valid song name !")
