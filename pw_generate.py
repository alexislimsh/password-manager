from passlib.hash import sha256_crypt
from pw_secret import get_pw_salt

app_salt = get_pw_salt()
pwd_context = sha256_crypt.using(rounds=80000, salt=app_salt)

def encrypt_password(password):
    return pwd_context.hash(password)

def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

def input_master():
    master = input("What is the master password?")
    return master

def input_website():
    website = ""
    while len(website) < 3:
        website = input("What is the website name (lowercase, min 3 characters)?")
    return website

def input_username():
    username = input("What is the username/email associated?")
    return username

def create_password(string_to_hash):
    encrypted = encrypt_password(string_to_hash)
    string_to_replace = "$5$rounds=80000$" + app_salt + "$"
    encrypted_replaced = encrypted.replace(string_to_replace, "")
    return encrypted_replaced
