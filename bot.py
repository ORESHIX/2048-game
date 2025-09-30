import telebot
from telebot import types

# --- НАСТРОЙКИ ---
# ВАЖНО: Замените 'YOUR_BOT_TOKEN' на токен, который вы получили от BotFather
TOKEN = '7720286113:AAE6fP1BaB_gDiGNpC-V5orrzVOzv9nd7XY'

# ВАЖНО: Замените этот URL на публичный HTTPS-адрес, где размещен ваш файл game_2048.html
GAME_URL = 'https://oreshix.github.io/2048-game/' 
# ------------------

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'game'])
def send_welcome(message):
    """
    Обработчик команды /start и /game.
    Отправляет пользователю кнопку для запуска Mini App.
    """
    
    # 1. Создание кнопки, которая открывает Web App
    # WebAppInfo — это специальный объект, который указывает на ваш HTML-файл.
    web_app = types.WebAppInfo(GAME_URL)
    
    # 2. Создание клавиатуры с этой кнопкой
    keyboard = types.InlineKeyboardMarkup()
    play_button = types.InlineKeyboardButton(
        text="🎮 Играть в 2048", 
        web_app=web_app
    )
    keyboard.add(play_button)
    
    # 3. Отправка сообщения с приветствием и кнопкой
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в 2048! Нажмите кнопку, чтобы запустить игру.",
        reply_markup=keyboard
    )

# Запуск бота (постоянный опрос новых сообщений)
print("Бот запущен и ожидает сообщений...")
try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"Ошибка при запуске бота: {e}")
