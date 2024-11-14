import curses

class task:
    def __init__(self, name, date_time, note=None, priority=None ): 
        self.name = name 
        self.completed = False
        self.day = date_time
        self.place = priority
        self.note = note

    def __str__(self): 
        return f"{"[x]" if self.completed else [ ]} {self.name} (priority = {self.place}, day = {self.day}, note = {self.note})"
    
    def mark_completed(self): 
        self.completed = True

    def mark_incompleted(self):
        self.completed = False
    
    def update_name(self, new_name):
        self.name = new_name
    
    def new_note(self, new_note):
        self.note = new_note

    def new_priority(self, priority):
        self.place = priority

class todo:
    def __init__(self):
        self.task = []

    def list_task(self):
        return self.task()

    def new_task(self, new_task):
        self.task.append(new_task)

    def remove_task(self, old_task):
        for task in self.task:
            if old_task == task:
                self.task.remove(task)

    def change_date(self, name, new_date):
        for task in self.task:
            if task == name:
                task.day = new_date
        
    def new_note(self, name, new_note):
        for task in self.task:
            if task == name:
                task.day = new_note

    def add_note(self, name, add_note):
        for task in self.task:
            if task == name:
                task.note += add_note
    
    def view_task(self):
        if self.task == []:
            print("no task")
        else:
            for task in self.task:
                print(task)

    def view_note(self, name):
        for task in self.task:
            if task == name:
                print("note: ", task.note )
                return
            else:
                print("task not found")
        
    def edit_task(self, old_name, new_name):
        for task in self.task:
            if task == old_name:
                task.update_name(new_name)

    def sort_priority(self):
        task.priority.sort(key= lambda x: x.place if x.place else 0)
    
    def list_completed(self):
        self.list_completed = []
        for task in self.task: 
            if task.completed:
                self.list_completed.append(task) 

class pointer:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.stdscr.clear()
        curses.curs_set(0)

    def display(self):
        self.stdscr.clear()
        self.stdscr.addstr(0 ,0 ,"1. new task")
        self.stdscr.addstr(1 ,0 ,"2. view task")
        self.stdscr.addstr(2 ,0 ,"3. remove task")
        self.stdscr.addstr(3 ,0 ,"4. edit date")
        self.stdscr.addstr(4 ,0 ,"5. edit note")
        self.stdscr.addstr(5 ,0 ,"6.edit priority")


        for i, task in enumerate(todo.task):
            self.stdscr.addstr(i + 1, 0, str(task))
        
        self.stdscr.refresh()

    def handle_input(self):
        key = self.stdscr.getch()

        if key == ord('q'): 
            return False
        
        elif key == ord('m'): 
            task.mark_completed()

        elif key == ord('r'):  
            todo.remove_task()

        elif key == ord('1'):
            self.stdscr.clear()
            self.stdscr.addstr( 1, 0, "name task: ")
            curses.echo()

            name = self.stdscr.getstr( 02, 0, 60).decode("utf-8").strip()
            if name :
                todo.new_task.append(name)
            
            self.stdscr.refresh()
            self.stdscr.getch()

        elif key == ord('2'):
            self.stdscr.clear()
            self.stdscr.addstr( 0, 0, str(todo.view_task))

        elif key == ord('3'):
            if len(todo.list_task()) > 0:
                
                curses.echo()
                del_task = self.stdscr.getstr()

    



    

        
            
