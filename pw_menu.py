import pickle
from datetime import date
import pyperclip
from pw_generate import input_website, input_master, input_username, create_password

# Open the password dictionary
try:
    pw_dict = pickle.load( open( "passwords.pkl", "rb" ) )
except:
    print('First-time user. Creating an empty dictionary.')
    pw_dict = {}

def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create a new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Check a password for a site or app')
    print('4. View all sites and apps')
    print('Q. Exit')
    print('-'*30)
    return input(': ')

# Option 1
def create_and_store():
    # Create a dict to store pw details
    new_entry = {}
    
    # Get password details
    website = input_website()
    while website in pw_dict.keys():
        print("Entry already exists. Please enter a new identifier.")
        website = input_website()

    master = input_master()
    username = input_username()

    # Create password
    combined = master + "_" + website + "_" + username
    encrypted = create_password(combined)
    
    # Store password details
    new_entry['username'] = username
    new_entry['time_created'] = date.today()
    new_entry['website'] = website
    
    # Create new entry in passwords dictionary, save the new passwords dictionary
    pw_dict[website] = new_entry
    pickle.dump(pw_dict, open( "passwords.pkl", "wb" ) )

    # Return the password
    pyperclip.copy(encrypted)
    
    print(('-'*6) + 'Use this password:' + ('-'*6))
    print(encrypted)
    print('Copied to clipboard.')


# Option 2
def find_websites_user():
    results = []
    username = input_username()
    for k,v in pw_dict.items():
        if v['username'] == username:
            results.append(k)
    if len(results) == 0:
        print("Error. No such entry")
    else:
        print(results)

# Option 3
def find_password():
    website = input_website()
    try:
        username = pw_dict[website]['username']
        master = input_master()
        combined = master + "_" + website + "_" + username
        encrypted = create_password(combined)
        print(('-'*3) + 'This is your password:' + ('-'*3))
        print(encrypted)
    except:
        print("Error. No such entry")

# Option 4
def find_websites():
    print(('-'*10) + 'All websites' + ('-'*10))
    for k in pw_dict.keys():
        print(k)
    print(('-'*30))

