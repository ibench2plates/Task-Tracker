tasks = []

def add_task(task):
    tasks.append({'task': task, 'completed': False})


def view_tasks():
    if not tasks:
        print("You have no tasks!")
    else:
        index = 1
        for task in tasks:
            status = "Completed" if task['completed'] else "Incomplete"
            print(f"{index}. {task['task']} - {status}")
            index += 1


def mark_complete(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        print("Task marked as complete.")
    else:
        print("Invalid task index.")

while True:
    print("\nTask Tracker Menu:")
    print("A. Add Task")
    print("V. View Tasks")
    print("D. Mark Task as Complete")
    print("Q: Quit")

    choice = input("Enter your choice: ")

    if choice == 'A':
        task_name = input("Enter task name: ")
        if task_name == 'Q':
            print("Exiting Task Tracker. Goodbye!")
            break
        add_task(task_name)

    elif choice == 'V':
        view_tasks()

    
    elif choice == 'D':
        task_index = int(input("Enter task number to mark as complete: "))
        mark_complete(task_index)
        print("Good Job! You have completed the task")
        else:
            print("Invalid task index. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task index.")


    elif choice == 'Q':
        print("Exiting Task Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

