from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Merhaba {}, bu bot ile ilk yazan botunu kurabilirsin.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Botu Kur", callback_data="generate")],
        [InlineKeyboardButton(text="Başa Dön", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Botu Kur", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Botu Kur", callback_data="generate")],
        [InlineKeyboardButton("Sahip", url="https://t.me/Anonymousss_TR")],
        [
            InlineKeyboardButton("Nasıl kullanılır", callback_data="help"),
            InlineKeyboardButton("Hakkında", callback_data="about")
      ]
    
    ]


    # Help Message
    HELP = """
✨ **Mevcut komutlar** ✨

/about - Bot Hakkında Bilgi
/help - Bot Hakkında Yardım
/start - Botu Başlatır
/generate - İlk Yazan Botunu Kurar
/cancel - Kurulumu İptal Eder
/restart - Botu Yeniden Başlatır
"""

    # About Message
    ABOUT = """
**Bot Hakkında** 

Ücretsiz bir şekilde ilk yazan botu kurar. Bot **otomatik dm özelliği**nede sahiptir.
    """
