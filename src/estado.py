from telegram import Update
import os
from telegram.ext import ContextTypes
import subprocess


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