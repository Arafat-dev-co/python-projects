import json 

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.is_completed =  False

    def to_dict(self):
        return{
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed
        }

    def __str__(self):
        if self.is_completed:
            status = "[X]"
        else:
            status = "[ ]"
        
        return f"{status} Title: {self.title} | Desc: {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.filename = 'tasks.json'

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file_object:
                contents = json.load(file_object)

            for content in contents:
                new_task = Task(content["title"], content["description"])
                new_task.is_completed = content["is_completed"]
                self.tasks.append(new_task)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

    def save_tasks(self):
        data_to_save = []

        for save in self.tasks:
            data_to_save.append(save.to_dict())
        with open(self.filename, 'w') as f:
            json.dump(data_to_save, f, indent=4)


    def add_task(self, task):
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks

    def mark_completed(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.is_completed = True
                return True
        return False

def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        print("---TASK MANGER---")
        print("1. Add Task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Exit")

        option = input("Choose: ")

        if option == "1":
            title = input("Enter your title: ")

            description = input("Enter your description: ")

            user = Task(title, description)

            manager.add_task(user)
            manager.save_tasks()
            print("Save Successfully")

        elif option == "2":
            user = manager.get_all_tasks()
            if len(user) == 0:
                print("No tasks found")
            else:
                for t in user:
                    print(t)
                    

        elif option == "3":
            title = input("Enter your title: ")
            success = manager.mark_completed(title)

            if success:
                manager.save_tasks()
                print("Task mark as completed!")
            else:
                print("Task not found.")

        elif option == "4":
            print("Thanks for using TASK MANAGER")
            break

        else:
            print("Invalid! Please choose from 1 - 4")

if __name__ == "__main__":
    main()