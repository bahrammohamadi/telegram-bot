
import requests
import pandas as pd
import numpy as np
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7730961238:AAGbwrC8NM-DDlHl5ztTmigE-4R9V-RPbY8"

# ایجاد منوی ساده
menu_keyboard = [["📊 بورس ایران"], ["🪙 رمزارز (به‌زودی)"]]
markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)

# تابع استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! لطفاً یکی از گزینه‌ها را انتخاب کن:", reply_markup=markup)

# هندلر برای دریافت انتخاب کاربر
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📊 بورس ایران":
        await update.message.reply_text("در حال تحلیل ۲۰ سهم پرتراکنش بورس ایران...")
        result = analyze_iran_bourse()
        await update.message.reply_text(result)
    elif text == "🪙 رمزارز (به‌زودی)":
        await update.message.reply_text("این بخش به‌زودی فعال خواهد شد.")
    else:
        await update.message.reply_text("دستور نامشخص است. لطفاً از منوی زیر انتخاب کن.", reply_markup=markup)

# تحلیل ساده ۲۰ سهم پرتراکنش بورس ایران (شبیه‌سازی شده فعلاً)
def analyze_iran_bourse():
    # اینجا به جای داده واقعی، فقط یک خروجی تستی ساختیم
    example_stocks = ["خگستر", "شپنا", "شستا", "خساپا", "فملی", "شتران", "خودرو", "وتجارت", "فولاد", "وبملت"]
    example_stocks += ["شبندر", "وبصادر", "سایپا", "پارسان", "فاسمین", "کچاد", "وتوصا", "کگل", "شکلر", "رمپنا"]

    output = "نمادهای پرتراکنش امروز:"

"
    for name in example_stocks:
        signal = np.random.choice(["سیگنال خرید", "روند خنثی", "سیگنال فروش"])
        output += f"• {name}: {signal}
"
    return output

# اجرای ربات
if __name__ == "__main__":
    print("Bot is running...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
