import requests
import pandas as pd
import numpy as np
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN, ADMIN_ID, MARKET_MODE  # وارد کردن تنظیمات از config.py

# ایجاد منوی ساده با استفاده از حالت‌های بازار
menu_keyboard = [[f"📊 {mode.capitalize()}"] for mode in MARKET_MODE] + [["🪙 رمزارز (به‌زودی)"]]
markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)

# تابع استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = f"سلام! شما مدیر ربات هستید. آی‌دی شما: {ADMIN_ID}\n"
    mode_message = f"حالت‌های فعال ربات: {', '.join(MARKET_MODE)}"
    await update.message.reply_text(welcome_message + mode_message, reply_markup=markup)

# هندلر برای دریافت انتخاب کاربر
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text.startswith("📊"):  # چک کردن انتخاب حالت بازار
        selected_mode = text[2:].lower()
        await update.message.reply_text(f"در حال تحلیل حالت بازار {selected_mode}...")
        result = analyze_market(selected_mode)
        await update.message.reply_text(result)
    elif text == "🪙 رمزارز (به‌زودی)":
        await update.message.reply_text("این بخش به‌زودی فعال خواهد شد.")
    else:
        await update.message.reply_text("دستور نامشخص است. لطفاً از منوی زیر انتخاب کن.", reply_markup=markup)

# تحلیل ساده بر اساس حالت بازار
def analyze_market(mode):
    if mode == "stock":
        example_stocks = ["خگستر", "شپنا", "شستا", "خساپا", "فملی", "شتران", "خودرو", "وتجارت", "فولاد", "وبملت"]
        example_stocks += ["شبندر", "وبصادر", "سایپا", "پارسان", "فاسمین", "کچاد", "وتوصا", "کگل", "شکلر", "رمپنا"]
        output = "نمادهای پرتراکنش امروز:\n"
        for name in example_stocks:
            signal = np.random.choice(["سیگنال خرید", "روند خنثی", "سیگنال فروش"])
            output += f"• {name}: {signal}\n"
        return output
    elif mode == "crypto":
        return "بخش رمزارز هنوز فعال نشده است."
    else:
        return "حالت نامشخص است."

# اجرای ربات
if __name__ == "__main__":
    print("ربات در حال اجرا است...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
