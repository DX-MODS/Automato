from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.utils import Automato
from config import Config
import requests
from lyricsgenius import Genius 
import os


API = "https://apis.xditya.me/lyrics?song="

@Automato.on_message(filters.text & filters.command(["lyrics"], Config.PREFIX) & filters.private)
async def sng(bot, message):  
          genius = Genius(Config.GENIUS_API)        
          mee = await message.reply_text("`Searching`")
          try:
              song = message.text.split(None, 1)[1] #.lower().strip().replace(" ", "%20")
          except IndexError:
              await message.reply("give me a query eg `lyrics faded`")
          chat_id = message.from_user.id
    #      rpl = lyrics(song)
          songGenius = genius.search_song(song)
          rpl = songGenius.lyrics
          await mee.delete()
          try:
            await mee.delete()
            await message.reply(rpl)
          except Exception as e:                            
             await message.reply_text(f"lyrics does not found for `{song} {e}`") #", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url = f"https://t.me/dxmodsupdates")]]))
          finally:
            await message.reply("Check out @dxmodsupdates(Updates)  https://t.me/DXMODS_Support(Support)")



def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = fin["lyrics"]
        return text
