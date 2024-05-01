from StringSessionBot.database.users_sql import Users, num_users
from StringSessionBot.database import SESSION
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(7087656547) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = await num_users()
    await msg.reply(f"Toplam Kullanıcı: {users}", quote=True)
