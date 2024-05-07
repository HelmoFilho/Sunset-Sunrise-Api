## -- Importing External Modules -- ##
import multiprocessing

## -- Importing Internal Modules -- ##
import config as cnfg

web_concurrency_str = cnfg.GUNICORN_WEB_CONCURRENCY
max_workers = cnfg.GUNICORN_MAX_WORKERS

if web_concurrency_str:

    web_concurrency = int(web_concurrency_str)
    assert web_concurrency > 0

else:

    cores = multiprocessing.cpu_count()

    workers_per_core = int(cnfg.GUNICORN_WORKERS_PER_CORE)
    default_web_concurrency = workers_per_core * cores

    web_concurrency = max(int(default_web_concurrency), 2)

if max_workers:
    web_concurrency = min(web_concurrency, int(max_workers))

# Gunicorn config variables
workers = web_concurrency
bind = f"{cnfg.HOST}:{cnfg.PORT}"
graceful_timeout = int(cnfg.GUNICORN_GRACEFUL_TIMEOUT)
timeout = int(cnfg.GUNICORN_TIMEOUT)
keepalive = int(cnfg.GUNICORN_KEEP_ALIVE)

print({
    "workers": workers,
    "bind": bind,
    "graceful_timeout": graceful_timeout,
    "timeout": timeout,
    "keepalive": keepalive,
})