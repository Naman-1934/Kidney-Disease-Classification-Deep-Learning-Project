import os
import sys
import logging

#               Current Time, Log Level Name( information log level name), Module Name, Message  
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Create a log folder
log_dir = "logs"

# Inside the folder it will create a log file
log_filepath = os.path.join(log_dir, "running_logs.log")

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("kidney_disease_classification_logger")