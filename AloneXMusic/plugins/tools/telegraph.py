from telegraph import upload_file
from pyrogram import filters
from AloneXMusic import app


@app.on_message(filters.command('tgm'))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("Mᴀᴋɪɴɢ A Lɪɴᴋ Oғ Yᴏᴜʀ Dᴏᴄᴜᴍᴇɴᴛ Bᴀʙʏ....")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'𝐘ᴏᴜʀ 𝐓ᴇʟᴇɢʀᴀᴘʜ  {url}')
