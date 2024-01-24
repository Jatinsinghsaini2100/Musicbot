import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "29880176"))
API_HASH = getenv("API_HASH", "a703140978f9856e3839176beaca03ec")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6686420045:AAH3NWOdFXjKOXSbnpgEVDDPGg2iJsCjfaU")

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
STRING1 = getenv("STRING_SESSION", "BQHH73AAItoUORcc8Fy4vYnz5CWIUnFmFA_0O2bitQWFJLQsUT9EbGlwM073um60Sd_xp12Yn8NY5-G79P9XlcjKkP9zc-jX6u2nfSmCHxLGFNCR9pTTohpaI0muSVAZh7RukXKwGTTg7uU1ouDdtRePBE_O9FJZnog39fK4qYzkFZ8CY2CF6eqVN8iffX-kjEIhyNzz8QUCcwvXF0X_twsNr6HYJVT43ay68E-Bw3uZtdlbEpnYeujjSxQBNE1AxMRrcIyL0i_iTkesV8AT0Gk663kq2nQjPYDd0jjICUzx-7aUBqIe07zsAb1MVRUugtFzEsIKtQ6A6rejZwZ9ThcLJOgSiwAAAAFbgnjsAA")
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
    "START_IMG_URL", "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/663108c0eccc9f321c4c4.jpg"


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
