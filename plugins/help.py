from pyrogram import filters
from helper.utils import Automato, HELP, CMD_HELP
from config import Config
from helper.pyrohelper import get_arg
HELP = {}
CMD_HELP = {}
HELP.update(
    {
        "**Admin Tools**": "__ban, unban, promote, demote, kick, mute, unmute, gmute, ungmute, pin, purge, del, invite__",
        "**AFK**": "__afk, unafk__",
        "**Alive**": "__alive, ping__",
        "**Developer**": "__eval, term, log__",
        "**Filters**": "__filter, filters, stop, stopall__",
        "**Misc**": "__paste, whois, id__",
        "**Notes**": "__save, get, clear, clearall, notes__",
        "**Anti-PM**": "__pmguard, setpmmsg, setlimit, setblockmsg, allow, deny__",
        "**Sticker**": "__kang, stkrinfo__",
        "**Greetings**": "__setwelcome, clearwelcome__",
    }
)


@Automato.on_message(filters.private & filters.command("help"))
async def help(client, message):
    args = get_arg(message)
    if not args:
        text = "**Available Commands**\n\n"
        for key, value in HELP.items():
            text += f"{key}: {value}\n\n"
        await message.edit(text)
        return
    else:
        module_help = CMD_HELP.get(args, False)
        if not module_help:
            await message.edit("__Invalid module name specified.__")
            return
        else:
            await message.edit(module_help)
