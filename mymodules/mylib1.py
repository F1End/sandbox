import logging

_logger = logging.getLogger(__name__)


def func1(value):
    if value is None:
        _logger.error("You did not give a real value!")
    else:
        print(f"Your value is {value}!")
