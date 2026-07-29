import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    text = """
👑 سلام! به کلش کوچ هوشمند خوش آمدی.

🧠 من مربی تحلیل‌گر Clash Royale هستم.

امکانات:
📊 تحلیل اکانت
🃏 پیشنهاد دک
📈 اولویت ارتقای کارت‌ها
🎯 بررسی نقاط ضعف

برای شروع Player Tag خودت را بفرست.
مثال:
#ABC12345
"""
    bot.reply_to(message, text)

@bot.message_handler(func=lambda message: True)
def analyze(message):
    bot.reply_to(
        message,
        "🔍 پیام دریافت شد.\n\n"
        "به‌زودی تحلیل هوشمند اکانت فعال می‌شود. 👑"
    )

print("Bot is running...")
bot.infinity_polling()
