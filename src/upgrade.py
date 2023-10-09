from telegram import Update
import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def upgrade_system(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global package, instalacion
    
    await update.message.reply_text(f'Trabajando en ello.....')
    await update.message.reply_video("/mnt/DiscoDuro/bot_Telegram/media/working_on_it.gif")
    upgrade = os.system(f'apt update -y && apt upgrade -y')

    if upgrade == 0:
        await update.message.reply_text(f'Se ha upgradeado el sistema')
    else:
        await update.message.reply_text(f'No se ha upgradeado el sistema')