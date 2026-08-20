import logging
import os


LOG_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data"
)

LOG_FILE = os.path.join(
    LOG_DIR,
    "system_monitor.log"
)


os.makedirs(LOG_DIR, exist_ok=True)


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


logger = logging.getLogger("system_monitor")