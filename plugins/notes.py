from pyrogram import filters



from helper.utils import Automato, CMD_HELP

from helper.pyrohelper import get_arg

import helper.database.notesdb as Auto
from config import Config



CMD_HELP.update(

    {

        "Notes": """

『 **Notes** 』

  `save` -> Save a new note. Must be used in reply with one parameter (note name).

  `get` -> Gets the note specified.

  `clear` -> Deletes a note, specified by note name.

  `clearall` -> Deletes all the saved notes.

  `notes` -> List the saved notes.

"""

    }

)



LOG_CHANNEL = Config.LOG_CHANNEL





@Automato.on_message(filters.command("save", Config.PREFIX) & filters.me)

async def save(client, message):

    arg = get_arg(message)

    if not arg:

        await message.edit("**You must give a name for a note.**")

        return

    note_name = arg

    note = await Auto.get_note(note_name)

    if note:

        await message.edit(f"**Note `{note_name}` already exists**")

        return

    reply = message.reply_to_message

    if not reply:

        await message.edit("Reply to a message to save a note")

        return

    copy = await Automato.copy_message(LOG_CHANNEL, message.chat.id, reply.id)

    await Auto.save_note(note_name, copy.id)

    await message.edit("**Note saved**")





@Automato.on_message(filters.command("get", Config.PREFIX) & filters.me)

async def get(client, message):

    arg = get_arg(message)

    if not arg:

        await message.edit("Get what?")

        return

    note_name = arg

    note = await Auto.get_note(note_name)

    if not note:

        await message.edit(f"**Note {note_name} dosen't exists**")

        return

    if message.reply_to_message:

        await Automato.copy_message(

            message.chat.id,

            LOG_CHANNEL,

            note,

            reply_to_message_id=message.reply_to_message.id,

        )

    else:

        await Automato.copy_message(message.chat.id, LOG_CHANNEL, note)

    await message.delete()





@Automato.on_message(filters.command("clear", Config.PREFIX) & filters.me)

async def clear(client, message):

    arg = get_arg(message)

    if not arg:

        await message.edit("What do you want to delete?")

        return

    note_name = arg

    note = await Auto.get_note(note_name)

    if not note:

        await message.edit(f"**Failed to delete note `{note_name}`**")

        return

    await Auto.rm_note(note_name)

    await message.edit(f"**Succesfully deleted note `{note_name}`**")





@Automato.on_message(filters.command("notes", Config.PREFIX) & filters.me)

async def notes(client, message):

    msg = "**Saved Notes**\n\n"

    all_notes = await Auto.all_notes()

    if not all_notes:

        await message.edit("**No notes has been saved**")

        return

    for notes in all_notes:

        msg += f"◍ `{notes}`\n"

    await message.edit(msg)





@Automato.on_message(filters.command("clearall", Config.PREFIX) & filters.me)

async def clearall(client, message):

    await Auto.rm_all()

    await message.edit("**Removed all saved notes**")
