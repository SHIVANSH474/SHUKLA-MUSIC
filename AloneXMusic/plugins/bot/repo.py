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
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/mastiwithfriendsx"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/ITSZ_SHIVANSH"),
          ],
               [
                InlineKeyboardButton("𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗡𝗘𝗧𝗪𝗢𝗥𝗞", url=f"https://t.me/STRANGER_LOGS"),

],

            
[
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://t.me/ITZ_MERADHIKABOT"),
InlineKeyboardButton("𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥", url=f"https://t.me/SHIVANSH39"),
],
[
              InlineKeyboardButton("𝗦𝗣𝗔𝗠 𝗕𝗢𝗧𝗦", url=f"https://t.me/FIGHTERS1234"),
              InlineKeyboardButton("𝗕𝗔𝗡𝗔𝗟𝗟", url=f"https://t.me/ll_Miss_Rose_bot"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚  𝗛𝗔𝗖𝗞 𝗕𝗢𝗧", url=f"https://t.me/@StrangerHackBot"),
InlineKeyboardButton("𝗨𝗦𝗘𝗥 𝗕𝗢𝗧", url=f"https://t.me/Shukla_op_clone1bot"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗥𝗢𝗕𝗢𝗧", url=f"https://t.me/StrangerSuperbot"),
InlineKeyboardButton("𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛", url=f"https://t.me/ABOUT_SHIVANSHOP"),
],
[
InlineKeyboardButton("𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗚𝗘𝗡 𝗕𝗢𝗧", url=f"https://t.me/StringSesssionGeneratorRobot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/70402820cd4afd8ea4c13.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
