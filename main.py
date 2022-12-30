import logging


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    mydict: dict = dict()
    try:
        mydict["missing_key"]
    except KeyError as e:
        logging.info(e)

    print("toot!")
    print("toot!")
