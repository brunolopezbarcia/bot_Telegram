import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from start_pc import start_pc

from upgrade import upgrade_system
from shellcomands import shell_comand

dotenv_path = Path('../constants/.env')
load_dotenv(dotenv_path=dotenv_path)

API = os.getenv('API_BOT')

print(API)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def install_package(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global package, instalacion
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

async def uninstall_package(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global package, instalacion
    package=update.message.text
    package_pre=package.split()
    if len(package_pre) >= 2:
        package_filtrado = package_pre[1]
        instalacion = os.system(f'apt update -y && apt autopurge {package_filtrado} -y')
    else:
        await update.message.reply_text(f'No se ha indicado ningun paquete')

    if instalacion == 0:
        await update.message.reply_text(f'Se ha desintalado el paquete: {package_filtrado}')
    else:
        await update.message.reply_text(f'No se ha desintalado el paquete: {package_filtrado}')


async def estado(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cpu = subprocess.Popen('sensors' , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time = subprocess.Popen('date', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output_time, err_time = time.communicate()
    output, err = (cpu.communicate())
    cadena = output_time
    cadena_texto = cadena.decode('utf-8')
    palabras = cadena_texto.split()
    fecha = ' '.join(palabras[1:5])
    texto_bytes = output
    texto = texto_bytes.decode('utf-8')

    lineas = texto.split('\n')

    temperatura_linea = None
    for linea in lineas:
        if "temp1:" in linea:
            temperatura_linea = linea
            break

    # Extraer la temperatura
    if temperatura_linea:
        partes = temperatura_linea.split()
        if len(partes) >= 2:
            temperatura = partes[1]
            print("Temperatura:", temperatura)
            print(output_time)
            await update.message.reply_text(f'A las {fecha} la temperatura de la raspy es: {temperatura}')
        else:
            print("No se pudo encontrar la temperatura.")
            await update.message.reply_text(f'A las {fecha} no se pudo encontrar la temperatura.')
    else:
        print("No se pudo encontrar la temperatura.")
        await update.message.reply_text(f'A las {fecha} no se pudo encontrar la temperatura.')

app = ApplicationBuilder().token(API).build()


app.add_handler(CommandHandler("estado", estado))
app.add_handler(CommandHandler("instalar", install_package))
app.add_handler(CommandHandler("desinstalar", uninstall_package))
app.add_handler(CommandHandler("upgrade", upgrade_system))
app.add_handler(CommandHandler("shell", shell_comand))
app.add_handler(CommandHandler("startpc", start_pc))

#TODO Añadir comando mirar uso cpu
#TODO Añadir comando mirar uso ram
#TODO Añadir comando mirar uso disco
#TODO Añadir comando mirar uso reiniciar
#TODO Añadir comando mirar uso upgradear

app.run_polling()
