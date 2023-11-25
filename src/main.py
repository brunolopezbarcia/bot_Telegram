import os
from pathlib import Path
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from add_handlers import add_handlers

#Funciones de comandos creadas por mi.

dotenv_path = Path('../constants/.env')
load_dotenv(dotenv_path=dotenv_path)

API = os.getenv('API_BOT')

app = ApplicationBuilder().token(API).build()

add_handlers(app)

#TODO Añadir comando mirar uso cpu
#TODO Añadir comando mirar uso ram
#TODO Añadir comando mirar uso disco
#TODO Añadir comando mirar uso reiniciar

app.run_polling()
