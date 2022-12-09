import asyncio
import os
import shutil
import time
import traceback

import imgbbpy
import pyromod.listen  # pylint: disable=unused-import
from pyrogram import Client, filters
from pyromod.helpers import ikb

from random import randint

from utils.configs import Tr, Var

Imgclient = imgbbpy.SyncClient(Var.API)

ext = tuple(
    [".jpg", ".png", ".jpeg", ".wepb", ".gif", ".bmp", ".heic", ".pdf", ".tif", ".webp"]
)


Img = Client(
    "ImgBB Bot",
    bot_token=Var.BOT_TOKEN,
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
)


START_BTN = ikb(
    [
        [
            ("👾 About", "about"),
            ("📚 Help", "help"),
        ],
        [
            ("❌", "close"),
        ],
    ]
)


HOME_BTN = ikb([[("🏠", "home"), ("❌", "close")]])
CLOSE_BTN = [("❌", "close")]


@Img.on_callback_query()
async def cdata(c, q):
    chat_id = q.from_user.id
    data = q.data
    wait = Tr.WAIT
    if data == "home":
        await q.answer(wait)
        await q.message.edit_text(
            text=Tr.START_TEXT.format(q.from_user.mention),
            reply_markup=START_BTN,
            disable_web_page_preview=True,
        )
    elif data == "help":
        await q.answer(wait)
        await q.message.edit_text(
            text=Tr.HELP_TEXT, reply_markup=HOME_BTN, disable_web_page_preview=True
        )
    elif data == "about":
        await q.answer(wait)
        await q.message.edit_text(
            text=Tr.ABOUT_TEXT,
            reply_markup=HOME_BTN,
            disable_web_page_preview=True,
        )

    elif data == "close":
        await q.message.delete(True)
        try:
            await q.message.reply_to_message.delete(True)
        except BaseException:
            pass


    elif data.startswith("del_"):
        num = data.split("_", 1)[1]

        await q.message.delete()

        if num == "0":
            exp = None
        else:
            exp = int(num)

        await q.answer(wait)

        r = q.message.reply_to_message
        rno = randint(100, 999)

        filename = f"Main-{rno}"

        if r.document:
            filename = f"Document-{rno}"
        elif r.photo:
            filename = f"Photo-{rno}"
        elif r.sticker:
            filename = f"Sticker-{rno}"
        elif r.animation:
            filename = f"Animation-{rno}"


        tmp = os.path.join("downloads", str(chat_id))
        if not os.path.isdir(tmp):
            os.makedirs(tmp)

        dwn = await q.message.reply_text(
            "✅ Downloading ...",
            True,
        )

        img_path = await r.download()
        await dwn.edit_text("⭕ Uploading ...")
        await dwn.delete()
        try:
            image = Imgclient.upload(file=img_path, expiration=exp, name=filename)
        except Exception as error:
            traceback.print_exc()
            await q.message.reply(
                f"⚠️ Ops, Something Went Wrong!\n\n**•Log: ** {error}"
            )
            return

        done = f"""
🔗 LINK : <code>{image.url}</code>

📝 FILENAME : {image.filename}

💾 SIZE : {HumanBytes(image.size)}

⚠️ DELETE URL : <code>{image.delete_url}</code>

⏳ EXPIRATION : {SecondsToText(int(image.expiration))}
"""
        imgkb = ikb(
            [
                [
                    ("🔗 Open", image.url, "url"),
                    ("⚠️ Delete", image.delete_url, "url"),
                ],
                [
                    ("❌", "close"),
                ],
            ]
        )

        await q.message.reply(done, disable_web_page_preview=True, reply_markup=imgkb, parse_mode='HTMl')
        shutil.rmtree(tmp, ignore_errors=True)

    else:
        await q.message.delete()


@Img.on_message(filters.private & filters.command(["start"]))
async def start(c, m):
    chat_id = m.from_user.id
    user = await c.get_users(int(chat_id))
    await m.reply_photo(
        photo=Var.START_PIC,
        caption=Tr.START_TEXT.format(m.from_user.mention),
        reply_markup=START_BTN,
        quote=True,
    )




@Img.on_message(
    filters.private
    & (filters.photo | filters.sticker | filters.document | filters.animation)
)
async def getimglink(c, m):
    chat_id = m.from_user.id
    user = await c.get_users(int(chat_id))

    if not Var.API:
        return await m.reply_text(
            Tr.ERR_TEXT,
            quote=True,
        )

    if m.document:
        if not m.document.file_name.endswith(ext):
            return
    await m.reply_chat_action("typing")
    BTN = ikb(
        [
            [
                ("▫️ 5 Minutes", "del_300"),
                ("▫️ 15 Minutes", "del_900"),
                ("▫️ 30 Minutes ", "del_1800"),
            ],
            [
                ("▪️ 1 Hour", "del_3600"),
                ("▪️ 2 Hours", "del_7200"),
                ("▪️ 6 Hours ", "del_21600"),
                ("▪️ 12 Hours ", "del_43200"),
            ],
            [
                ("◽ 1 Day", "del_86400"),
                ("◽ 2 Days", "del_172800"),
                ("◽ 3 Days", "del_259200"),
            ],
            [
                ("◾ 1 week", "del_604800"),
                ("◾ 2 Weeks", "del_1209600"),
                ("◾ 1 Month", "del_2629800"),
                ("◾ 2 Months", "del_5259600"),
            ],
            [
                ("◻ Don't AutoDelete ◼", "del_0"),
            ],
            [
                ("❌", "close"),
            ],
        ]
    )

    await m.reply_text(
        "🗑 AutoDelete ? ...",
        reply_markup=BTN,
        quote=True,
    )




def HumanBytes(size):
    if not size:
        return ""
    power = 2 ** 10
    n = 0
    Dic_powerN = {0: " ", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + "B"


def SecondsToText(secs):
    days = secs // 86400
    hours = (secs - days * 86400) // 3600
    minutes = (secs - days * 86400 - hours * 3600) // 60
    seconds = secs - days * 86400 - hours * 3600 - minutes * 60
    result = (
        ("{0} Day{1}, ".format(days, "s" if days != 1 else "") if days else "")
        + ("{0} Hour{1}, ".format(hours, "s" if hours != 1 else "") if hours else "")
        + (
            "{0} Minute{1}, ".format(minutes, "s" if minutes != 1 else "")
            if minutes
            else ""
        )
        + (
            "{0} Second{1}, ".format(seconds, "s" if seconds != 1 else "")
            if seconds
            else ""
        )
    )
    return result


Img.run()
