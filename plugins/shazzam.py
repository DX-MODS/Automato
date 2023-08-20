# Copyright (C) 2023 DX_MODS
#Licensed under the MIT License;
#you may not use this file except in compliance with the License.
#Author ZIYAN

from __future__ import unicode_literals 
from os import environ,execl
from sys import executable
from pyrogram.errors import FloodWait 
from pyrogram.types import Message , InlineKeyboardMarkup, InlineKeyboardButton ,CallbackQuery
from pyrogram.errors import FloodWait 
from asyncio import sleep
from shazamio import Shazam
import asyncio
import time
import os
from requests import get
from helper.functions.util import run_cmd as runcmd
import datetime
from json import JSONDecodeError
import requests
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import yt_dlp
import requests
from typing import Tuple
from pyrogram import filters
from pyrogram import Client

import time
from helper.functions.shazzam import humanbytes, edit_or_reply, fetch_audio
NOT_SUPPORT = [ ]

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])
#@sync_to_async
def thumb_down(album_id,img):
    with open(f"/tmp/thumbnails/{album_id}.jpg","wb") as file:
        file.write(get(img).content)
    return f"/tmp/thumbnails/{album_id}.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


async def shazam(file):
    shazam = Shazam()
    try:
        r = await shazam.recognize_song(file)
    except:
        return None, None, None
    if not r:
        return None, None, None
    track = r.get("track")
    nt = track.get("images")
    image = nt.get("coverarthq")
    by = track.get("subtitle")
    title = track.get("title")
    return image, by, title

async def convert_to_audio(vid_path):
    stark_cmd = f"ffmpeg -i {vid_path} -map 0:a friday.mp3"
    await runcmd(stark_cmd)
    final_warner = "friday.mp3"
    if not os.path.exists(final_warner):
        return None
    return final_warner

@Client.on_message(filters.command(["find","shazzam"], Config.PREFIX))
async def shazam_(client, message):
    stime = time.time()
    msg = await message.reply_text("`𝚂𝚑𝚊𝚣𝚊𝚖𝚒𝚗𝚐 𝚃𝚑𝚒𝚜 𝚂𝚘𝚗𝚐.")
    if not message.reply_to_message:
        return await msg.edit("`𝚁𝚎𝚙𝚕𝚢 𝚃𝚘 𝚂𝚘𝚗𝚐 𝙵𝚒𝚕𝚎`")
    if not (message.reply_to_message.audio or message.reply_to_message.voice or message.reply_to_message.video):
        return await msg.edit("`𝚁𝚎𝚙𝚕𝚢 𝚃𝚘 𝙰𝚞𝚍𝚒𝚘 𝙵𝚒𝚕𝚎.`")
    if message.reply_to_message.video:
        video_file = await message.reply_to_message.download()
        music_file = await convert_to_audio(video_file)
        dur = message.reply_to_message.video.duration
        if not music_file:
            return await msg.edit("`𝚄𝚗𝚊𝚋𝚕𝚎 𝚃𝚘 𝙲𝚘𝚗𝚟𝚎𝚛𝚝 𝚃𝚘 𝚂𝚘𝚗𝚐 𝙵𝚒𝚕𝚎. 𝙸𝚜 𝚃𝚑𝚒𝚜 𝙰 𝚅𝚊𝚕𝚒𝚍 𝙵𝚒𝚕𝚎?`")
    elif (message.reply_to_message.voice or message.reply_to_message.audio):
        dur = message.reply_to_message.voice.duration if message.reply_to_message.voice else message.reply_to_message.audio.duration
        music_file = await message.reply_to_message.download()
    size_ = humanbytes(os.stat(music_file).st_size)
    dur = datetime.timedelta(seconds=dur)
    thumb, by, title = await shazam(music_file)
    if title is None:
        return await msg.edit("`𝙽𝚘 𝚁𝚎𝚜𝚞𝚕𝚝𝚜 𝙵𝚘𝚞𝚗𝚍.`")
    etime = time.time()
    t_k = round(etime - stime)
    caption = f"""<b><u>𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚎𝚍 𝙱𝚢 @AutomatoDxbot</b></u>
    
<b>Song Name :</b> <code>{title}</code>
<b>Singer :</b> <code>{by}</code>
<b>Duration :</b> <code>{dur}</code>
<b>Size :</b> <code>{size_}</code>
<b>Time Taken :</b> <code>{t_k} Seconds</code>

<b><u>𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚎𝚍 𝙱𝚢 @AutomatoDxbot</b></u>
    """
    if thumb:
        await msg.delete()
        await message.reply_to_message.reply_photo(thumb, caption=caption, quote=True)
    else:
        await msg.edit(caption)
    os.remove(music_file)
    if thumb:
       os.remove(thumb)
