import os
import sqlite3
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 1. Cargar vriables secretas
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2. Configurar los permisos
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents) # <-- Se modifico para gestionar mejor los comandos

# Funcion auxiliar para consultar la base de datos de SQLite <--- Se modifico para usar la nueva base de datos
def obtener_datos_heroe(nombre_heroe):
    conexion = sqlite3.connect("heroes.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM heroes WHERE LOWER(heroes) = ?", (nombre_heroe.lower(),))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado

@bot.event
async def on_ready():
    print(f'Coach MLBB Conectado como {bot.user}!')

# 3. Vista a Discord (Contenedor de lso botones)
class VisitaRolesCounter(discord.ui.View):
    def __init__(self, datos_heroe, usuario_original):
        super().__init__(timeout=60) #Temposizador de desactivación (60 seg)
        self.datos = datos_heroe
        self.usuario = usuario_original
    
    # Modificador de respuesta generico para botones
    async def procesar_carril(self, interaction: discord.Interaction, indice_columna, nombre_carril):
        # Validar que solo respónda a quien uso el comando
        if interaction.user != self.usuario:
            await interaction.response.send_message("¡Este menú no es tuyo!", ephemeral=True)
            return
        
        # Extraer el contra-pick de la columna especifica de la BD
        counter_especifico = self.datos[indice_columna]
        nombre_heroe = self.datos[0]

        if counter_especifico:
            mensaje = f"Coach dice: Para enfrentar a **{nombre_heroe.capitalize()}** en la **{nombre_carril}**, los mejores counters son: **{counter_especifico.capitalize()}**."
        else:
            mensaje = f"Aún no tengo un counter registrado para **{nombre_heroe.capitaize()}** en la **{nombre_carril}**."
        
        # Desactiar los botones luego de elegir
        for hijo in self.children:
            hijo.disable = True

        # Editamos el mensaje original con la respuesta final
        await interaction.response.edit_message(content=mensaje, embed=None, view=self)

    # Definición de cada Botón (Corresponden a los índices de tu tabla en heroes_db.py)
    @discord.ui.button(label="Jungla", style=discord.ButtonStyle.primary)
    async def boton_jungla(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.procesar_carril(interaction, 1, "Jungla") # Índice 1 = jungla

    @discord.ui.button(label="Línea Exp", style=discord.ButtonStyle.success)
    async def boton_exp(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.procesar_carril(interaction, 2, "Línea de Experiencia") # Índice 2 = linea_exp

    @discord.ui.button(label="Línea Mid", style=discord.ButtonStyle.danger)
    async def boton_mid(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.procesar_carril(interaction, 3, "Línea de Mid") # Índice 3 = linea_mid

    @discord.ui.button(label="Línea Oro", style=discord.ButtonStyle.secondary)
    async def boton_oro(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.procesar_carril(interaction, 4, "Línea de Oro") # Índice 4 = linea_gold

    @discord.ui.button(label="Roamer", style=discord.ButtonStyle.primary)
    async def boton_roamer(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.procesar_carril(interaction, 5, "Roamer") # Índice 5 = roamer

# 4. Comando !counter estructurado <-- Se modifico este
@bot.command(name="counter")
async def counter(ctx, *, heroe: str = None):
    if not heroe:
        await ctx.send("Por favor, especifica el nombre del heroe. Ejemplo: '!counter akai'")
        return
    
    datos = obtener_datos_heroe(heroe.strip())

    if datos:
        # Creación del Embed
        embed = discord.Embed(
            title=f"Analisis de tu Counter-Pick: {datos[0].capitalize()}",
            description="¿En que rol o linea te vas a enfrentar a este heroe? Selecciona un boton abajo para darte el conseño exacto.",
            color=discord.Color.blue()
        )

        # Instanciamos la vista con los botones pasándole los datos de la BD y el usuario
        vista = VisitaRolesCounter(datos, ctx.author)
        await ctx.send(embed=embed, view=vista)
    else: 
        await ctx.send(f"Aún no está registrado **{heroe}** en la base de datos. ¡Lo anotaré para estudiarlo!")

# 5. Encender el bot usando el TOKEN.
bot.run(TOKEN)