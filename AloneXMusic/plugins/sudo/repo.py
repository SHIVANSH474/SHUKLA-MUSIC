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
    up_r = f"[𝗥𝗘𝗣𝗢]({config.UPSTREAM_REPO})"
    up_b = f"[𝗠𝗔𝗦𝗧𝗘𝗥]({config.UPSTREAM_BRANCH})"
    sp_c = f"[𓊈𒆜彡[𝐀ʟᴏɴᴇ 𝐍ᴇᴛᴡᴏʀᴋ]彡𒆜𓊉]({config.SUPPORT_CHANNEL})"
    sp_g = f"[𓊈𒆜彡[𝐀ʟᴏɴᴇ's 𝐇ᴇᴀᴠᴇɴ]彡𒆜𓊉]({config.SUPPORT_CHAT})"
    ow_i = f"[⏤͟͞ 𝐀 Ł ꪮ ɳ ᴇ ꭙ ˼ㅤ [•ᴧғᴋ•]™](https://t.me/ALONE_WAS_BOT)"

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
