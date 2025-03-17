import hashlib
import os
import socket
import random
import requests
import string
from typing import List


# 1. Hash Generator

def generate_hash(file_path: str, algorithm: str = "sha256") -> str:
    """Generate the hash of a file using the specified algorithm."""
    hash_func = getattr(hashlib, algorithm, None)
    if hash_func is None:
        raise ValueError("Invalid hash algorithm.")
    
    hasher = hash_func()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)
    
    return hasher.hexdigest()

# 2. Open Ports Scanner

def scan_ports(host: str, ports: List[int]) -> List[int]:
    """Scan a list of ports on a target host and return the open ones."""
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((host, port)) == 0:
                open_ports.append(port)
    return open_ports

# 3. Check Public IP

def get_public_ip() -> str:
    """Retrieve the public IP address of the machine."""
    try:
        response = requests.get("https://api64.ipify.org?format=text", timeout=5)
        return response.text
    except requests.RequestException:
        return "Unable to retrieve IP."

# 4. Password Generator

def generate_password(length: int = 16) -> str:
    """Generate a random password with a given length."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return "".join(random.choice(characters) for _ in range(length))


# Example Usage
if __name__ == "__main__":
    # Hash Generator Example
    # print(generate_hash("example.txt"))
    
    # Port Scanner Example
    # print(scan_ports("127.0.0.1", [22, 80, 443]))
    
    # Public IP Example
    print("Public IP:", get_public_ip())
    
    # Password Generator Example
    print("Generated Password:", generate_password())
