from todolist import ToDoList, ToDo
import sys

class Main():
    def __init__(self):
        self.todolist = ToDoList("todolist")
        self.options = {
            '1': self.display,
            '2': self.addtask,
            '3': self.removetask,
            '4': self.quit
            }
    
    def displaymenu(self):
        '''Display to-do list menu'''
        print('''
        Welcome to To-Do List App!

        To-Do List Menu

        1. Display all tasks
        2. Add new task
        3. Remove task
        4. Quit
        ''')
    
    def run(self):
        '''Keep program in running'''
        while True:
            self.displaymenu()
            choice = input('Enter you choice: ')
            option = self.options.get(choice)
            try:
                option()
            except KeyError:
                print('Please enter valid choice')
            except TypeError:
                print('Please enter valid choice in numeric')

    def display(self):
        '''Display the tasks if there is any'''
        if len(self.todolist.todolist) > 0:
            self.todolist.display()
        else:
            print('There is no any tasks at the moment.')
    
    def addtask(self):
        '''Add task into to do list and identify potential
        value error caused by invalid deadline input'''
        task = input('Enter task: ')
        deadline = input('Enter task deadline: ')
        label = input('Enter label for this tasks: ')
        label = label.split(',')
        try:
            self.todolist.addtask(task, deadline, label)
        except ValueError:
            print('Failed to add task! Please enter valid date.')
        else:
            print('Successfully add task')
            self.todolist.save()
    
    def removetask(self):
        '''Remove task using index and detect invalid index input'''
        if len(self.todolist.todolist) > 0:
            self.todolist.display()
            delchoice = input('\nEnter task to be removed: ')
            try:
                self.todolist.removetask(int(delchoice))
            except IndexError:
                print('Please enter valid task in numeric')
            else:
                self.todolist.save()
        else:
            print('There is no any tasks at the moment.')
    
    def quit(self):
        '''Serialize file into pickle and quit'''
        self.todolist.save()
        print("Thank you for using this app.")
        sys.exit()


if __name__ == '__main__':
    Main().run()