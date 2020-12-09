import sqlite3
from sqlite3 import Error
import pickle
from datetime import date
import pyperclip

from pw_generate import input_details, create_password
from pw_database import db_connection, create_entry, find_all, display_query, execute_query, show_database

# Open the password dictionary
# try:
#     pw_dict = pickle.load( open( "passwords.pkl", "rb" ) )
# except:
#     print('First-time user. Creating an empty dictionary.')
#     pw_dict = {}

#conn = db_connection()
#cursor = conn.cursor()

def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create a new password')
    print('2. List all platforms, usernames or identifiers')
    print('3. Find your login / password details for a platform')
    print('4. Show n number of rows')
    print('5. Custom search with SQL')
    print('Q. Exit')
    print('-'*30)
    return input(': ')

# Option 1
def create_and_store():
    
    # Get list of identifiers
    query = '''SELECT identifier FROM passwords'''
    
    existing_ids = [val[0] for val in execute_query(query)]


    # Get details of the platform, unique identifier, master password and username/email
    platform = input_details('platform')
    identifier = input_details('identifier')
    while identifier.replace("'", '') in existing_ids:
        print("Entry already exists. Please enter a new identifier.")
        identifier = input_details('identifier')
    master = input_details('master_pw')
    username = input_details('username')
    additional = input_details('additional')

    # Create password
    combined = master + "_" + platform + "_" + username + additional
    encrypted = create_password(combined)
    
    # Store details in database
    create_entry(identifier, platform, username, additional)

    """ The code block below is from the dictionary version """
    # Create a dict to store pw details
    # new_entry = {}

    # Store password details
    # new_entry['username'] = username
    # new_entry['time_created'] = date.today()
    # new_entry['website'] = website
    
    # # Create new entry in passwords dictionary, save the new passwords dictionary
    # pw_dict[website] = new_entry
    # pickle.dump(pw_dict, open( "passwords.pkl", "wb" ) )

    # Return the password
    pyperclip.copy(encrypted)
    
    print(('-'*6) + 'Use this password:' + ('-'*6))
    print(encrypted)
    print('Copied to clipboard.')


# Option 2

def view_all_menu():
    print(('-'*3) + 'What would you like to view?'+ ('-' *3))
    print('1. Platforms')
    print('2. Usernames')
    print('3. Identifiers')
    return input(': ')

def view_all():
    field = int(view_all_menu())
    
    while field not in [1,2,3]:
         field = view_all_menu()
    
    find_all(field)

# Option 3
def find_entries():
    query = '''SELECT DISTINCT platform FROM passwords'''
    
    existing_platforms = [val[0] for val in execute_query(query)]

    print(existing_platforms)
    
    platform = input_details('platform')
    print(platform)

    while platform.replace("'", "") not in existing_platforms:
        print('Platform is not in database. Please search another platform.')
        platform = input_details('platform')

    query = f'''
    SELECT * FROM passwords WHERE platform = {platform}
    '''
    print(('-'*5) + f'Displaying entries for {platform}' + ('-'*5))
    display_query(query)


# Option 4

def view_db():
    nrows = int(input('How many rows do you want to display?'))
    while nrows <=0:
        nrows = int(input('How many rows do you want to display?'))
    
    
    show_database(nrows)

# Option 5
def custom_search():
    query = input('Please enter a valid SQL query')
    print(('-'*5) + 'Displaying query results' + ('-'*5))
    display_query(query)

# Option 2
# def find_platforms_user():
#     username = input_details('username')
#     query = f'''SELECT DISTINCT platform FROM passwords WHERE username = {username}
#     '''
#     display_query(query)
#     results = []
#     username = input_details('username')

#     for k,v in pw_dict.items():
#         if v['username'] == username:
#             results.append(k)
#     if len(results) == 0:
#         print("Error. No such entry")
#     else:
#         print(results)

# Option 3
# def find_password():
#     platform = input_details('platform')
    
#     # What is the website?
#     # What is the username? 
    
#     try:
#         username = pw_dict[website]['username']
#         master = input_master()
#         combined = master + "_" + website + "_" + username
#         encrypted = create_password(combined)
#         print(('-'*3) + 'This is your password:' + ('-'*3))
#         print(encrypted)
#     except:
#         print("Error. No such entry")




