from passlib.hash import sha256_crypt
from pw_secret import get_pw_salt

app_salt = get_pw_salt()
pwd_context = sha256_crypt.using(rounds=80000, salt=app_salt)

def encrypt_password(password):
    return pwd_context.hash(password)

def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

def input_details(field='identifer'):
    answer = ""
    if field == 'master_pw':
        while len(answer) < 3:
            answer = input("What is the master password? (min 3 characters) ")

    elif field == 'platform':
        while len(answer) < 3:
            answer = input("What is the platform name? (lowercase, min 3 characters) ")

    elif field == 'identifier':
        while len(answer) < 3:
            answer = input("REQUIRED: Please enter a unique identifier for the database (min 3 chars) ")

    elif field == 'username':
        while len(answer) < 5:
            answer = input("What is the username/email? (min 5 characters) ")

    elif field == 'additional':
        answer = input('OPTIONAL: Please give an additional hash changer. ')
    
    elif field == 'notes':
        answer = input('OPTIONAL: Please add any notes for the entry.  ')

    else:
        print("Error, input field is wrong.")
    
    return '"' + answer + '"'


# def input_master():
#     master = 
#     return master

# def input_website():
    
#     return website

# def input_identifier():
#     identifier = ""
#     while len(identifier) <

# def input_username():
#     username = ""
#     while len(username) < 5:
#         username = input("What is the username/email associated? (min 5 characters)")
#     return username

def create_password(string_to_hash):
    encrypted = encrypt_password(string_to_hash)
    string_to_replace = "$5$rounds=80000$" + app_salt + "$"
    encrypted_replaced = encrypted.replace(string_to_replace, "")
    return encrypted_replaced



