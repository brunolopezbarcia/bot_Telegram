from telegram import Update
import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start_pc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text(f'Trabajando en ello.....')
    await update.message.reply_video("/mnt/DiscoDuro/bot_Telegram/media/working_on_it.gif")
    start_pc_var = os.system(f'etherwake 5C:60:BA:33:43:18')

    if start_pc_var == 0:
        await update.message.reply_text(f'Se ha encendido el equipo')
    else:
        await update.message.reply_text(f'No se ha encendido el equipo😞')
        await update.message.reply_video("/mnt/DiscoDuro/bot_Telegram/media/error.gif")