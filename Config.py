import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "18196466"))
    API_HASH = os.environ.get("API_HASH", "b85f12702596a6cfb6fb51b1c4e01630")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Elrasam11111bot")
    SUPPORT = os.environ.get("SUPPORT", "EL_RASA")
    CHANNEL = os.environ.get("CHANNEL", "E_L_R_A_S_A_M")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/6e1cb97beb53c9c51c2d5.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
