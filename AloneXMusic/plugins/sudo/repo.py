import asyncio

from pyrogram import filters

import config
from AloneXMusic import app
from AloneXMusic.misc import SUDOERS
 
from AloneXMusic.utils.formatters import convert_bytes





@app.on_message(filters.command(["repo"]) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.."
    )
    up_r = f"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x67\x69\x74\x68\x75\x62\x2E\x63\x6F\x6D\x2F\x54\x65\x61\x6D\x41\x6C\x6F\x6E\x65\x4F\x70\x2F\x41\x6C\x6F\x6E\x65\x58\x4D\x75\x73\x69\x63"
    up_b = config.UPSTREAM_BRANCH
    sp_c = f"https://t.me/AloneXBots"
    sp_g = f"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x6C\x6F\x6E\x65\x73\x48\x65\x61\x76\x65\x6E"
    ow_i = f"[⏤͟͞ 𝐀 Ł ꪮ ɳ ᴇ ꭙ ˼ㅤ [•ᴧғᴋ•]™](\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x4C\x4F\x4E\x45\x5F\x57\x41\x53\x5F\x42\x4F\x54)"

 ##############
 
    text = f"""𝗔𝗟𝗢𝗡𝗘 𝗠𝗨𝗦𝗜𝗖 𝗥𝗘𝗣𝗢⌫

    
<u>𝗖𝗥𝗘𝗗𝗜𝗧 ❥︎𝗠𝗥 𝗔𝗟𝗢𝗡𝗘:</u>

𝗥𝗘𝗣𝗢 ❥︎ {up_r}

𝗕𝗥𝗔𝗡𝗖𝗘 ❥︎ {up_b}

𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ❥︎ {sp_c}

𝗚𝗥𝗢𝗨𝗣 ❥︎ {sp_g}

𝗢𝗪𝗡𝗘𝗥 ❥︎ {ow_i}

    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
