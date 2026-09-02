import hashlib
import hmac
import base64

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# ==========================================================
# AES ENCRYPTION & DECRYPTION
# ==========================================================

def aes_encrypt():
    print("\n========== AES ENCRYPTION ==========")

    message = input("Enter message: ")

    # AES requires a 16, 24 or 32-byte key
    key = get_random_bytes(32)

    cipher = AES.new(key, AES.MODE_CBC)

    encrypted_data = cipher.encrypt(
        pad(message.encode("utf-8"), AES.block_size)
    )

    # Store IV + encrypted data together
    result = cipher.iv + encrypted_data

    encoded_result = base64.b64encode(result).decode("utf-8")
    encoded_key = base64.b64encode(key).decode("utf-8")

    print("\nAES Key:")
    print(encoded_key)

    print("\nEncrypted Message:")
    print(encoded_result)

    return encoded_key, encoded_result


def aes_decrypt():
    print("\n========== AES DECRYPTION ==========")

    key_input = input("Enter Base64 AES key: ")
    encrypted_input = input("Enter Base64 encrypted message: ")

    try:
        key = base64.b64decode(key_input)
        encrypted_data = base64.b64decode(encrypted_input)

        # First 16 bytes are the IV
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        cipher = AES.new(key, AES.MODE_CBC, iv)

        decrypted_data = unpad(
            cipher.decrypt(ciphertext),
            AES.block_size
        )

        print("\nDecrypted Message:")
        print(decrypted_data.decode("utf-8"))

    except Exception as e:
        print("\nDecryption failed:", e)


# ==========================================================
# RSA KEY GENERATION
# ==========================================================

def generate_rsa_keys():
    print("\n========== RSA KEY GENERATION ==========")

    key = RSA.generate(2048)

    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("private_key.pem", "wb") as file:
        file.write(private_key)

    with open("public_key.pem", "wb") as file:
        file.write(public_key)

    print("\nRSA keys generated successfully!")
    print("Private key saved as: private_key.pem")
    print("Public key saved as: public_key.pem")


# ==========================================================
# RSA ENCRYPTION
# ==========================================================

def rsa_encrypt():
    print("\n========== RSA ENCRYPTION ==========")

    try:
        message = input("Enter message: ")

        with open("public_key.pem", "rb") as file:
            public_key = RSA.import_key(file.read())

        cipher = PKCS1_OAEP.new(public_key)

        encrypted_message = cipher.encrypt(
            message.encode("utf-8")
        )

        encoded_message = base64.b64encode(
            encrypted_message
        ).decode("utf-8")

        print("\nEncrypted RSA Message:")
        print(encoded_message)

    except FileNotFoundError:
        print("\nRSA keys not found.")
        print("Please generate RSA keys first.")


# ==========================================================
# RSA DECRYPTION
# ==========================================================

def rsa_decrypt():
    print("\n========== RSA DECRYPTION ==========")

    try:
        encrypted_input = input(
            "Enter Base64 encrypted RSA message: "
        )

        encrypted_message = base64.b64decode(
            encrypted_input
        )

        with open("private_key.pem", "rb") as file:
            private_key = RSA.import_key(file.read())

        cipher = PKCS1_OAEP.new(private_key)

        decrypted_message = cipher.decrypt(
            encrypted_message
        )

        print("\nDecrypted RSA Message:")
        print(decrypted_message.decode("utf-8"))

    except FileNotFoundError:
        print("\nPrivate key not found.")
        print("Please generate RSA keys first.")

    except Exception:
        print("\nRSA decryption failed.")


# ==========================================================
# SHA-256 HASHING
# ==========================================================

def sha256_hash():
    print("\n========== SHA-256 HASHING ==========")

    message = input("Enter message: ")

    hash_object = hashlib.sha256(
        message.encode("utf-8")
    )

    hash_value = hash_object.hexdigest()

    print("\nSHA-256 Hash:")
    print(hash_value)


# ==========================================================
# HMAC-SHA1
# ==========================================================

def hmac_sha1():
    print("\n========== HMAC-SHA1 ==========")

    key = input("Enter secret key: ")
    message = input("Enter message: ")

    hmac_value = hmac.new(
        key.encode("utf-8"),
        message.encode("utf-8"),
        hashlib.sha1
    ).hexdigest()

    print("\nHMAC-SHA1:")
    print(hmac_value)


# ==========================================================
# MAIN MENU
# ==========================================================

def main():

    while True:

        print("\n")
        print("==========================================")
        print("       CRYPTOGRAPHY ALGORITHMS TOOLKIT")
        print("==========================================")

        print("1. AES Encryption")
        print("2. AES Decryption")
        print("3. Generate RSA Keys")
        print("4. RSA Encryption")
        print("5. RSA Decryption")
        print("6. SHA-256 Hashing")
        print("7. HMAC-SHA1")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            aes_encrypt()

        elif choice == "2":
            aes_decrypt()

        elif choice == "3":
            generate_rsa_keys()

        elif choice == "4":
            rsa_encrypt()

        elif choice == "5":
            rsa_decrypt()

        elif choice == "6":
            sha256_hash()

        elif choice == "7":
            hmac_sha1()

        elif choice == "8":
            print("\nThank you for using the Cryptography Toolkit!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# ==========================================================
# PROGRAM START
# ==========================================================

if __name__ == "__main__":
    main()
