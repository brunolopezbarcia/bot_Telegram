from telegram import Update
import os
from telegram.ext import ContextTypes

async def install_package(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    package=update.message.text
    package_pre=package.split()
    if len(package_pre) >= 2:
        package_filtrado = package_pre[1]
        instalacion = os.system(f'apt update -y && apt install {package_filtrado} -y')
    else:
        await update.message.reply_text(f'No se ha indicado ningun paquete')

    if instalacion == 0:
        await update.message.reply_text(f'Se ha instalado el paquete: {package_filtrado}')
    else:
        await update.message.reply_text(f'No se ha instalado el paquete: {package_filtrado}')