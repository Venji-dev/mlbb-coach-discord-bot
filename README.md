# 🛡️ MLBB Coach Discord Bot

Un bot de Discord interactivo diseñado para actuar como tu coach personal de **Mobile Legends: Bang Bang**. Te ayuda a analizar partidas sugiriendo counter-picks, consejos tácticos y las líneas ideales para cada héroe en tiempo real.

## 🚀 Funcionalidades Actuales
*   **Comando de Saludo (`hola bot`):** El bot responde de manera amigable e interactiva al usuario.
*   **Consulta de Counters (`!counter <héroe>`):** Muestra de forma estructurada la línea de juego, los mejores counters y consejos prácticos para enfrentar a héroes como Fanny, Tigreal y Lapu-Lapu.
*   **Base de Datos Local:** Cuenta con un archivo `heroes_db.py` modular para almacenar y expandir la información de los personajes de forma sencilla.

## 🛠️ Requisitos e Instalación
Para ejecutar este bot localmente necesitas:
1. **Python 3.x** instalado.
2. Un archivo `.env` en la raíz del proyecto con tu credencial:
   ```env```
   DISCORD_TOKEN=tu_token_aqui
3. **Instalar las dependencias del proyecto** `pip install` discord.py python-dotenv
4. **Para poder iniciar al bot** `python bot.py`
