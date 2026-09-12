import logging


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s level=%(levelname)s %(name)s %(message)s",
    )
