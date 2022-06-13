## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgB58vqYfK3Pp4p9rTtBR2emmMvWM7mz3a9rdapyG8-KDnsvr1_PhsCTEuvU9LLfZmXo5uUN1MIDV-QNt-p3h9PBLqxaw6nLcSI8Syu9Ce_TmAybWdGbUm-UR5nZ0BbfvhmWM-s9dMNXa793-SA7XArlH30QX8dALyNGYCN6jSXmUa4XgzAm2_qG97q-q0KV9Jjk1FbOka2FBsKvM6r8MhCGQYOou6xzP8OIuFN0fy9RehFNnkzPM5vDL9-A7PqKzMJz0_pOL0oqu_YZ_qv1JWn2UU3VxysyroFQkhFalfvT7c3XKO6DBAGFYEP0X_Kx63AW5BI9lli4w5ou8ifzNUdOAAAAAUGEif4A")
BOT_TOKEN = getenv("BOT_TOKEN", "5346606020:AAGksjGL3ZAs2Ji1IxeFJnNh_hrXfyLy8Xs")
BOT_NAME = getenv("BOT_NAME", "Music ₘᵦ𝄴₃")
API_ID = int(getenv("API_ID", "11798215"))
API_HASH = getenv("API_HASH", "433b9d1c8d24b23e0101cfd42ce262e8")
OWNER_NAME = getenv("OWNER_NAME", "abbas")
OWNER_USERNAME = getenv("OWNER_USERNAME", "q1n1p")
ALIVE_NAME = getenv("ALIVE_NAME", "𝓜𝓞𝓞𝓝₂₀₀₁")
BOT_USERNAME = getenv("BOT_USERNAME", "Music636_bot")
OWNER_ID = getenv("OWNER_ID", "5394172414")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "q1n1p")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "s_s3_s")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "q1n1p")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/46fa55b49b85c084159ce.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/466de30ee0f9383c8e09e.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
