from config import Config
from helper.db import db
from pyrogram.types import Message
from pyrogram import Client, filters
from helper.utils import Automato
@Automato.on_message(filters.command("users") & filters.user(Config.ADMIN))
async def get_stats(bot :Automato, message: Message):
    mr = await message.reply('**𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶 𝙳𝙴𝚃𝙰𝙸𝙻𝚂.....**')
    total_users = await db.total_users_count()
    await mr.edit( text=f"❤️‍🔥 TOTAL USER'S = `{total_users}`")
