import os
import discord
from dotenv import load_dotenv
from heroes_db import HEROES

# 1. Cargar vriables secretas desde el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2. Configurar los permisos (Intents)
intents = discord.Intents.default()
intents.message_content = True # Permiso para que el bot lea lo escrito.

# 3. Inicializar el bot.
bot = discord.Client(intents=intents)

# 4. Evento: bot conectado con exito.
@bot.event
async def on_ready():
    print(f'Hola! Me conecte exitosmenet como {bot.user}')

# 5. Evento: bot leyendo un mensaje.
@bot.event
async def on_message(message):
    # Evitar que el bot se responda a si mismo.
    if message.author == bot.user:
        return
    # Responder a un saludo de prueba.
    if message.content.lower() == 'hola bot':
        await message.channel.send(f'Hola {message.author.name} estoy listo para ser tu coach de MLBB!')
        return
    # Comando conuter-pick
    if message.content.lower().startswith('!counter'):
        # Extraemos el nombre del heroe.
        # .split(' ', 1) divide el texto en 2 partes usando el primer espacio.
        partes = message.content.lower().split(' ', 1)
        
        if len(partes)>1:
            heores_buscando = partes[1].strip() # 'lapu-lapu', 'Yve', etc.

            # Buscamos si el heroe existe en la base de datos
            if heores_buscando in HEROES:
                datos = HEROES[heores_buscando]
                linea = datos["Linea"]
                counters = ", ".join(datos["Counters"])
                conssejos = datos["Consejo"]

                # Armamos la respuesta estructurada
                respuesta = (
                    f"**Analisis de Coach para {heores_buscando.capitalize()}** \n"
                    f"**Linea habitual:** {linea}\n"
                    f"**Counters Directos:** {counters}\n"
                    f"**Consejo tactico:** {conssejos}"
                )
                await message.channel.send(respuesta)
            else:
                # si el heroe no esta en la base de datos
                await message.channel.send(f"Aún no esta registrado **{heores_buscando}** en la base de datos. Lo voy a anotar para estudiarlo!")

# 6. Encender el bot usando el TOKEN.
bot.run(TOKEN)