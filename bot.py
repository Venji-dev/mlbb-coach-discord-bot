import os
import discord
from dotenv import load_dotenv

# 1. Cargar vriables secretas desde el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2. Configurar los permisos (Intents)
intents = discord.Intents.default()
intents.message_content = True # Permiso para que el bot lea lo escrito

# 3. Inicializar el bot
bot = discord.Client(intents=intents)

# 4. Evento: bot conectado con exito
@bot.event
async def on_ready():
    print(f'Hola! Me conecte exitosmenet como {bot.user}')

# 5.Evento: bot leyendo un mensaje
@bot.event
async def on_message(message):
    # Evitar que el bot se responda a si mismo
    if message.author == bot.user:
        return
    # Responder a un saludo de prueba
    if message.content.lower() == 'hola bot':
        await message.channel.send(f'Hola {message.author.name} estoy listo para ser tu coach de MLBB!')

# 6. Encender el bot usando el TOKEN
bot.run(TOKEN)