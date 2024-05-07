## -- Importing External Modules -- ##
import dotenv, os, pytz

## -- Importing Internal Modules -- ##

dotenv.load_dotenv(".env")

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 15000))
SHOW_DOC = os.getenv("SHOW_DOC", "N").upper() == 'S'

TIMEZONE = os.getenv("TIMEZONE", "America/Fortaleza")
if TIMEZONE not in pytz.all_timezones:
    raise ValueError('Invalid timezone string')

UVICORN_WORKERS = int(os.getenv("UVICORN_WORKERS", 4))
UVICORN_CONNECTION_LIMIT = int(os.getenv("UVICORN_CONNECTION_LIMIT", 4))
UVICORN_BACKLOG_LIMIT = int(os.getenv("UVICORN_BACKLOG_LIMIT", 50))
UVICORN_CLEANUP_INTERVAL = int(os.getenv("UVICORN_CLEANUP_INTERVAL", 10))

GUNICORN_WEB_CONCURRENCY = os.getenv("GUNICORN_WEB_CONCURRENCY")
GUNICORN_WORKERS_PER_CORE = int(os.getenv("GUNICORN_WORKERS_PER_CORE", 1))
GUNICORN_MAX_WORKERS = os.getenv("GUNICORN_MAX_WORKERS")
GUNICORN_GRACEFUL_TIMEOUT = int(os.getenv("GUNICORN_GRACEFUL_TIMEOUT", 120))
GUNICORN_TIMEOUT = int(os.getenv("GUNICORN_TIMEOUT", 120))
GUNICORN_KEEP_ALIVE = int(os.getenv("GUNICORN_KEEP_ALIVE", 5))