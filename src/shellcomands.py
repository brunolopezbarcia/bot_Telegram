from telegram import Update
import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time


async def shell_comand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global package, instalacion

    shell_Comand=update.message.text
    shell_Comand_pre=shell_Comand
    if len(shell_Comand_pre) >= 2:
        comando = shell_Comand[6:]
        print(comando)

    comando_2 = os.system(f"{comando} > __.txt")
    
    f = open(f"__.txt")
    
    archivo = f.read()
    
    f.close()
    
    if comando_2 == 0:
        await update.message.reply_text("Ejecucion correcta si el comando devuelve algo sera el siguiente mensaje")
        await update.message.reply_text(archivo)
    else:
        await update.message.reply_text("Algo no ha ido bien 😬")
        await update.message.reply_video("/mnt/DiscoDuro/bot_Telegram/media/error.gif")
        

    os.system(f"rm -f __.txt")
    
    