class task:
    def __init__(self, name, date_time, note=None, priority=None ): #init programme has name, was completed or no, date and priority
        self.name = name 
        self.completed = False
        self.day = date_time
        self.place = priority
        self.note = note

    def __str__(self): #if task completed, programme will print [x] before else print [ ] 
        return f"{"[x]" if self.completed else [ ]} {self.name} (priority = {self.place}, day = {self.day}, note = {self.note}"
    
    #mark cpled or not
    def mark_completed(self): 
        self.completed = True

    def mark_incompleted(self):
        self.completed = False
    
    def update_name(self, new_name):
        self.name = new_name
    
    def new_note(self, name, new_note):
        for task in self.name:
            if task == name:
                self.note = new_note

    def update_note(self, name, adding_note):
        for task in self.name:
            if task == name:
                self.note += adding_note
    




class todo:
    def __init__(self):
        self.task = []

    def new_task(self, new_task):
        self.task.append(new_task)

    def add_date(self, date_time):
        task.day = date_time

    def remove_task(self, old_task):
        for task in self.task:
            if old_task == task:
                self.task.remove(task)
    
    def view_task(self):
        if self.task == []:
            print("no task")
        else:
            for task in self.task:
                print(task)

    def check_note(self, name):
        for task in self.task:
            if task == name:
                print("note: ", f"{task.note}")
            else:
                print("task not found")
        
    def edit_task(self, old_name, new_name):
        for task in self.task:
            if task == old_name:
                task.update_name(new_name)

    def sort_priority(self):
        self.task.sort(key=lambda x: x.priority if x.priority else 0)
    
    def list_of_task_was_completed(self):
        self.list_of_task_was_completed = []
        for task in self.task: 
            self.list_of_task_was_completed.append(task)



def main():
    
    print("\n1. new task")
    print("2. view task")
    print("3. remove task")
    print("4. check note")
    print("5. edit note")
    
    choice = int(input(""))

    if choice == 1:
        name = input("task name: ")
        task1 = todo.new_task(task(name))
        print(task1)












