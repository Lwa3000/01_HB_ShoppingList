
shopping_list = []

def add_to_list(new_item):
    new_item = new_item.lower()
    if new_item in shopping_list:
        return 'Already on the list!'
    else:
        shopping_list.append(new_item)
        shopping_list.sort()
        return shopping_list

def remove_from_list(remove_item):
    remove_item = remove_item.lower()
    if remove_item in shopping_list:
        shopping_list.remove(remove_item)
        shopping_list.sort()
        return shopping_list
    else:
        return 'Item is not on the list :)'

def main_input():
    options = raw_input("""
        1. Add
        2. Remove
        """)
    if (options == "1" or options.lower() == 'add'):
        new_item = raw_input("What's on your shopping list?")
        print add_to_list(new_item)
    elif (options == "2" or options.lower() == 'remove'):
        print shopping_list
        remove_item = raw_input("What would you like to remove?")
        remove_from_list(remove_item)
        print shopping_list
    else:
        print 'Not an option'

main_input()
main_input()
main_input()
main_input()
main_input()
main_input()
main_input()
main_input()
main_input()
main_input()
