import asyncio
import requests
import aiohttp
from pyrogram import filters
from pyrogram.types import Message
from helper.utils import Automato


@Automato.on_message(filters.private & filters.command("neko"))
async def neko(client, message):
    text = client.reply_to_client.text
    try:
        params = {"content": text}
        headers = {'content-type' : 'application/json'}
        url = "https://nekobin.com/api/documents"
        neko = requests.post(url, json=params, headers=headers)
        key = neko.json()["result"]["key"]
    except Exception:
        await client.edit_text("`API is down try again later`")
        await asyncio.sleep(2)
        await client.delete()
        return
    else:
        url = f"https://nekobin.com/{key}"
        reply_text = f"**Pasted to: [Nekobin]({url})**"
        delete = (
            True
            if len(client.command) > 1
            and client.command[1] in ["d", "del"]
            and client.reply_to_client.from_user.is_self
            else False
        )
        if delete:
            await asyncio.gather(
                Automato.send_client(
                    client.chat.id, reply_text, disable_web_page_preview=True
                ),
                client.reply_to_client.delete(),
                client.delete(),
            )
        else:
            await client.edit_text(
                reply_text,
                disable_web_page_preview=True,
            )
