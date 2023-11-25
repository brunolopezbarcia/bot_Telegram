from estado import estado
from install_package import install_package
from shellcomands import shell_comand
from start_pc import start_pc
from uninstall_package import uninstall_package
from upgrade import upgrade_system


from telegram.ext import CommandHandler


def add_handlers(app):
    app.add_handler(CommandHandler("estado", estado))
    app.add_handler(CommandHandler("instalar", install_package))
    app.add_handler(CommandHandler("desinstalar", uninstall_package))
    app.add_handler(CommandHandler("upgrade", upgrade_system))
    app.add_handler(CommandHandler("shell", shell_comand))
    app.add_handler(CommandHandler("startpc", start_pc))