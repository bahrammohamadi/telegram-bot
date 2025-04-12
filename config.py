# توکن ربات تلگرام
BOT_TOKEN = "7730961238:AAGbwrC8NM-DDlHl5ztTmigE-4R9V-RPbY8"

# آی‌دی مدیر ربات
ADMIN_ID = 46428047

# حالت‌های مختلف بازار (سهام و رمزارزها)
MARKET_MODE = ["stock", "crypto"]

# بررسی صحت تنظیمات
def validate_config():
    if not BOT_TOKEN or not isinstance(BOT_TOKEN, str):
        raise ValueError("توکن ربات به درستی وارد نشده است.")
    if not ADMIN_ID or not isinstance(ADMIN_ID, int):
        raise ValueError("آی‌دی مدیر باید یک عدد صحیح باشد.")
    if not MARKET_MODE or not isinstance(MARKET_MODE, list):
        raise ValueError("حالت‌های بازار باید به صورت لیست تنظیم شوند.")

# فراخوانی تابع اعتبارسنجی
try:
    validate_config()
    print("پیکربندی به درستی انجام شد.")
except ValueError as error:
    print(f"خطا در تنظیمات: {error}")
