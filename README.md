*   # 🛡️ MLBB Coach Discord Bot

Un bot de Discord interactivo diseñado para actuar como tu coach personal de **Mobile Legends: Bang Bang**. Te ayuda a analizar partidas sugiriendo counter-picks, consejos tácticos y las líneas ideales para cada héroe en tiempo real.

## 🚀 Funcionalidades Actuales
*   **Comando de Saludo (`hola bot`):** El bot responde de manera amigable e interactiva al usuario.
*   **Consulta de Counters (`!counter <héroe>`):** Muestra de forma estructurada la línea de juego, los mejores counters y consejos prácticos para enfrentar a héroes como Akai y Alice.
*   **Base de Datos Automatizada:** Utiliza una base de datos **SQLite** (`heroes.db`) gestionada de forma eficiente mediante un script importador.

## 🗄️ Gestión de Héroes (Excel / CSV)
Para evitar escribir código de forma manual, la base de datos se alimenta directamente desde un archivo de Excel:

1. Modifica o añade los héroes en el archivo `heroes.csv` usando tu editor preferido o Excel (asegúrate de mantener las columnas y usar `;` como separador).
2. Ejecuta el script de importación en tu terminal para actualizar la base de datos local:
   ```bash
   python heroes_db.py
   

## 🛠️ Requisitos e Instalación
Para ejecutar este bot localmente necesitas:
1. **Python 3.x** instalado.
2. Un archivo `.env` en la raíz del proyecto con tu credencial:
   ```env```
   DISCORD_TOKEN=tu_token_aqui
3. **Instalar las dependencias del proyecto** `pip install` discord.py python-dotenv
4. **Para poder iniciar al bot** `python bot.py`
