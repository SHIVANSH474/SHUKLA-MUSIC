import asyncio

from pyrogram import filters

import config
from AloneXMusic import app
from AloneXMusic.utils.formatters import convert_bytes





@app.on_message(filters.command("repo"))
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.."
    )
    up_r = f"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x67\x69\x74\x68\x75\x62\x2E\x63\x6F\x6D\x2F\x54\x65\x61\x6D\x41\x6C\x6F\x6E\x65\x4F\x70\x2F\x41\x6C\x6F\x6E\x65\x58\x4D\x75\x73\x69\x63"

 ##############
 
    text = f"""𝗔𝗟𝗢𝗡𝗘 𝗠𝗨𝗦𝗜𝗖 𝗥𝗘𝗣𝗢⌫

    
<u>𝗖𝗥𝗘𝗗𝗜𝗧 ❥︎𝗠𝗥 𝗔𝗟𝗢𝗡𝗘:</u>

𝗥𝗘𝗣𝗢 ❥︎ {up_r}

    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
