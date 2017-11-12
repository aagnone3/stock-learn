import logging


def configure_logger(name=__name__, level="INFO"):
    """

    :param name:
    :param level:
    :return:
    """
    level_map = {
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    level_caps = level.upper()
    if level_caps not in level_map:
        print("Level {} not supported. Defaulting to INFO.".format(level))
        level_caps = "INFO"

    level = level_map[level_caps]
    log_format = '%(asctime)s %(levelname)s %(name)s: [%(processName)s:%(process)d] %(message)s'
    logging.basicConfig(level=level, format=log_format)
    return logging.getLogger(name)
