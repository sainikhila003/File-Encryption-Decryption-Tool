from cryptography.fernet import Fernet
import os

# Generate or load key
def generate_key():
    return Fernet.generate_key()

def save_key(key, filename="secret.key"):
    with open(filename, "wb") as file:
        file.write(key)

def load_key(filename="secret.key"):
    return open(filename, "rb").read()

# Encrypt file
def encrypt_file(filename, key):
    fernet = Fernet(key)

    with open(filename, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename + ".enc", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"✅ File encrypted: {filename}.enc")

# Decrypt file
def decrypt_file(encrypted_filename, key):
    fernet = Fernet(key)

    with open(encrypted_filename, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    output_file = encrypted_filename.replace(".enc", ".dec")
    with open(output_file, 'wb') as dec_file:
        dec_file.write(decrypted)
    print(f"✅ File decrypted: {output_file}")

# Main script
if __name__ == "__main__":
    print("🔐 File Encryption & Decryption Tool")
    print("1. Generate Key\n2. Encrypt File\n3. Decrypt File")
    choice = input("Choose an option: ")

    if choice == "1":
        key = generate_key()
        save_key(key)
        print("🔑 Key generated and saved as secret.key")
    elif choice == "2":
        key = load_key()
        file_name = input("Enter the filename to encrypt: ")
        encrypt_file(file_name, key)
    elif choice == "3":
        key = load_key()
        file_name = input("Enter the encrypted filename to decrypt: ")
        decrypt_file(file_name, key)
    else:
        print("❌ Invalid option.")
