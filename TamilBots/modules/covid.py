import requests, json
from pyrogram import Client, filters
from os import getenv
from TamilBots import app, LOGGER


# HPB API
response_API = requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
data = json.loads(response_API.text)
local_new_cases     = str(data['data']['local_new_cases'])
update_date_time    = str(data['data']['update_date_time'])
local_new_cases     = str(data['data']['local_new_cases'])
local_active_cases  = str(data['data']['local_active_cases'])
local_total_cases   = str(data['data']['local_total_cases'])
local_deaths        = str(data['data']['local_deaths'])
local_recovered     = str(data['data']['local_recovered'])
local_total_number_of_individuals_in_hospitals = str(data['data']['local_total_number_of_individuals_in_hospitals'])
global_new_cases    = str(data['data']['global_new_cases'])
global_total_cases  = str(data['data']['global_total_cases'])
local_new_deaths    = str(data['data']['local_new_deaths'])
global_deaths       = str(data['data']['global_deaths'])
global_new_deaths   = str(data['data']['global_deaths'])
global_recovered    = str(data['data']['global_recovered'])

covidinfo = f"""
ශ්‍රී ලංකාවේ කොරෝනා තත්වය. 🇱🇰
🔄 {update_date_time} ට යාවත්කාලීන කරන ලදී.
• නව රෝගීන් ගණන 😷 - {local_new_cases}
• නව මරණ ගණන ⚰ - {local_new_deaths}
• තහවුරු කරන ලද මුළු රෝගීන් ගණන 🤒 - {local_total_cases}
• තවමත් ප්‍රතිකාර ලබන රෝගීන් ගණන 🤕 - {local_active_cases}
• මේ වන විට සුව වූ කොරෝන රෝගීන් ගණන 🙂 - {local_recovered}
• මුළු මරණ සංඛ්‍යාව ⚰ - {local_deaths}
"""

# /gcovid command menu
gcovidinfo = f"""
සමස්ත ලෝකයේ කොරෝනා තත්වය. 🌎
🔄{update_date_time} ට යාවත්කාලීන කරන ලදී.
• නව රෝගීන් ගණන 😷 - {global_new_cases}
• නව මරණ ගණන ⚰ - {global_new_deaths}
• තහවුරු කරන ලද මුළු රෝගීන් ගණන 🤒 - {global_total_cases}
• මේ වන විට සුව වූ කොරෝන රෝගීන් ගණන 🙂 - {global_recovered}
• මුළු මරණ සංඛ්‍යාව ⚰ - {global_deaths}
"""

@app.on_message(filters.command("covid"))
async def covid(__, message):
    app.send_message(message.chat.id, covidinfo)
