
# Logowanie w Pythonie
import logging
import sys
import syslog

log_format = "%(asctime)s:%(levelname)s:%(filename)s:%(message)s"
logging.basicConfig(
    level=logging.DEBUG, #poziom logowania
    #filename="app.log", #plik logu
    format=log_format, #format logu
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Info message")
logging.error("Error message")
logging.fatal("Fatal error")

try:
    x = 0
    y = 1/x
except Exception as exc:
    logging.critical(exc, exc_info=True)
    sys.exit(1)
