from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

menu_kb = ReplyKeyboardMarkup(
            [
                [KeyboardButton("🍽 Menyu")],
                [KeyboardButton('📖 Buyurtmalar tarixi'), KeyboardButton("✍️ Fikr bildirish")],
                [KeyboardButton("ℹ️ Ma'lumot"), KeyboardButton("☎️ Biz bilan aloqa")],
                [KeyboardButton("⚙️Sozlamalar")]
            ],
            resize_keyboard=True
        )
