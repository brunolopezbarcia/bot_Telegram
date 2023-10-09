#!/bin/bash

function instalar-prereq() {
    apt install boxes -y
}


function mostrarInicio() {
    echo "GRACIAS POR CONFIAR EN NUESTRO BOT" | boxes -d dog -a c
}

function solicitar-datos(){
    read -p "Cual es la API del bot de telegram: " API_BOT_TELEGRAM
    echo $API_BOT_TELEGRAM

    read -p "Cual es la ruta de instalacion: " RUTA_INSTALACION

    read -p "Quieres crear el servicio del bot: [s\n] " CREACION_SERVICIO

    echo "Estan los datos correctos:"
    echo $API_BOT_TELEGRAM
    echo $RUTA_INSTALACION
    echo $CREACION_SERVICIO

    read -p "Estan los datos correctos: [s\n] " COMPROBACION_DATOS
}

function instalar-bot(){
    echo "MOVIENDONOS A LA RUTA DE INSTALACION" | boxes
    cd $RUTA_INSTALACION

    echo "CLONANDO EL REPOSITORIO"  | boxes

    git clone http://brunolb:Brunito213-@192.168.0.100:3000/CASA/bot_Telegram.git

    echo "ESTABLECIENDO VARIABLES DE ENTORNO" | boxes
    touch bot_Telegram/constants/.env
    echo "API_BOT="$API_BOT_TELEGRAM >> bot_Telegram/constants/.env
    echo "RUTA_ENV="$RUTA_INSTALACION"bot_Telegram/constants/.env" >> bot_Telegram/constants/.env

    echo "INSTALANDO LOS PAQUETES DE PYTHON NECESARIOS" | boxes
    pip3 install -r $RUTA_INSTALACION/bot_Telegram/requirements.txt --break-system-packages


    ARCHIVO_SERVICIO=$RUTA_INSTALACION/bot_Telegram/bot_Telegram.service
    if [[ $CREACION_SERVICIO == "s" || $CREACION_SERVICIO == "S" ]]
    then
            sed -i "s|\$RUTA|$RUTA_INSTALACION|g" "$RUTA_INSTALACION/bot_Telegram/bot_Telegram.service"
            mv $RUTA_INSTALACION/bot_Telegram/bot_Telegram.service /etc/systemd/system/
            systemctl daemon-reload
            systemctl enable bot_Telegram --now
            echo "SERVICIO CREADO E INICIADO\n DISFRUTA DE TU NUEVO BOT" | boxes -d dog -a c
    else 
        echo "NO SE CREA EL SERVICIO" | boxes
    fi
}

function main() {
    instalar-prereq
    mostrarInicio
    solicitar-datos
    if [[ $COMPROBACION_DATOS == "s" || $COMPROBACION_DATOS == "S" ]]
    then
          instalar-bot
    else
        solicitar-datos
    fi
}


if [ "$(id -u)" -eq 0 ]; then
  main
else
  echo "EL SCRIPT DEBE CORRERSE COMO ROOT" | boxes -d dog -a c
fi