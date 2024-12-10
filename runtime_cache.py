import os
from datetime import datetime


def get_last_runtime(file_path):
    """Read the last runtime from a file."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            timestamp = file.read().strip()
            return int(timestamp) if timestamp.isdigit() else 0
    return 0


def save_current_runtime(file_path):
    """Save the current timestamp to a file."""
    current_timestamp = int(datetime.now().timestamp())
    with open(file_path, "w") as file:
        file.write(str(current_timestamp))
