import pickle
from pw_secret import get_app_password
from pw_menu import menu, create_and_store, view_all, find_entries, view_db, custom_search, update_or_delete
from pw_database import execute_query, create_table, alter_table 

# App login
app_pw = get_app_password()

unlock = input('Enter the master password:')

while unlock != app_pw:
    print('Wrong. Try again!')
    unlock = input('Enter the master password:')

try:
    execute_query('''SELECT * FROM passwords LIMIT 1''')

except:
    print('Table does not exist. Creating passwords table.')
    create_table()

try:
    execute_query('''SELECT notes FROM passwords LIMIT 1''')

except:
    print('You have an existing passwords table from an older version. Updating table.')
    alter_table()

# Menu
choice = menu()
while choice != 'Q':
    
    if choice == '1':
        create_and_store()
        
    elif choice == '2':
        view_all()
       
    elif choice == '3':
        find_entries()
     
    elif choice == '4':
        view_db()

    elif choice == '5':
        update_or_delete()

    elif choice == '6':
        custom_search()
       
    else:
        choice = menu()
    
    choice = menu()
exit()