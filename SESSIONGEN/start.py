from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID

# Renaming the filter function to avoid conflict with built-in names
def command_filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(command_filter("start"))
async def start(bot: Client, msg: Message):
    me = (await bot.get_me()).mention  # Changed variable name to avoid shadowing built-in function name 'me'
    await msg.reply_text(
        text=f"""MERHABA {msg.from_user.mention},

๏ ben {me},
𝗉𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝗒𝖺𝗋𝖽ı𝗆ı𝗒𝗅𝖺 𝗉𝗒𝗍𝗁𝗈𝗇 𝗂𝗅𝖾 𝗒𝖺𝗓ı𝗅𝗆ış 𝖺çı𝗄 𝗄𝖺𝗒𝗇𝖺𝗄𝗅ı 𝖻𝗂𝗋 𝖽𝗂𝗓𝖾 𝗈𝗍𝗎𝗋𝗎𝗆 𝗈𝗅𝗎ş𝗍𝗎𝗋𝗎𝖼𝗎 𝖻𝗈𝗍𝗎 kurucu @Patronby63 
ᴍᴀᴅᴇ ʙʏ: [kumsal team](https://t.me/gecemavisisohbett) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="💫𝙊𝙩𝙪𝙧𝙪𝙢 𝙤𝙡𝙪ş𝙩𝙪𝙧💫", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("💫𝙨𝙖𝙝𝙞𝙗𝙞💫", url="https://t.me/Patronby63"),
                    InlineKeyboardButton("💫𝙠𝙖𝙮𝙣𝙖𝙠 𝙠𝙤𝙙💫", url="https://github.com/kumsalfed5456/STR-NG-OTURUM-")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
