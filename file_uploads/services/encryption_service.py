from cryptography.fernet import Fernet

class EncryptionService:
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def encrypt_file(content, key):
        cipher = Fernet(key)
        return cipher.encrypt(content)

    @staticmethod
    def decrypt_file(encrypted_content, key):
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_content)
