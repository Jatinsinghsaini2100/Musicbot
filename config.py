import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "29880176"))
API_HASH = getenv("API_HASH", "a703140978f9856e3839176beaca03ec")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6686420045:AAH4xpOg3cfDtRK4TP7usMe7Mzl3rmej8dw")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://tonyxbot:tonyxbot@cluster0.bojrxzg.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001887112549"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5366891026"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://t.me/sastatony",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/sastatony")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+e-sDXiSwXntjMDU1")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFep5gAEj_riAk0lE-5zore9rd5dYCd4YqagCsnHbOSzknHm4tDHIgzbdvUwsvJnOY7WgxZj_30FX5mrog9u1fAdIHiqh1JcLzFqiLTutwm8ADFqE8FTr_F_L0EzwyIRmBZh8ow_Xo65gY4NZauq97yKyr_Hk6f_-NBgej8bi-_ZDgHmQ9f8La_OzHba69IWfxMixgll1akgO8wXaKkOqXfYCHM48wrx4CyllrMNR5VvcaNz3T_RrRUi6CeY9wLRWKFPTYQlXCk-9ZDoBm8J1yMVsqZqp2iFBYYV8n0XP6jwqpBgFvZ0IiU_DpDbB8mrbmlvZsOhHoneDtsLYgGEtruzdS4_AAAAAGTODQBAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/f0ce9ed1ccc9685f2d5e7.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
