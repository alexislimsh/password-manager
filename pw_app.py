import pickle
from pw_secret import get_app_password
from pw_menu import menu, create_and_store, find_websites_user, find_password, find_websites

# App login
app_pw = get_app_password()

unlock = input('Enter the master password:')

while unlock != app_pw:
    print('Wrong. Try again!')
    unlock = input('Enter the master password:')

# Menu
choice = menu()
while choice != 'Q':
    
    if choice == '1':
        create_and_store()
        
    elif choice == '2':
        find_websites_user()
       
    elif choice == '3':
        find_password()
     
    elif choice == '4':
        find_websites()
       
    else:
        choice = menu()
    
    choice = menu()
exit()