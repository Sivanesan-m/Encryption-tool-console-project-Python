import base64

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result


def base64_encode(text):
    return base64.b64encode(text.encode()).decode()


def base64_decode(encoded_text):
    return base64.b64decode(encoded_text.encode()).decode()


def main():
    print("🔐 Welcome to Python Encryption & Decryption Tool!")

    while True:
        print("\nChoose an option:")
        print("1. Caesar Cipher Encrypt")
        print("2. Caesar Cipher Decrypt")
        print("3. Base64 Encode")
        print("4. Base64 Decode")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value (e.g. 3): "))
            print("Encrypted text:", caesar_cipher(text, shift, "encrypt"))

        elif choice == "2":
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value (e.g. 3): "))
            print("Decrypted text:", caesar_cipher(text, shift, "decrypt"))

        elif choice == "3":
            text = input("Enter text to encode (Base64): ")
            print("Encoded text:", base64_encode(text))

        elif choice == "4":
            text = input("Enter Base64 text to decode: ")
            try:
                print("Decoded text:", base64_decode(text))
            except Exception:
                print("❌ Invalid Base64 input.")

        elif choice == "5":
            print("Goodbye! 🔓")
            break
        else:
            print("Invalid choice. Please select 1–5.")


if __name__ == "__main__":
    main()
