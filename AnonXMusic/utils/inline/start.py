from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=" Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⛦",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=" Hᴇʟᴩ ",
                callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text=" Sᴇᴛᴛɪɴɢs ", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="+ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ +",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴩ", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="Sᴜᴩᴩᴏʀᴛ", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="Oᴡɴᴇʀ", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="[❄️] Iɴᴛʀᴏᴅᴜᴄᴛɪᴏɴ [❄️]", url=config.GITHUB_REPO
            )
        ],
     ]
    return buttons
