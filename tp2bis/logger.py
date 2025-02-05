import logging

logging.basicConfig(filename="output.log", level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)
