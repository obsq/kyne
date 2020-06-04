
import sys
from telethon import events, functions, __version__
from userbot import CMD_HELP
from userbot.events import kyne3301
from userbot.events import obsq, command
from userbot import bot as kyne

from userbot import CMD_HELP, ALIVE_NAME, PM_MESSAGE, KYNE_NAME, KYNE_MSG, ORI_MSG
KYNE_NNAME = str(KYNE_NAME) if KYNE_NAME else str(KYNE_MSG)
 
tgbotusername = var.TG_BOT_USER_NAME_BF_HER
@kyne3301(outgoing=True, pattern="^!help(?: |$)(.*)")
async def help(event):
    """ For !help command"""
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        args = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_HELP:
                string += "🛡 " + i + "\n"
                for iter_list in CMD_HELP[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await borg.send_message(event.chat_id, "Do !help cammand")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_HELP:
                string = "Commands found in {}:\n".format(input_str)
                for i in CMD_HELP[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(args + " is not a valid plugin!")
        else:
            help_string = f"`{KYNE_NNAME} :` --HELP MODULE-- "
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername,
                help_string
            )
            await results[0].click(
                event.chat_id,
                reply_to=event.reply_to_msg_id,
                hide_via=True
            )
            await event.delete()

          
        
 




@kyne.on(obsq(pattern=f"help(?: |$)(.*)", allow_sudo=True))
async def help(event):
    """ For .help command,"""
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        args = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_HELP:
                string += "🛡 " + i + "\n"
                for iter_list in CMD_HELP[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await borg.send_message(event.chat_id, "Do !help cammand")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_HELP:
                string = "Commands found in {}:\n".format(input_str)
                for i in CMD_HELP[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(args + " is not a valid plugin!")
        else:
            help_string = f"`{KYNE_NNAME} :` --HELP MODULE-- "
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername,
                help_string
            )
            await results[0].click(
                event.chat_id,
                reply_to=event.reply_to_msg_id,
                hide_via=True
            )
            await event.delete()






        
CMD_HELP.update({
    "admin":
    "!promote <username/reply/userid> <custom name>\
\nUsage: Provides admin rights to the person in the chat.\
\n\n!demote <username/reply/userid>\
\nUsage: Revokes the person's admin permissions in the chat.\
\n\n!ban <reply> <reason (optional)>\
\nUsage: Bans the person off your chat.\
\n\n!unban <username/reply/userid>\
\nUsage: Removes the ban from the person in the chat.\
\n\n!mute <username/reply/userid> <reason (optional)>\
\nUsage: Mutes the person in the chat, works on admins too.\
\n\n!warn <reply to a message > <reason (optional)>\
\nUsage: warn the person\
\n\n!resetwarns <reply to a user > \
\nUsage: reset the target person's warns\
\n\n!warns <reply to a user > \
\nUsage: get warnings of the targeted person\
\n\n!unmute <username/reply/userid>\
\nUsage: Removes the person from the muted list.\
\n\n!gban <username/reply/userid> <reason (optional)>\
\nUsage: Ban the person in all groups you have in common with them. and block user in your pm too!\
\n\n!unban <username/reply/userid>\
\nUsage: Reply someone's message with !ungban to remove them from the gban list.\
\n\n!delusers\
\nUsage: Searches for deleted accounts in a group. Use !delusers clean to remove deleted accounts from the group.\
\n\n!admins\
\nUsage: Retrieves a list of admins in the chat.\
\n\n!bots\
\nUsage: Retrieves a list of bots in the chat.\
\n\n!users  <Retrieves a list of members in the chat.>\
\nUsage: Retrieves all (or queried) users in the chat.\
\n\n!pin <reply to message>\
\nUsage: Changes the group's display picture.\
\n\n!setgpic <reply to image>\
\nUsage: Changes the group's display picture."
})


CMD_HELP.update({
    "notes":
    "\
#<notename>\
\nUsage: Gets the specified note.\
\n\n!savenote <notename> <notedata> or reply to a message with !savenote <notename>\
\nUsage: Saves the replied message as a note with the notename. (Works with pics, docs, and stickers too!)\
\n\n!checknote\
\nUsage: Gets all saved notes in a chat.\
\n\n!clearnote <notename>\
\nUsage: Deletes the specified note."
})



CMD_HELP.update({
    "api":
    "\
you must add api keys else these commands not work\
\n\n!read reply to a photo \
\nUsage: read texts in photo\
\n\n!auto\
\nUsage: javes start to auto reply user(lydia).\
\n\n!offauto\
\nUsage: Stop auto reply.\
\n\n!lydia reply to a msg\
\nUsage: auto reply about taged message\
\n\n!rbg reply to a img\
\nUsage: Remove background from img\
\n\n!weather <country> or <city>\
\nUsage: get full weather details\
\n\n!youtube <word>\
\nUsage: Do youtube search\
"
})

CMD_HELP.update({
    "welcome":
    "\
!savewelcome reply to a message with !savewelcome\
\nUsage: Saves the message as a welcome note in the chat.\
\n\nAvailable variables for formatting welcome messages :\
\n`{mention}, {title}, {count}, {first}, {last}, {fullname}, {userid}, {username}, {my_first}, {my_fullname}, {my_last}, {my_mention}, {my_username}`\
\n\n!checkwelcome\
\nUsage: Check whether you have a welcome note in the chat.\
\n\n!clearwelcome\
\nUsage: Deletes the welcome note for the current chat.\
"
})

CMD_HELP.update({
    "locks":
    "!lock <all (or) type(s)> or !unlock <all (or) type(s)>\
\nUsage: Allows you to lock/unlock some common message types in the chat.\
[NOTE: Requires proper admin rights in the chat !!]\
\n\nAvailable message types to lock/unlock are: \
\n`all, msg, media, sticker, gif, game, inline, poll, invite, pin, info`"
})


CMD_HELP.update({
    "chat":
    "!chatid\
\nUsage: Fetches the current chat's ID\
\n\n!userid\
\nUsage: Fetches the ID of the user in reply, if its a forwarded message, finds the ID for the source.\
\n\n!chatinfo\
\nUsage: Fetches the group's info\
\n\n!log\
\nUsage: Forwards the message you've replied to in your bot logs group.\
\n\n!invite\
\nUsage: !invite <username> invite the user to the group.\
\n\n!kickme\
\nUsage: Leave from a targeted group.\
\n\n!link <username/userid> : <optional text> (or) reply to someone's message with !link <optional text>\
\nUsage: Generate a permanent link to the user's profile with optional custom text."
})

CMD_HELP.update({
    "filter":
    "!checkfilter\
    \nUsage: Lists all active userbot filters in a chat.\
    \n\n!savefilter reply to a message with !savefilter <keyword>\
    \nUsage: Saves the replied message as a reply to the 'keyword'.\
    \nThe bot will reply to the message whenever 'keyword' is mentioned.\
    \nWorks with everything from files to stickers.\
    \n\n!clearfilter <filter>\
    \nUsage: Stops the specified filter. \
    \n\n!clearallfilter \
    \nUsage: Stops all filters.\
    \n\n!savefilter2 ,  !checkfilter2,  clearfilter2\
    \nUsage: same like filter "
})


CMD_HELP.update({
    "stickers":
    "!kang\
\nUsage: Reply !kang to a sticker or an image to kang it to your userbot pack.\
\n\n!kang [emoji('s)]\
\nUsage: Works just like !kang but uses the emoji('s) you picked.\
\n\n!kang [number]\
\nUsage: Kang's the sticker/image to the specified pack \
\n\n!kang [emoji('s)] [number]\
\nUsage: Kang's the sticker/image to the specified pack and uses the emoji('s) you picked.\
\n\n!stickerinfo\
\nUsage: Gets info about the sticker pack.\
\n\n!ss\
\nUsage: convert user text to sticker like a sticker screenshot\
\n\n!ss2\
\nUsage: Convert picture to sticker\
\n\n!text\
\nUsage: text to sticker\
\n\n!text2\
\nUsage: same like !text but can use custom fonts like !text font | message ex -  !text2 font | lol \
\n\n!fry\
\nUsage: make given image funny\
"
})


CMD_HELP.update({
    "beta":
    "!mail\
\nUsage: Create a fake  main and list it \
\n\n!ushort \
\nUsage: shorten the url.\
\n\n!song2\
\nUsage: find the target song \
\n\n!lyrics2 [emoji('s)] [number]\
\nUsage: get lyrics of song\
\n\n!mask\
\nUsage: make mask for tagged photo/sticker\
"
})






CMD_HELP.update({
    "blacklist":
    "!checkblacklist\
    \nUsage: Lists all active userbot blacklists in a chat.\
    \n\n!saveblacklist <keyword> <reply text> or reply to a message with !saveblacklist <keyword>\
    \nUsage: Delete then non admins blacklisted wards.\
    \n\n!clearblacklist <ward>\
    \nUsage: Stops the specified blacklist ward."
})


CMD_HELP.update({
    "sudo":
    "if you active sudo , sudo users can controll your javes like you controll groupmanaging bots\
    \nyou can active sudo by !set var SUDO_USERS <your sudo user's id>\
    \n\nyou can active multiple sudo users by space \
    \ncheck sudo by .sudo in sudo user's accoint\
    \n(!) command for bot owner , (.) command for sudo users like !ban for owner , .ban for sudo users\
"
})




CMD_HELP.update({
    "others":
    "comming soon!\
    \n you can see other help commands in @kyne3301 for now\
"
})
