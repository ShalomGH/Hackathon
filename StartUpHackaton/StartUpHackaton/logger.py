import logging

from .settings import LOGGING_SETTINGS


class Colors:
    """Console Colors"""
    reset = '\x1B[0m'
    bold = '\x1b[1m'
    dim = "\x1b[2m"
    underline = '\x1B[4m'
    blink = '\x1b[5m'
    reverse = "\x1b[7m"  # BACKGROUND
    hidden = "\x1b[8m"

    Black = '\x1B[30m'
    Red = '\x1B[31m'
    Green = '\x1B[32m'
    Yellow = '\x1B[33m'
    Blue = '\x1B[34m'
    Magenta = '\x1B[35m'
    Cyan = '\x1B[36m'
    White = '\x1B[37m'
    Grey = '\x1B[38m'


class CustomFormatter(logging.Formatter):
    MESSAGE_FORMATS = {
        logging.DEBUG: Colors.Blue,
        logging.INFO: Colors.Green,
        logging.WARNING: Colors.Yellow,
        logging.ERROR: Colors.Red,
        logging.CRITICAL: Colors.underline + Colors.bold + Colors.Red,
    }

    def __init__(self, colored=False, *args, **kwargs):
        self.colored = colored
        super().__init__(*args, **kwargs)

    def format(self, record):
        log_format = LOGGING_SETTINGS['FORMAT']
        if self.colored:
            message_colored = self.MESSAGE_FORMATS[record.levelno] + "{message}" + Colors.reset
            log_format = log_format.replace('{message}', message_colored)

        formatter = logging.Formatter(log_format, style='{', datefmt=LOGGING_SETTINGS['DATEFORMAT'])
        return formatter.format(record)


class CreationFormatter(CustomFormatter):
    MESSAGE_FORMATS = {
        logging.DEBUG: Colors.Blue,
        logging.INFO: Colors.Magenta,
        logging.WARNING: Colors.Yellow,
        logging.ERROR: Colors.Red,
        logging.CRITICAL: Colors.underline + Colors.bold + Colors.Red,
    }

    def format(self, record):
        log_format = LOGGING_SETTINGS['FORMAT']
        message_colored = self.MESSAGE_FORMATS[record.levelno] + "{message}" + Colors.reset
        log_format = log_format.replace('{message}', message_colored)

        formatter = logging.Formatter(log_format, style='{', datefmt=LOGGING_SETTINGS['DATEFORMAT'])
        return formatter.format(record)


class SkipStaticFilter(logging.Filter):
    """ Logging filter to skip logging of staticfiles to terminal """

    def filter(self, record):
        return not record.getMessage().startswith('"GET')
