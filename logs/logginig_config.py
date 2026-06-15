import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=(logging.FileHandler("logs/app.log"),),
)

logger = logging.getLogger()
logger.info("uuigiu")
