## -- Importing External Modules -- ##
import uvicorn

## -- Importing Internal Modules -- ##
from src.app.routing import app
import config as cnfg


def main() -> None:
    """
    Created for easy debugging
    """

    dict_connection = {
        "app": "main:app",
        "host": cnfg.HOST,
        "port": cnfg.PORT,
        "workers": cnfg.UVICORN_WORKERS,
        "backlog": cnfg.UVICORN_BACKLOG_LIMIT,
        "limit_max_requests": cnfg.UVICORN_CONNECTION_LIMIT,
        "timeout_keep_alive": cnfg.UVICORN_CLEANUP_INTERVAL,
    }

    uvicorn.run(**dict_connection)


if __name__ == "__main__":
    main()