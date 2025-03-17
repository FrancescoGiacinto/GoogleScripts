import re
from typing import List, Tuple


def is_valid_email(email: str) -> bool:
    """
    Validate an email address using a regular expression.
    
    :param email: The email address to validate.
    :return: True if the email is valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def extract_ip_addresses(log_data: str) -> List[str]:
    """
    Extract all IPv4 addresses from a given log string.
    
    :param log_data: A string containing log data.
    :return: A list of extracted IP addresses.
    """
    pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    return re.findall(pattern, log_data)


def detect_sql_injection(query: str) -> bool:
    """
    Detect potential SQL injection patterns in a given SQL query.
    
    :param query: The SQL query string to analyze.
    :return: True if an SQL injection pattern is detected, False otherwise.
    """
    pattern = r"('|--|#|;|\/\*|\*\/|xp_)"
    return bool(re.search(pattern, query, re.IGNORECASE))


def extract_urls(text: str) -> List[str]:
    """
    Extract all URLs from a given text using a regular expression.
    
    :param text: The input text containing potential URLs.
    :return: A list of extracted URLs.
    """
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return re.findall(pattern, text)


def mask_sensitive_data(text: str) -> str:
    """
    Mask sensitive data such as credit card numbers in a given text.
    
    :param text: The input text containing potential sensitive data.
    :return: The text with sensitive data masked.
    """
    pattern = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
    return re.sub(pattern, '****-****-****-****', text)


def analyze_password_strength(password: str) -> Tuple[bool, str]:
    """
    Check if a password meets strong security requirements.
    
    :param password: The password string to check.
    :return: A tuple containing a boolean (True if strong, False otherwise) and a message.
    """
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(pattern, password):
        return True, "Password is strong."
    return False, "Password must be at least 8 characters long, include an uppercase letter, a lowercase letter, a number, and a special character."

# Example usage:
if __name__ == "__main__":
    print(is_valid_email("test@example.com"))  # True
    print(extract_ip_addresses("Failed login from 192.168.1.1 on port 22"))  # ['192.168.1.1']
    print(detect_sql_injection("SELECT * FROM users WHERE username = 'admin' --"))  # True
    print(extract_urls("Visit https://example.com for more details."))  # ['https://example.com']
    print(mask_sensitive_data("My credit card number is 1234-5678-9101-1121."))  # 'My credit card number is ****-****-****-****.'
    print(analyze_password_strength("StrongPass1!"))  # (True, 'Password is strong.')
