import asyncio
import time
from datetime import datetime
from pyrogram import filters
from helper.start_time import StartTime
from sys import version_info
from helper.utils import Automato
from pyrogram.types import Message


__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"
__pyro_version__ = "2.0.106"

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Automato.on_message(filters.private & filters.command("alive"))
async def alive(_, m):
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg = f"**[Automato](https://github.com/DX-MODS/Automato)**\n"
    reply_msg += f"__Python__: `{__python_version__}`\n"
    reply_msg += f"__@Pyrogram version__: `{__pyro_version__}`\n"
    end_time = time.time()
    reply_msg += f"__Automato uptime__: {uptime}"
    photo = "https://graph.org/file/7ed4076ca07271fef389b.jpg"
    await m.delete()
    if m.reply_to_message:
        await Automato.send_photo(
            m.chat.id,
            photo,
            caption=reply_msg,
            reply_to_message_id=m.reply_to_message.id,
        )
    else:
        await Automato.send_photo(m.chat.id, photo, caption=reply_msg)

