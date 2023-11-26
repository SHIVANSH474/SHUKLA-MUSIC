from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneXMusic import app
from config import BOT_USERNAME

start_txt = """
✪ 𝐖εℓ¢σмє 𝐅σя 𝐀ℓσиє 𝐑єρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/AlonesHeaven"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/ALONE_WAS_BOT"),
          ],
               [
                InlineKeyboardButton("𝗔𝗟𝗢𝗡𝗘 𝗡𝗘𝗧𝗪𝗢𝗥𝗞", url=f"https://t.me/AloneXBots"),

],
[
              InlineKeyboardButton("𝗩1 𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/TeamAloneOp/AloneX"),
              InlineKeyboardButton("𝗩2 𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/TeamAloneOp/AloneXMusic"),
              ],
              [
              InlineKeyboardButton("𝗩1 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧", url=f"https://github.com/TeamAloneOp/AloneXRobot"),
InlineKeyboardButton("𝗩2 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧", url=f"https://github.com/TeamAloneOp/AloneRobot"),
],
[
InlineKeyboardButton("𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡 𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/TeamAloneOp/Telethon-Music"),
InlineKeyboardButton("𝗔𝗟𝗢𝗡𝗘 𝗬𝗨𝗞𝗞𝗜", url=f"https://github.com/TeamAloneOp/AloneMusicBot"),
],
[
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/TeamAloneOp/AloneXChatBot"),
InlineKeyboardButton("𝗜𝗗 𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/TeamAloneOp/AloneXIdChatbot"),
],
[
              InlineKeyboardButton("𝗦𝗣𝗔𝗠", url=f"https://github.com/TeamAloneOp/AloneXSpam"),
              InlineKeyboardButton("𝗕𝗔𝗡𝗔𝗟𝗟", url=f"https://github.com/TeamAloneOp/AloneXBanallBot"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://github.com/TeamAloneOp/AloneXStringGenBot"),
InlineKeyboardButton("𝗕𝗬𝗣𝗔𝗦𝗦", url=f"https://github.com/TeamAloneOp/AloneXBypass"),
],
[
InlineKeyboardButton("𝗥𝗪 𝗦𝗧𝗥𝗜𝗣𝗘", url=f"https://github.com/TeamAloneOp/kaali-Linux"),
InlineKeyboardButton("𝗥𝗪 𝗗𝗘𝗣𝗟𝗢𝗬", url=f"https://github.com/TeamAloneOp/AloneXRailway"),
],
[
InlineKeyboardButton("𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗕𝗢𝗧", url=f"https://t.me/AloneXMusicBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/70402820cd4afd8ea4c13.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
