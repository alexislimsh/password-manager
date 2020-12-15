import sqlite3
from sqlite3 import Error
from datetime import date
from prettytable import PrettyTable

## To add in find password, list all websites, find websites based on username

def db_connection():
    try:

        conn = sqlite3.connect('password-db.db')
        
        return conn

    except Error:

        print(Error)

conn = db_connection()
cursor = conn.cursor()

# Display and query functions
def display_table(headers, rows):
    table = PrettyTable()
    table.field_names = headers
    for r in rows:
        table.add_row(r)
    print(table)

def execute_query(query):
    return cursor.execute(query).fetchall()

def display_query(query):
    rows = execute_query(query)
    headers = [cn[0] for cn in cursor.description]
    display_table(headers, rows)

# Create and alter table
def create_table():
    
    query = '''
    CREATE TABLE IF NOT EXISTS passwords(identifier TEXT PRIMARY KEY, 
                                         date_created TEXT,
                                         platform TEXT, 
                                         username TEXT,
                                         additional TEXT,
                                         notes TEXT);
    '''
    cursor.execute(query)
    conn.commit()

def alter_table():
    query = '''
    ALTER TABLE passwords
    ADD COLUMN notes TEXT
     '''
    execute_query(query)
    conn.commit()

# Show entire database - provide no. of rows
def show_database(nrows=5):
    query = f'''
    SELECT * FROM passwords
    LIMIT {nrows}
    '''
    
    display_query(query)

# Create password and store

def create_entry(identifier, platform, username, additional, notes):
    created_date = "'" + date.today().strftime('%d/%m/%Y') + "'"
    query = f'''
    INSERT INTO passwords VALUES({identifier}, {created_date}, {platform}, {username}, {additional}, {notes})
    '''
    
    cursor.execute(query)
    conn.commit()

    print(('-'*6) + 'The following entry was created' + ('-'*6))
    
    query = f'''SELECT * FROM passwords WHERE identifier = {identifier}'''
    display_query(query)
    print('Note: Master password is not saved.')

# List all platforms in database. List all identifiers / usernames also.

def find_all(field = 1):
    field_dict = {1: 'platform', 2: 'username', 3: 'identifier'}
    field_v = field_dict[field]
    
    print(('-'*5) + f'Displaying all values for {field_v}' + ('-'*5))
    query = f'''
    SELECT DISTINCT {field_v} FROM passwords
    '''
    display_query(query)

# Update and delete entries
def update_entry(identifier, field):
    
    field_dict = {1: 'username', 2: 'additional', 3: 'notes'}
    field_v = field_dict[field]

    print('The current value is:')

    query = f'''
    SELECT {field_v} FROM passwords WHERE identifier = {identifier}
    '''
    display_query(query)

    new_val = '"' + input('Please enter the new value: ') + '"'

    query = f'''
    UPDATE passwords
    SET {field_v} = {new_val}
    WHERE
    identifier = {identifier}
    '''
    execute_query(query)
    conn.commit()

    print(f'The entry for {identifier} has been updated.')

    query = f'''
    SELECT * FROM passwords WHERE identifier = {identifier}
    '''
    
    display_query(query)


def delete_entry(identifier):
    print(f'Are you sure you want to delete the entry for {identifier}?')
    double_check = input(f'Please enter {identifier} to confirm: ')
    
    while double_check != identifier.replace('"', ''):
        double_check = input(f'Wrong! Please enter {identifier} to confirm or enter N to return: ')
        if double_check == '"N"':
            return
    
    query = f'''
    DELETE FROM passwords
    WHERE identifier = {identifier}
    '''
    execute_query(query)
    conn.commit()

    print(f'The entry for {identifier} has been deleted.')






