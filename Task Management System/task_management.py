import json
from datetime import datetime
import re


def add_task(tasks, task):
    """
    Adds a new task to the task list.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task (dict): The task to be added.

    Returns:
    list of dict: Updated list of tasks.json.
    """
    tasks.append(task)
    return tasks


def remove_task(tasks, task_id):
    """
    Removes a task by its ID.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be removed.

    Returns:
    list of dict: Updated list of tasks.json.
    """

    return [task for task in tasks if task['id'] != task_id]


def update_task(tasks, task_id, updated_task):
    """
    Updates an existing task.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be updated.
    updated_task (dict): The updated task details.

    Returns:
    list of dict: Updated list of tasks.json.
    """
    for task in tasks:
        if task['id'] == task_id:
            task.update(updated_task)
            break
        return tasks


def get_task(tasks, task_id):
    """
    Retrieves a task by its ID.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be retrieved.

    Returns:
    dict: The task with the specified ID, or None if not found.
    """
    for task in tasks:
        if task['id'] == task_id:
            return task
        else:
            return None


def set_task_priority(tasks, task_id, priority):
    """
    Sets the priority of a task.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be updated.
    priority (str): The new priority level.

    Returns:
    list of dict: Updated list of tasks.json.
    """
    for task in tasks:
        if task['id'] == task_id:
            task['priority'] = priority
        return tasks

def set_task_deadline(tasks, task_id, deadline):
    """
    Sets the deadline for a task.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be updated.
    deadline (str): The new deadline.

    Returns:
    list of dict: Updated list of tasks.json.
    """
    for task in tasks:
        if task['id'] == task_id:
            task['deadline'] = deadline
        return tasks

def mark_task_as_completed(tasks, task_id):
    """
    Marks a task as completed.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be marked as completed.

    Returns:
    list of dict: Updated list of tasks.json.
    """
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
        return tasks

def set_task_description(tasks, task_id, description):
    """
    Sets the description for a task.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id (int): The ID of the task to be updated.
    description (str): The new description.

    Returns:
    list of dict: Updated list of tasks.json.
    """
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
        return tasks

def search_tasks_by_keyword(tasks, keyword):
    """
    Searches tasks.json by a keyword in the description.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    keyword (str): The keyword to search for.

    Returns:
    list of dict: Tasks that contain the keyword in their description.
    """
    return [task for task in tasks if keyword in task['description']]


def filter_tasks_by_priority(tasks, priority):
    """
    Filters tasks.json by priority.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    priority (str): The priority level to filter by.

    Returns:
    list of dict: Tasks with the specified priority.
    """
    return [task for task in tasks if task['priority'] == priority]

def filter_tasks_by_status(tasks, status):
    """
    Filters tasks.json by their completion status.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    status (bool): The completion status to filter by.

    Returns:
    list of dict: Tasks with the specified completion status.
    """


def filter_tasks_by_deadline(tasks, deadline):
    """
    Filters tasks.json by their deadline.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    deadline (str): The deadline to filter by.

    Returns:
    list of dict: Tasks with the specified deadline.
    """
    return [task for task in tasks if task['deadline'] == deadline]

def count_tasks(tasks):
    """
    Returns the total number of tasks.json.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    int: The total number of tasks.json.
    """
    return len(tasks)

def count_completed_tasks(tasks):
    """
    Returns the number of completed tasks.json.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    int: The number of completed tasks.json.
    """
    return len([task for task in tasks if task['completed'] == True])

def count_pending_tasks(tasks):
    """
    Returns the number of pending tasks.json.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    int: The number of pending tasks.json.
    """
    return len([task for task in tasks if task['completed'] == False])


def generate_task_summary(tasks):
    """
    Generates a summary report of all tasks.json.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    dict: A summary report containing total, completed, and pending tasks.json.
    """
    summary = (f"Total tasks.json - {len(tasks)}; "
               f"Completed tasks.json - {len([task for task in tasks if task['completed'] == True])};"
               f"Pending tasks.json - {len([task for task in tasks if task['completed'] == False])} ")
    return summary

