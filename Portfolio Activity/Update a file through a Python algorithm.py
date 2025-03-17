"""
This script manages access to a restricted subnetwork by updating an allow list of IP addresses.
It reads a file containing allowed IPs, removes the ones present in a remove list, and updates the file accordingly.

Functions used:
- open() with the with statement for safe file handling
- .read() and .write() for reading and updating file contents
- .split() to convert string data into a list
- for loop to iterate through remove list
- .remove() to delete specific IP addresses from the list

"""

from typing import List

def update_allow_list(allow_list_file: str, remove_list_file: str) -> None:
    """
    Reads the allow list file, removes IPs found in the remove list, and updates the allow list file.
    
    :param allow_list_file: Path to the file containing the allow list.
    :param remove_list_file: Path to the file containing the list of IPs to remove.
    """
    # Read the allow list file
    with open(allow_list_file, "r") as file:
        ip_addresses: List[str] = file.read().split("\n")
    
    # Read the remove list file
    with open(remove_list_file, "r") as file:
        remove_list: List[str] = file.read().split("\n")
    
    # Remove IPs found in the remove list
    for ip in remove_list:
        if ip in ip_addresses:
            ip_addresses.remove(ip)
    
    # Write the updated allow list back to the file
    with open(allow_list_file, "w") as file:
        file.write("\n".join(ip_addresses))
    
    print("Update complete: Removed specified IPs from the allow list.")

# Define file paths
import_file = "allow_list.txt"
remove_file = "remove_list.txt"

# Execute function
update_allow_list(import_file, remove_file)