"""Rudimentary implementation of the Caesar Cipher

Author: Thomas Lane
Date: 2021/12/06
"""

import pprint
import string
from typing import Dict


def generate_cipher() -> Dict[str, str]:
    """Generates a dictionary that maps each ASCII letter character to its
    scambled equivalent - shifting each character 3 positions over in string.ascii_letters

    Returns:
        Dict[str, str]: cipher dictionary with one item per ASCII letter
    """
    string.ascii_letters
    shifted_chars = string.ascii_letters[3:] + string.ascii_letters[0:3]

    cipher = {
        letter: shifted
        for (letter, shifted) in zip(string.ascii_letters, shifted_chars)
    }

    return cipher


def generate_rev_cypher(cipher: Dict[str, str]) -> Dict[str, str]:
    """
    Returns and reverse cipher to map from encrypted cipher text back to plain
    text. It creates the reverse cipher by looping over the passed cipher and
    creating a new dictionary that maps uses the value of the cipher parameter
    as the reverse cipher key and the key of the original as the reverse cipher
    value.

    Args:
        cipher (Dict[str,str]): encryption cipher to be reversed

    Returns:
        Dict[str,str]: decryption cipher that preforms the reverse mapping of
                    the input cipher
    """
    rev_cipher = {shifted: letter for letter, shifted in cipher.items()}

    return rev_cipher


def encode_message(cipher: Dict[str, str], message: str) -> str:
    """
    This function converts each letter in the message to the one specified in
    the cipher dictionary.  It then returns the transformed message. It leaves
    non-letter characters unchanged.

    Args:
        cipher (Dict[str,str]): a dictionary that maps an input character to
                                its transformed equivalent

        message (str): A string to be transformed using the cipher

    Returns:
        str: the transformed string
    """
    encoded_message = ""
    ascii_letters = set(string.ascii_letters)
    for letter in message:
        if letter in ascii_letters:
            letter = cipher[letter]
        encoded_message += letter

    return encoded_message


def main():
    """Demonstrate use of ceaser cipher module

    Create an encryption cipher dictionary using generate_cipher()
    Create an decryption cipher dictionary using generate_rev_cipher()

    """
    encryption_cipher = generate_cipher()
    decryption_cipher = generate_rev_cypher(encryption_cipher)
    print("Encryption cipher:\n")
    pprint.pprint(encryption_cipher)
    print("\nDecryption cipher:\n")
    pprint.pprint(decryption_cipher)

    plain_text = "Exams suck! But you might still learn something"
    print(f"\nHere is the original text (plain text):\n\t{plain_text}")

    cipher_text = encode_message(encryption_cipher, plain_text)
    print(f"Here is the encrypted text (cipher text):\n\t{cipher_text}")

    original_text_back = encode_message(decryption_cipher, cipher_text)
    print(f"Here is the original text after decryption:\n\t{original_text_back}")


if __name__ == "__main__":
    main()
