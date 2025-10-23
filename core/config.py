import logging


def setup_logging():
    logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="{asctime} [{levelname}] {name}: {message}",
                    style="{")

    logging.getLogger("watchfiles").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)