from helper.utils import Automato

from config import Config



from pyrogram import filters, Client

from pyrogram.types import Message



from helper.database.gmutedb import get_gmuted_users, gmute_user, ungmute_user

from helper.pyrohelper import get_arg

from helper.adminhelpers import CheckAdmin





@Automato.on_message(filters.command("gmute") & filters.me)

async def gmute(_, message):

    reply = message.reply_to_message

    if reply:

        user = reply.from_user.id

    else:

        user = get_arg(message)

        if not user:

            await message.edit("**Whome should I gmute?**")

            return

    get_user = await Automato.get_users(user)

    await gmute_user(get_user.id)

    await message.edit(f"**Gmuted {get_user.first_name}, LOL!**")





@Automato.on_message(filters.command("ungmute") & filters.me)

async def gmute(_, message):

    reply = message.reply_to_message

    if reply:

        user = reply.from_user.id

    else:

        user = get_arg(message)

        if not user:

            await message.edit("**Whome should I ungmute?**")

            return

    get_user = await Automato.get_users(user)

    await ungmute_user(get_user.id)

    await message.edit(f"**Unmuted {get_user.first_name}, enjoy!**")



async def check_prefix(filter, client: Client, message: Message):

    if(message.text and (message.text).startswith(PREFIX + PREFIX)):

        return True

    return False



@Automato.on_message(filters.me & filters.outgoing & filters.create(check_prefix))

async def change_cmd(client, message):

    await message.edit(f"`{message.text[1:]}`")



@Automato.on_message(filters.group & filters.incoming)

async def check_and_del(client, message):

    if not message:

        return

    try:

        if not message.from_user.id in (await get_gmuted_users()):

            return

    except AttributeError:

        return

    message_id = message.id

    try:

        await Automato.delete_messages(message.chat.id, message_id)

    except:

        pass  # you don't have delete rights
