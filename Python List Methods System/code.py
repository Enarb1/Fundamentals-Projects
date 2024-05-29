def display_menu():
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")


def handle_append(lst):
    value = input("Insert one value to add in the list: ")
    lst.append(value)
    print(lst)


def handle_extend(lst):
    value = input("Insert values to extend the list (comma-separated): ")
    value_to_add = value.split(", ")
    lst.extend(value_to_add)
    print(lst)


def handle_insert(lst):
    index = int(input("Insert index number: "))
    value = input("Insert value for that index: ")
    lst.insert(index, value)
    print(lst)


def handle_remove(lst):
    value = input("Insert value to remove: ")
    if value not in lst:
        print("value does not exist!")
    else:
        lst.remove(value)
        print(lst)


def handle_pop(lst):
    # TODO: Prompt the user for an index to pop (optional, leave empty to pop last item)
    # Use the pop() method to remove the item at the specified index or the last item if no index is provided
    # Handle the case where the index is out of range
    # Print the updated list
    pass


def handle_clear(lst):
    # TODO: Use the clear() method to remove all items from the list
    # Print the updated list
    pass


def handle_index(lst):
    # TODO: Prompt the user for a value to find its index
    # Use the index() method to find the index of the value
    # Handle the case where the value is not found in the list
    # Print the index of the value
    pass


def handle_count(lst):
    # TODO: Prompt the user for a value to count its occurrences in the list
    # Use the count() method to count how many times the value appears in the list
    # Print the count of the value
    pass


def handle_sort(lst):
    # TODO: Use the sort() method to sort the list in ascending order
    # Print the updated list
    pass


def handle_reverse(lst):
    # TODO: Use the reverse() method to reverse the order of the list
    # Print the updated list
    pass


def handle_copy(lst):
    # TODO: Use the copy() method to create a shallow copy of the list
    # Print the copied list
    pass


def main():
    initial_values = input("Enter initial list values (comma-separated): ")
    lst = initial_values.split(',')

    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            handle_append(lst)
        elif choice == '2':
            handle_extend(lst)
        elif choice == '3':
            handle_insert(lst)
        elif choice == '4':
            handle_remove(lst)
        elif choice == '5':
            handle_pop(lst)
        elif choice == '6':
            handle_clear(lst)
        elif choice == '7':
            handle_index(lst)
        elif choice == '8':
            handle_count(lst)
        elif choice == '9':
            handle_sort(lst)
        elif choice == '10':
            handle_reverse(lst)
        elif choice == '11':
            handle_copy(lst)
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
