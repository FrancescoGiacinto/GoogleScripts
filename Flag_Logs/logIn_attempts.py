from typing import List

def read_log_file(file_path: str) -> List[str]:
    """
    Reads a log file and returns a list of usernames representing failed login attempts.
    
    :param file_path: Path to the log file.
    :return: List of usernames from the log file.
    """
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Error: The log file was not found.")
        return []

def count_failed_attempts(login_list: List[str], current_user: str) -> int:
    """
    Counts the number of failed login attempts for a specific user.
    
    :param login_list: List of usernames representing failed login attempts.
    :param current_user: The username to check.
    :return: The count of failed login attempts for the user.
    """
    counter = 0
    for username in login_list:
        if username == current_user:
            counter += 1
    return counter

def login_check(login_list: List[str], current_user: str) -> None:
    """
    Checks if a user has had three or more failed login attempts and prints an alert.
    
    :param login_list: List of usernames representing failed login attempts.
    :param current_user: The username to check.
    """
    failed_attempts = count_failed_attempts(login_list, current_user)
    
    if failed_attempts >= 3:
        print(f"ALERT: Account for user '{current_user}' is locked due to multiple failed login attempts.")
    else:
        print(f"User '{current_user}' can log in. Failed attempts: {failed_attempts}")

# Example usage
if __name__ == "__main__":
    log_file_path = "failed_logins.txt"  # Example log file
    login_attempts = read_log_file(log_file_path)
    
    # Example check for a specific user
    user_to_check = "eraab"
    login_check(login_attempts, user_to_check)
