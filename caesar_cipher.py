def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a text using the Caesar Cipher algorithm.

    :param text: The input string to encrypt or decrypt.
    :param shift: The shift value for the cipher.
    :param mode: Either 'encrypt' or 'decrypt'.
    :return: The resulting encrypted or decrypted string.
    """
    if mode == 'decrypt':
        shift = -shift

    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result


def main():
    print("Caesar Cipher Program")
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")
        if choice == '3':
            print("Goodbye!")
            break

        if choice in ['1', '2']:
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value (integer): "))
            mode = 'encrypt' if choice == '1' else 'decrypt'
            result = caesar_cipher(message, shift, mode)
            print(f"\nResult: {result}")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
