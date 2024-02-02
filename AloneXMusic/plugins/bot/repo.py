from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneXMusic import app
from config import BOT_USERNAME

start_txt = """
✪ 𝗣𝗔𝗛𝗟𝗘 𝗝𝗔𝗞𝗘 𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛 𝗞𝗢 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟𝗢 𝗥𝗘𝗣𝗢 𝗠𝗜𝗟 𝗝𝗔𝗬𝗘𝗚𝗔 😎 ✪
 
 ➲𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗠𝗬 𝗣𝗢𝗪𝗘𝗥𝗙𝗨𝗟 𝗕𝗢𝗧 𝗟𝗜𝗦𝗧 ✰
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/mastiwithfriendsx"),
          InlineKeyboardButton("𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛", url="https://t.me/SHIVANSH39"),
          ],
               [
                InlineKeyboardButton("𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥-𝗨𝗣𝗗𝗔𝗧𝗦", url=f"https://t.me/SHIVANSH474"),

],

            
[
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://t.me/ITZ_MERADHIKABOT"),
InlineKeyboardButton("𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥-𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/Itz_SapnaMusicbot"),
],
[
              InlineKeyboardButton("𝗦𝗣𝗔𝗠 𝗕𝗢𝗧𝗦", url=f"https://t.me/FIGHTERS1234"),
              InlineKeyboardButton("𝗕𝗔𝗡𝗔𝗟𝗟", url=f"https://t.me/ll_Miss_Rose_bot"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚  𝗛𝗔𝗖𝗞 𝗕𝗢𝗧", url=f"https://t.me/StrangerHackBot"),
InlineKeyboardButton("𝗨𝗦𝗘𝗥 𝗕𝗢𝗧", url=f"https://t.me/Shukla_op_clone1bot"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗥𝗢𝗕𝗢𝗧", url=f"https://t.me/StrangerSuperbot"),
InlineKeyboardButton("𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥-𝗠𝗔𝗡𝗘𝗚𝗘𝗥", url=f"https://t.me/Melaniarobot"),
],
[
InlineKeyboardButton("𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗚𝗘𝗡 𝗕𝗢𝗧", url=f"https://t.me/StringSesssionGeneratorRobot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://te.legra.ph/file/8e779ca298fb47f368f2b.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
