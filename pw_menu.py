import sqlite3
from sqlite3 import Error
import pickle
from datetime import date
import pyperclip

from pw_generate import input_details, create_password
from pw_database import db_connection, create_entry, find_all, display_query, execute_query, show_database, update_entry, delete_entry

#conn = db_connection()
#cursor = conn.cursor()

def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create a new password')
    print('2. List all platforms, usernames or identifiers')
    print('3. Find your login / password details for a platform')
    print('4. Show n number of rows')
    print('5. Update/delete an entry')
    print('6. Custom search with SQL')
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
    notes = input_details('notes')

    # Create password
    combined = master + "_" + platform + "_" + username + additional
    encrypted = create_password(combined)
    
    # Store details in database
    create_entry(identifier, platform, username, additional, notes)

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
    check = True
    
    while check == True:
        nrows = input('How many rows do you want to display?')
        try: 
            nrows = int(nrows)
            if nrows > 0:
                check = False
            else: 
                print('Please try again.)
        except:
            print('Please try again.')
    
    show_database(nrows)

def update_or_delete():
    print(('-'*3) + 'What would you like to do?'+ ('-' *3))
    print('1. Update entry')
    print('2. Delete entry')
    step = int(input(": "))
    
    while step not in (1, 2):
        step = int(input(": "))

    if step == 1:
        identifier = '"' + input('Please enter the unique identifier for the entry: ') + '"'
        print(('-'*3) + 'What would you like to update?'+ ('-' *3))
        print('1. Username')
        print('2. Additional hash')
        print('3. Notes')
        field = int(input(': '))
        while field not in (1, 2, 3):
            field = int(input(': '))

        update_entry(identifier, field)
    else:
        identifier = '"' + input('Please enter the unique identifier for the entry: ') + '"'
        delete_entry(identifier)


# Option 6
def custom_search():
    query = input('Please enter a valid SQL query: ')
    print(('-'*5) + 'Displaying query results' + ('-'*5))
    display_query(query)





