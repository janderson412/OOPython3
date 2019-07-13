import logging

def TestFunc(*args, **kwargs):
    for arg in args:
        print(f"arg={arg}")

    for kwarg in kwargs.keys():
        key = kwarg
        print(f"kwarg[{key}] = {kwargs[key]}")


logger = logging.getLogger(__name__)
logging.basicConfig(filename='C:\Temp\logger.txt', level=logging.INFO)
logger.info("Startup !!!")

TestFunc(1, 2, 3, first='John', last='Anderson')