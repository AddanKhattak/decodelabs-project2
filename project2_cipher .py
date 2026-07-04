# ============================================================
#  DecodeLabs Internship — Project 2
#  Advanced Encryption & Decryption (Extended Caesar Cipher)
#  Cybersecurity Analyst Track
# ============================================================
#

#
#  Printable ASCII range: 32 (space) to 126 (~)
#  Total characters      : 95
#  Formula used          : (ASCII_value - 32 + shift) % 95 + 32
# ============================================================


PRINTABLE_ASCII_START = 32    # ASCII code for space ' '
PRINTABLE_ASCII_END   = 126   # ASCII code for tilde '~'
TOTAL_PRINTABLE       = 95    # Total printable ASCII characters (126 - 32 + 1)


def encrypt_char(char, shift):
    """
    Encrypts a single character using Extended ASCII Caesar Cipher.

    Works on ALL printable ASCII characters:
    space, digits, uppercase, lowercase, symbols (@, #, !, $, %, etc.)

    Formula: encrypted = (ascii_value - 32 + shift) % 95 + 32

    Parameters:
        char  (str) : A single character to encrypt
        shift (int) : The shift key

    Returns:
        str : The encrypted character
    """
    ascii_val = ord(char)

    # Only process printable ASCII characters (32 to 126)
    if PRINTABLE_ASCII_START <= ascii_val <= PRINTABLE_ASCII_END:
        shifted   = (ascii_val - PRINTABLE_ASCII_START + shift) % TOTAL_PRINTABLE
        encrypted = shifted + PRINTABLE_ASCII_START
        return chr(encrypted)

    # Characters outside printable range (rare) pass through unchanged
    return char


def decrypt_char(char, shift):
    """
    Decrypts a single character — reverse of encrypt_char.

    Uses negative shift to reverse the transformation.

    Parameters:
        char  (str) : A single encrypted character
        shift (int) : The same shift key used during encryption

    Returns:
        str : The original character
    """
    return encrypt_char(char, -shift)


def encrypt(plaintext, shift):
    """
    Encrypts an entire message character by character.

    Parameters:
        plaintext (str) : The original message (letters, digits, symbols all supported)
        shift     (int) : The shift key (how many positions to move each character)

    Returns:
        str : The fully encrypted ciphertext
    """
    return "".join(encrypt_char(char, shift) for char in plaintext)


def decrypt(ciphertext, shift):
    """
    Decrypts an entire encrypted message back to the original.

    Parameters:
        ciphertext (str) : The encrypted message
        shift      (int) : The same shift key used during encryption

    Returns:
        str : The original plaintext message
    """
    return "".join(decrypt_char(char, shift) for char in ciphertext)


def get_encryption_map(shift, preview_chars=20):
    """
    Generates a preview of the character substitution map.
    Shows what each character becomes after encryption.

    Parameters:
        shift         (int) : The shift key
        preview_chars (int) : How many characters to preview (default 20)

    Returns:
        list of tuples : [(original, encrypted), ...]
    """
    sample = "ABCDEabcde0123456789@#!$%"
    return [(ch, encrypt_char(ch, shift)) for ch in sample[:preview_chars]]


def display_results(original, encrypted, decrypted, shift):
    """
    Displays encryption/decryption results in a clean, structured format.
    Also shows a character map preview and verification status.

    Parameters:
        original  (str) : The original plaintext
        encrypted (str) : The encrypted ciphertext
        decrypted (str) : The decrypted result (should match original)
        shift     (int) : The shift key used
    """
    width = 58

    print("\n" + "=" * width)
    print("       DECODELABS CIPHER ENGINE — PROJECT 2")
    print("       Extended ASCII Caesar Cipher")
    print("=" * width)

    print(f"\n  {'Shift Key':<18}: {shift}")
    print(f"  {'Character Range':<18}: Printable ASCII (space to ~)")
    print(f"  {'Total Characters':<18}: {TOTAL_PRINTABLE} (digits + letters + symbols)")

    print("\n" + "-" * width)
    print("  ENCRYPTION RESULTS")
    print("-" * width)
    print(f"  {'Original Text':<18}: {original}")
    print(f"  {'Encrypted Text':<18}: {encrypted}")
    print(f"  {'Decrypted Text':<18}: {decrypted}")

    print("\n" + "-" * width)
    print("  CHARACTER MAP PREVIEW (first 15 characters)")
    print("-" * width)

    char_map = get_encryption_map(shift)
    print("  " + "  ".join(f"{pair[0]}→{pair[1]}" for pair in char_map[:15]))

    print("\n" + "-" * width)
    print("  VERIFICATION")
    print("-" * width)

    if original == decrypted:
        print("  [✓]  PASSED  — Decryption perfectly matches original.")
    else:
        print("  [✗]  FAILED  — Mismatch detected. Check shift key.")

    print("=" * width + "\n")


def get_valid_shift():
    """
    Prompts user for a shift key and validates the input.
    Keeps asking until a valid integer is entered.

    Returns:
        int : A valid shift value
    """
    while True:
        try:
            shift = int(input("  Enter shift key (e.g. 7):    "))
            if shift == 0:
                print("  [!] Shift key 0 means no encryption. Please enter a non-zero value.")
                continue
            return shift
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")


def get_valid_message():
    """
    Prompts user for a message and ensures it is not empty.

    Returns:
        str : A non-empty message string
    """
    while True:
        message = input("  Enter the message to encrypt: ")
        if message.strip():
            return message
        print("  [!] Message cannot be empty. Please try again.")


# ---------------------------------------------------------------
#  MAIN PROGRAM
# ---------------------------------------------------------------

def main():
    """
    Entry point — handles user interaction and runs the cipher pipeline:
    Input → Encrypt → Decrypt → Display → Verify
    """
    header = "=" * 58
    print(f"\n{header}")
    print("    DecodeLabs — Extended Encryption & Decryption")
    print("    Supports: Letters  |  Digits  |  Symbols")
    print(f"{header}\n")

    message   = get_valid_message()
    shift     = get_valid_shift()

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    display_results(message, encrypted, decrypted, shift)


if __name__ == "__main__":
    main()
