import curses

class task:
    def __init__(self, name, date_time=False, note=False, priority=False ): 
        self.name = name 
        self.completed = False
        self.day = date_time
        self.place = priority
        self.note = note

    def __str__(self): 
        return f"[{"x" if self.completed else " "}] {self.name} (date : {self.day}, note : {self.note}, priority : {self.place})"

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

    def update_date(self, new_date):
        self.day = new_date


class todo:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.task = []
        self.index = 0

        curses.curs_set(0)
        self.stdscr.nodelay(1)  
        self.stdscr.timeout(100)  
        
        self.run()

    def display(self):
        self.stdscr.clear()
        self.stdscr.addstr(0 ,0 , "q to quit, arrow to change note",curses.A_BOLD)

        for i, task in enumerate(self.task):
            if i == self.index:
                self.stdscr.addstr( i + 1, 0, str(task))
            else:
                self.stdscr.addstr( i + 1, 0, str(task))

        self.stdscr.addstr(len(self.task) + 2, 0, "1. Add Task")
        self.stdscr.addstr(len(self.task) + 3, 0, "2. Remove Task")
        self.stdscr.addstr(len(self.task) + 4, 0, "3. Edit Task Name")
        self.stdscr.addstr(len(self.task) + 5, 0, "4. Edit Task Note")
        self.stdscr.addstr(len(self.task) + 6, 0, "5. Edit Task Date")
        self.stdscr.addstr(len(self.task) + 7, 0, "6. List Completed Tasks")
        self.stdscr.addstr(len(self.task) + 9, 0, "'m' to completed")

        self.stdscr.refresh()

    def handle_input(self):
        key = self.stdscr.getch()

        if key == ord('q'): 
            return False
        elif key == curses.KEY_DOWN :
            self.index = min( self.index, len(self.task) - 1)
        elif key == curses.KEY_UP :
            self.index = max( self.index, len(self.task) - 1)
        elif key == ord('1'):
            self.new_task()
        elif key == ord('2'):
            self.remove_task()
        elif key == ord('3'):
            self.change_date()
        elif key == ord('4'):
            self.new_note
        elif key == ord('5'):
            self.add_note()
        elif key == ord('6'):
            self.edit_task()
        elif key == ord('7'):
            self.list_completed()
        return True

    def new_task(self,):
        self.stdscr.clear()
        self.stdscr.addstr("name: ")
        curses.echo()
        new_task = self.stdscr.getstr(1, 0, 60).decode("utf-8").strip()
        
        if new_task :
            new_task = task(new_task)
            self.task.append(new_task)
            
            self.stdscr.clear()
            self.stdscr.addstr("add successfully")
            self.stdscr.refresh()
            self.stdscr.getch()

    def remove_task(self):
        if self.task :
            task = self.task.pop(self.index)

            if self.index() >= len(self.task) :
                self.index = len(self.task) - 1

    def change_date(self):
        if self.task :
            task = self.task[task.index]

            self.stdscr.clear()
            self.stdscr.addstr("date: ")
            curses.echo()
            new_date = self.stdscr.getstr(1, 0, 60).decode("utf-8").strip()

        if new_date :
            task.update_date(new_date)
        
    def new_note(self):
        if self.task :
            self.stdscr.clear()
            self.stdscr.addstr("new name: ")
            curses.echo()
            name = self.stdscr.getstr(1, 0, 60).decode("utf-8").strip()
        if name :
            task.update_name(name)
     
    def edit_task(self):
        if self.task :

            self.stdscr.clear()
            self.stdscr.addstr("date: ")
            curses.echo()
            new_name = self.stdscr.getstr(1, 0, 60).decode("utf-8").strip()
            
            if new_name :
                task.new_note(new_name)
    
    def list_completed(self):
        completed = [task for task in self.task if task.completed]
        self.stdscr.clear()

        self.stdscr.addstr(0, 0, "list job was completed: " )
        for i, task in enumerate(todo()):
            if i == self.index:
                self.stdscr.addstr( i + 1, 0, str(completed))

        self.stdscr.refresh()
        self.stdscr.getch()

    def run(self):
        while True:
            self.display()
            if not self.handle_input():
                break


def main(stdscr):
    app = todo(stdscr)

if __name__ == "__main__" :
    curses.wrapper(main)
