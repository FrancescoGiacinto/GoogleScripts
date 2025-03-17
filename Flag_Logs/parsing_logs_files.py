import os

def read_and_split_file(file_path: str, delimiter: str = " ") -> list:
    """
    Reads a file, converts its content into a string, and splits it into a list using a specified delimiter.
    
    Args:
        file_path (str): The path to the file to be read.
        delimiter (str): The character to split the file content. Defaults to whitespace.
    
    Returns:
        list: A list containing the split contents of the file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    
    with open(file_path, "r") as file:
        content = file.read()
    
    return content.split(delimiter)


def write_joined_file(file_path: str, data_list: list, separator: str = " ") -> None:
    """
    Joins a list into a string using a separator and writes it to a file.
    
    Args:
        file_path (str): The path to the file to be written.
        data_list (list): A list of strings to be joined.
        separator (str): The separator to use when joining elements. Defaults to a space.
    """
    content = separator.join(data_list)
    
    with open(file_path, "w") as file:
        file.write(content)


def secure_parse_log(file_path: str) -> list:
    """
    Reads a log file, splits each line into individual words, and returns a structured list.
    
    Args:
        file_path (str): The path to the log file.
    
    Returns:
        list: A list of parsed log lines, each represented as a list of words.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file '{file_path}' not found.")
    
    parsed_logs = []
    with open(file_path, "r") as file:
        for line in file:
            parsed_logs.append(line.strip().split())
    
    return parsed_logs


def anonymize_log(file_path: str, output_path: str, sensitive_words: list) -> None:
    """
    Reads a log file, anonymizes sensitive information, and writes the sanitized log to a new file.
    
    Args:
        file_path (str): The path to the input log file.
        output_path (str): The path to the output sanitized log file.
        sensitive_words (list): A list of words that should be replaced with '[REDACTED]'.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")
    
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    sanitized_lines = []
    for line in lines:
        words = line.split()
        sanitized_line = ["[REDACTED]" if word in sensitive_words else word for word in words]
        sanitized_lines.append(" ".join(sanitized_line))
    
    with open(output_path, "w") as file:
        file.write("\n".join(sanitized_lines))


def detect_suspicious_activity(file_path: str, keywords: list) -> list:
    """
    Reads a log file and detects lines containing specific keywords related to suspicious activity.
    
    Args:
        file_path (str): The path to the log file.
        keywords (list): A list of suspicious keywords to look for.
    
    Returns:
        list: A list of suspicious log entries.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file '{file_path}' not found.")
    
    suspicious_entries = []
    with open(file_path, "r") as file:
        for line in file:
            if any(keyword in line for keyword in keywords):
                suspicious_entries.append(line.strip())
    
    return suspicious_entries