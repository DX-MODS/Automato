import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from helper.utils import Automato
from config import Config

@Automato.on_message(filters.command(["json","js"], Config.PREFIX))
async def jsonify(_, message):
    the_real_message = None
    reply_to_id = None
    pk = InlineKeyboardMarkup([[InlineKeyboardButton(text="𝙲𝙻𝙾𝚂𝙴", callback_data="close_data")]])  
                
    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message

    try:        
        await message.reply_text(f"<code>{the_real_message}</code>", reply_markup=pk, quote=True)
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))       
        await message.reply_document(
            document="json.text",
            caption=str(e),
            disable_notification=True,
            quote=True,
            reply_markup=reply_markup
        )            
        os.remove("json.text")

