from time import sleep, time



from pyrogram.types import Message, ChatPrivileges

from pyrogram import enums



from helper.utils import Automato





async def CheckAdmin(message: Message):

    """Check if we are an admin."""

    admin = "administrator"

    creator = "creator"

    ranks = [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]



    SELF = await Automato.get_chat_member(

        chat_id=message.chat.id, user_id=message.from_user.id

    )



    if SELF.status not in ranks:

        await message.edit("__I'm not Admin!__")

        sleep(2)

        await message.delete()



    else:

        if SELF.status is not enums.ChatMemberStatus.ADMINISTRATOR or SELF.privileges.can_restrict_members:

            return True

        else:

            await message.edit("__No Permissions to restrict Members__")

            sleep(2)

            await message.delete()
