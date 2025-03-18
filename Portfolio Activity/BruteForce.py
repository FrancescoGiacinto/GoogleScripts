import random
import nltk
from nltk.corpus import words
import time
from typing import Tuple, Optional


def generate_key() -> int:
    """Generate a key with 16 bits.

    Returns:
        int: A 16-bit integer key (0 to 65535).
    """
    return random.randint(0, 65535)


def simple_cryptography(message: str, key: int) -> bytes:
    """Encrypt a message using XOR with a repeated 16-bit key.

    Args:
        message (str): The message to encrypt.
        key (int): A 16-bit integer key.

    Returns:
        bytes: The encrypted message as bytes.
    """
    # Convert the key to 2 bytes (16 bits)
    key_bytes = key.to_bytes(2, 'big')
    # Encode the message to bytes using UTF-8
    message_bytes = message.encode('utf-8')
    # Repeat the key to match the length of the message
    key_repeated = (key_bytes * (len(message_bytes) // len(key_bytes) + 1))[:len(message_bytes)]
    # Perform XOR between the message and the repeated key
    ciphertext = bytes([m ^ k for m, k in zip(message_bytes, key_repeated)])
    # Return the encrypted message as bytes
    return ciphertext


def simple_decrypt(ciphertext: bytes, key: int) -> str:
    """Decrypt a message using XOR with a repeated 16-bit key.

    Args:
        ciphertext (bytes): The encrypted message as bytes.
        key (int): A 16-bit integer key.

    Returns:
        str: The decrypted message as a string.
    """
    # Convert the key to 2 bytes (16 bits)
    key_bytes = key.to_bytes(2, 'big')
    # Repeat the key to match the length of the ciphertext
    key_repeated = (key_bytes * (len(ciphertext) // len(key_bytes) + 1))[:len(ciphertext)]
    # Perform XOR between the ciphertext and the repeated key
    message_bytes = bytes([c ^ k for c, k in zip(ciphertext, key_repeated)])
    
    # Attempt to decode the message to a string using UTF-8
    try:
        return message_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return ""  # Return an empty string if decoding fails


# Download the words corpus from NLTK
nltk.download('words')

# Create a set of English words for quick lookup
word_list = set(words.words())


def is_english_word(text: str) -> bool:
    """Check if a given text contains valid English words.
    
    Args:
        text (str): The text to check.
    
    Returns:
        bool: True if at least 75% of the words in the text are English, otherwise False.
    """
    # Split the text into words
    words_in_text = text.split()
    # Check if the text is empty or contains non-printable characters
    if not words_in_text or not text.isprintable():  # Ensure the text is readable
        return False # Return False if the text is empty or contains non-printable characters
    # Calculate the ratio of valid English words in the text
    ratio = sum(1 for word in words_in_text if word.lower() in word_list) / len(words_in_text)
    
    return ratio > 0.75  # Require 75% of words to be valid English



def brute_force_attack(ciphertext: bytes) ->  Tuple[Optional[int], Optional[str], int, float]:
    """
    Perform a brute-force attack to decrypt a message encrypted with a simple XOR cipher.
    
    Args:
        ciphertext (bytes): The encrypted message as a byte sequence.

    Returns:
        tuple: A tuple containing:
            - (int | None) The discovered key (None if not found).
            - (str | None) The decrypted message (None if no valid message is found).
            - (int) The total number of attempts made.
            - (float) The total time taken to complete the attack.
    """

    attempts: int = 0  # Initialize the counter for the number of decryption attempts
    start_time: float = time.time()  # Record the start time to measure execution duration

    # Iterate through all possible 16-bit keys (0 to 65535)
    for key in range(65536):  
        # Increment attempt counter for each key tested
        attempts += 1 
        # Attempt decryption with current key 
        decrypted: str = simple_decrypt(ciphertext, key)

        # Check if the decrypted message is readable and contains mostly English words
        if decrypted and decrypted.isprintable() and is_english_word(decrypted):  
            elapsed_time: float = time.time() - start_time  # Calculate elapsed time

            # Print the success message along with found key details
            print("\n===== Brute-Force Attack Successful =====")
            print(f"Key Found: {key} (Hex: {key.to_bytes(2, 'big').hex()})") 
            print(f"Decrypted Message: {decrypted}")
            print(f"Total Attempts: {attempts}")
            print(f"Time Taken: {elapsed_time:.4f} seconds")  

            return key, decrypted, attempts, elapsed_time  # Return the successful result

    # If no valid key is found, compute elapsed time and return failure message
    elapsed_time: float = time.time() - start_time
    print("\n===== Brute-Force Attack Failed =====")
    print(f"Total Attempts: {attempts}") 
    print(f"Time Taken: {elapsed_time:.4f} seconds") 

    return None, None, attempts, elapsed_time  # Return failure case (no valid key found)



# Example usage
message = "Hello world"
key = generate_key()
ciphertext = simple_cryptography(message, key)
decrypted_text = simple_decrypt(ciphertext, key)

# Display encryption details
print("\n===== Encryption Details =====")
print(f"Original Message: {message}")
print(f"Generated Key (Hex): {key.to_bytes(2, 'big').hex()}")
print(f"Ciphertext (Hex): {ciphertext.hex()}")

# Display decryption result
print("\n===== Decryption Test =====")
print(f"Decrypted Text: {decrypted_text}")

# Perform brute-force attack
brute_force_attack(ciphertext)
