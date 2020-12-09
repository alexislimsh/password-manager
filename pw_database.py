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

def create_table():
    
    query = '''
    CREATE TABLE IF NOT EXISTS passwords(identifier TEXT PRIMARY KEY, 
                                         date_created TEXT,
                                         platform TEXT, 
                                         username TEXT,
                                         additional TEXT);
    '''
    cursor.execute(query)
    conn.commit()

# Show entire database - provide no. of rows
def show_database(nrows=5):
    query = f'''
    SELECT * FROM passwords
    LIMIT {nrows}
    '''
    
    display_query(query)

# Create password and store
def create_entry(identifier, platform, username, additional):
    created_date = "'" + date.today().strftime('%d/%m/%Y') + "'"
    query = f'''
    INSERT INTO passwords VALUES({identifier}, {created_date}, {platform}, {username}, {additional})
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


# Execute custom SQL query?

# Find password - need to check for the username


    # What is the website?


# Change password - should we add a unique hash changer?