def save_tasks_to_file(tasks, file_path):
    """
    Saves the task list to a file.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    file_path (str): The path to the file where tasks.json will be saved.

    Returns:
    None
    """
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=2)

def load_tasks_from_file(file_path):
    """
    Loads the task list from a file.

    Parameters:
    file_path (str): The path to the file where tasks.json are saved.

    Returns:
    list of dict: The loaded list of tasks.json.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def sort_tasks_by_deadline(tasks):
    """
    Sorts tasks.json by their deadline.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    list of dict: The sorted list of tasks.json.
    """
    tasks = sorted(tasks, key=lambda task: datetime.strptime(task['deadline'], "%Y-%m-%d"))

    return tasks

def sort_tasks_by_priority(tasks):
    """
    Sorts tasks.json by their priority.

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.

    Returns:
    list of dict: The sorted list of tasks.json.
    """
    priority_order = {'low': 3, 'medium': 2, 'high': 1}
    tasks = sorted(tasks, key=lambda task: priority_order[task['priority']])
    return tasks


def priority_input_validation(priority):
    """
    Checks if the priority input is valid.

    Parameters:
    priority from input

    Returns:
    True or False
    """
    if priority != 'low' and priority != 'medium' and priority != "high":
        return False
    else:
        return True


def date_validation(date):
    """
    Checks if the input date format for the deadline is valid.

    Parameters:
    date = deadline date from input

    Returns:
    True or False
    """
    pattern = r'^\d{4}-\d{2}-\d{2}$'

    if re.match(pattern, date):
        return True
    else:
        return False


def check_id_exist(task_id, tasks):
    """
    Checks if the task ID exists

    Parameters:
    tasks.json (list of dict): The current list of tasks.json.
    task_id from input

    Returns:
    True or False
    """
    return bool([num for num in tasks if num['id'] == task_id])


def print_menu():
    """
    Prints the user menu.
    """
    menu = """
    Task Manager Menu:
    1. Add Task
    2. Remove Task
    3. Update Task
    4. Get Task
    5. Set Task Priority
    6. Set Task Deadline
    7. Mark Task as Completed
    8. Set Task Description
    9. Search Tasks by Keyword
    10. Filter Tasks by Priority
    11. Filter Tasks by Status
    12. Filter Tasks by Deadline
    13. Count Tasks
    14. Count Completed Tasks
    15. Count Pending Tasks
    16. Generate Task Summary
    17. Save Tasks to File
    18. Load Tasks from File
    19. Sort Tasks by Deadline
    20. Sort Tasks by Priority
    21. Exit
    """
    print(menu)


def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task = {
                'id': int(input("Enter task ID: ")),
                'description': input("Enter task description: "),
                'priority': input("Enter task priority (low, medium, high): ").strip().lower(),
                'deadline': input("Enter task deadline (YYYY-MM-DD): ").strip(),
                'completed': False
            }
            task_id = task['id']
            priority = task['priority']
            date_input = task['deadline']
            if not check_id_exist(task_id, tasks):
                if priority_input_validation(priority):
                    if date_validation(date_input):
                        tasks = add_task(tasks, task)
                        print("Task added successfully.")
                    else:
                        print("Invalid date format! Enter deadline in YYYY-MM-DD format!")
                else:
                    print("Invalid input! Priority should be low, medium or high")
            else:
                print("ID already exists!")
        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            if check_id_exist(task_id, tasks):
                tasks = remove_task(tasks, task_id)
                print("Task removed successfully.")
            else:
                print("Task ID doesn't exist")
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            if check_id_exist(task_id, tasks):
                updated_task = {
                    'description': input("Enter new task description: "),
                    'priority': input("Enter new task priority (low, medium, high): "),
                    'deadline': input("Enter new task deadline (YYYY-MM-DD): ")
                }
                updated_task['priority'] = priority
                updated_task['deadline'] = date_input
                if priority_input_validation(priority):
                    if date_validation(date_input):
                        tasks = update_task(tasks, task_id, updated_task)
                        print("Task updated successfully.")
                    else:
                        print("Invalid date format! Enter deadline in YYYY-MM-DD format!")
                else:
                    print("Invalid input! Priority should be low, medium or high")
            else:
                print("Task ID doesn't exist")
        elif choice == '4':
            task_id = int(input("Enter task ID to get: "))
            if check_id_exist(task_id, tasks):
                task = get_task(tasks, task_id)
                print("Task details:", task)
            else:
                print("Task ID doesn't exist")
        elif choice == '5':
            task_id = int(input("Enter task ID to set priority: "))
            priority = input("Enter new priority (low, medium, high): ")
            if check_id_exist(task_id, tasks):
                if priority_input_validation(priority):
                    tasks = set_task_priority(tasks, task_id, priority)
                    print("Task priority set successfully.")
                else:
                    print("Invalid input! Priority should be low, medium or high")
            else:
                print("Task ID doesn't exist")
        elif choice == '6':
            task_id = int(input("Enter task ID to set deadline: "))
            deadline = input("Enter new deadline (YYYY-MM-DD): ")
            if check_id_exist(task_id, tasks):
                if date_validation(deadline):
                    tasks = set_task_deadline(tasks, task_id, deadline)
                    print("Task deadline set successfully.")
                else:
                    print("Invalid date format! Enter deadline in YYYY-MM-DD format!")
            else:
                print("Task ID doesn't exist")
        elif choice == '7':
            task_id = int(input("Enter task ID to mark as completed: "))
            if check_id_exist(task_id, tasks):
                tasks = mark_task_as_completed(tasks, task_id)
                print("Task marked as completed.")
            else:
                print("Task ID doesn't exist")
        elif choice == '8':
            task_id = int(input("Enter task ID to set description: "))
            description = input("Enter new description: ")
            if check_id_exist(task_id, tasks):
                tasks = set_task_description(tasks, task_id, description)
                print("Task description set successfully.")
            else:
                print("Task ID doesn't exist")
        elif choice == '9':
            keyword = input("Enter keyword to search: ")
            found_tasks = search_tasks_by_keyword(tasks, keyword)
            print("Tasks found:", found_tasks)
        elif choice == '10':
            priority = input("Enter priority to filter by (low, medium, high): ")
            filtered_tasks = filter_tasks_by_priority(tasks, priority)
            print("Filtered tasks.json:", filtered_tasks)
        elif choice == '11':
            status = input("Enter status to filter by (completed/pending): ").lower() == 'completed'
            filtered_tasks = filter_tasks_by_status(tasks, status)
            print("Filtered tasks.json:", filtered_tasks)
        elif choice == '12':
            deadline = input("Enter deadline to filter by (YYYY-MM-DD): ")
            filtered_tasks = filter_tasks_by_deadline(tasks, deadline)
            print("Filtered tasks.json:", filtered_tasks)
        elif choice == '13':
            total_tasks = count_tasks(tasks)
            print("Total number of tasks.json:", total_tasks)
        elif choice == '14':
            completed_tasks = count_completed_tasks(tasks)
            print("Number of completed tasks.json:", completed_tasks)
        elif choice == '15':
            pending_tasks = count_pending_tasks(tasks)
            print("Number of pending tasks.json:", pending_tasks)
        elif choice == '16':
            summary = generate_task_summary(tasks)
            print("Task Summary:", summary)
        elif choice == '17':
            file_path = input("Enter file path to save tasks.json: ")
            save_tasks_to_file(tasks, file_path)
            print("Tasks saved to file.")
        elif choice == '18':
            file_path = input("Enter file path to load tasks.json from: ")
            tasks = load_tasks_from_file(file_path)
            print("Tasks loaded from file.")
        elif choice == '19':
            tasks = sort_tasks_by_deadline(tasks)
            print("Tasks sorted by deadline.")
        elif choice == '20':
            tasks = sort_tasks_by_priority(tasks)
            print("Tasks sorted by priority.")
        elif choice == '21':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
