import os
import time
import re
from datetime import datetime


def write_log(file_path: str, message: str) -> None:
    """
    Writes a log message to the specified log file with a timestamp.
    
    :param file_path: Path to the log file
    :param message: Log message to write
    """
    with open(file_path, 'a') as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")


def read_logs(file_path: str) -> list:
    """
    Reads the entire log file and returns a list of log entries.
    
    :param file_path: Path to the log file
    :return: List of log lines
    """
    if not os.path.exists(file_path):
        return []
    
    with open(file_path, 'r') as log_file:
        return log_file.readlines()


def search_logs(file_path: str, keyword: str) -> list:
    """
    Searches for a keyword in the log file and returns matching lines.
    
    :param file_path: Path to the log file
    :param keyword: Keyword to search for in the logs
    :return: List of matching log lines
    """
    logs = read_logs(file_path)
    return [line for line in logs if keyword in line]


def detect_anomalies(file_path: str, pattern: str) -> list:
    """
    Detects anomalies in the log file based on a regex pattern.
    
    :param file_path: Path to the log file
    :param pattern: Regular expression pattern to match anomalies
    :return: List of log lines that match the pattern
    """
    logs = read_logs(file_path)
    regex = re.compile(pattern)
    return [line for line in logs if regex.search(line)]


def monitor_log(file_path: str):
    """
    Monitors the log file in real-time and prints new entries as they are added.
    
    :param file_path: Path to the log file
    """
    if not os.path.exists(file_path):
        print("Log file does not exist.")
        return
    
    with open(file_path, 'r') as log_file:
        log_file.seek(0, os.SEEK_END)  # Move to the end of file
        while True:
            line = log_file.readline()
            if line:
                print(line.strip())
            else:
                time.sleep(1)  # Wait for new lines to be written