import logging

from mymodules import mylib1

_logger = logging.getLogger(__name__)

# print("Hello there!")
# _logger.warning("WARNING TEST HERE!")

mylib1.func1("Precious!")
mylib1.func1(None)