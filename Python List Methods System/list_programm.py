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
    value = input("Insert values to extend the list (comma-separated): ").strip()
    value_to_add = [item.strip() for item in value.split(",")]
    lst.extend(value_to_add)
    print(lst)


def handle_insert(lst):
    while True:
        index = input("Insert index number: ")
        if index.isdigit():
            index = int(index)
            value = input("Insert value for that index: ")
            lst.insert(index, value)
            print(lst)
            break
        else:
            print("Please enter a number for index")


def handle_remove(lst):
    value = input("Insert value to remove: ")
    if value not in lst:
        print("value does not exist!")
    else:
        lst.remove(value)
        print(lst)


def handle_pop(lst):
    while True:
        value = input("Insert index to remove , or leave empty to remove last item: ")
        if value == '':
            lst.pop()
            print(lst)
            break
        elif value.isdigit():
            value = int(value)
            if value not in range(len(lst)):
                print("Index does not exist!")
                while True:
                    answer = input("Try again? Y/N")
                    if answer == "Y":
                        break
                    elif answer == "N":
                        return display_menu()
                    else:
                        print("Invalid answer. Chose Y for YES and N for NO . ")
            else:
                lst.pop(value)
                print(lst)
                break
        else:
            print("Please enter a number for the index, or leave empty to remove last item!")



def handle_clear(lst):
    lst.clear()
    print(f"List cleared. List : {lst}")


def handle_index(lst):
    value = input("Insert value to find its index: ")
    if value not in lst:
        print("No such value in the list!")
    else:
        index = lst.index(value)
        print(f"The index of {value} is: {index}")


def handle_count(lst):
    value = input("Type the value which you want to count: ")
    if value not in lst:
        print(f"{value} does not exist in this list!")
    else:
        count_value = lst.count(value)
        if count_value == 1:
            print(f"{value} appears {count_value} time in the list.")
        else:
            print(f"{value} appears {count_value} times in the list.")


def handle_sort(lst):
    lst.sort()
    print(lst)


def handle_reverse(lst):
    lst.reverse()
    print(lst)


def handle_copy(lst):
    copied_list = lst.copy()
    print(copied_list)


def main():
    initial_values = input("Enter initial list values (comma-separated): ").strip()
    lst = [value.strip() for value in initial_values.split(',') if value.strip()]

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
