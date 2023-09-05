''''
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("HRLogger")
'''

'''
import os
import logging

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True) 

try:
    log_filepath = os.path.abspath(os.path.join(log_dir, 'running_logs.log'))
    with open(log_filepath, 'w') as file:
        pass  # Do nothing, just create the file
except Exception as e:
    print(f"Error creating log file: {e}")


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]",
    handlers=[
        logging.FileHandler(log_filepath, delay=True),  # Disable buffering
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('HRLogger')
'''

import os
import logging

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

log_filepath = os.path.join(log_dir, 'running_logs.log')

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]",
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('HRLogger')

# ...

# At the end of your code, add the following line to close the logger:
logging.shutdown()
