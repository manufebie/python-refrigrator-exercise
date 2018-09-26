import os, sys

greeter = '''
************************************************
****************** The Fridge ******************
************************************************
'''
my_fridge = {'top': {}, 'middle': {}, 'bottom': {}} # section of the fridge


#  clear screen when called
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# function to add new items to the fridge
def add_item(compart):
    clear()
    print(greeter)
    print('Add items to {} shelf\n'.format(compart).upper())
    
    while True:
        item = input('(ITEM)     > ')
        quantity = int(input('(QUANTITY) > '))
        total += quantity # add quantity to total_items
        new_items = {item:quantity}

        my_fridge[compart].update(new_items)
        menu_1()
        
# MAIN Menu
def display_menu():
    # Display Menu
    clear()
    print(greeter)
    print('''
[1] Add new item(s) to fridge
[2] Remove item(s) from fridge
[3] See items inside fridge
[4] Clean/Purge fridge
[5] Quit program 
    ''')
    choice = int(input('> '))

    if choice == 1:
        menu_1()
    elif choice == 2:
        remove_items()
    elif choice == 3:
        show_fridge_content()
    elif choice == 4:
        pass
    elif choice == 5:
        clear()
        sys.exit()


# First Menu
def menu_1():
    clear()
    print(greeter)
    print('''
[1] Add item(s) to TOP section
[2] Add item(s) to MIDDLE section
[3] Add item(s) to BOTTOM section
[4] See items inside fridge
[5] Back
''')
    choice = int(input('> '))
    if choice == 1:
        add_item('top')
    elif choice == 2:
        add_item('middle')
    elif choice == 3:
        add_item('bottom')
    elif choice == 4:
        show_fridge_content()
    elif choice == 5:
        display_menu()

def show_fridge_content():
    clear()
    print(greeter)
    print('[1] Show menu')
    print('bsalsnla\n')
    choice = int(input('> '))
    if choice == 1:
        display_menu()

def remove_items():
    clear()
    print(greeter)
    print('Remove items from:')
    print('''
[1] TOP Shelf
[2] MIDDLE Shelf
[3] BOTTOM Shelf
    ''')
    choice = int(input('> '))

display_menu()