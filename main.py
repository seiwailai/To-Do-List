from todolist import ToDoList, ToDo
import sys

class Main():
    def __init__(self):
        self.todolist = ToDoList("todolist")
        self.options = {
            '1': self.displayundone,
            '2': self.displaydone,
            '3': self.addtask,
            '4': self.removetask,
            '5': self.completetask,
            '6': self.quit
            }
    
    def displaymenu(self):
        '''Display to-do list menu'''
        print('''
        Welcome to To-Do List App!

        To-Do List Menu

        1. Display undone tasks
        2. Display done tasks
        3. Add new task
        4. Remove task
        5. Complete task
        6. Quit
        ''')
    
    def run(self):
        '''Keep program in running'''
        while True:
            self.displaymenu()
            choice = input('\nEnter you choice: ')
            option = self.options.get(choice)
            try:
                option()
            except KeyError:
                print('Please enter valid choice!')
            except TypeError:
                print('Please enter valid choice in numeric!')

    def displayundone(self):
        '''Display the incompleted tasks if there is any'''
        try:
            self.todolist.display('Undone')
        except Exception:
            print('There is no any incompleted tasks at the moment.')
    
    def displaydone(self):
        '''Display the completed tasks if there is any'''
        try:
            self.todolist.display('Done')
        except Exception:
            print('There is no any completed tasks at the moment.')
    
    def addtask(self):
        '''Add task into to do list and identify potential
        value error caused by invalid deadline input'''
        task = input('\nEnter task: ')
        deadline = input('Enter task deadline: ')
        label = input('Enter label for this tasks: ')
        label = label.split(',')
        label = [labels.strip(' ') for labels in label]
        try:
            self.todolist.addtask(task, deadline, label)
        except ValueError:
            print('Failed to add task! Please enter valid date.')
        else:
            print('Successfully add task.')
            self.todolist.save()
    
    def removetask(self):
        '''Remove task using index and detect invalid index input'''
        try:
            self.todolist.display('Undone')
        except Exception:
            print('There is no any incompleted tasks at the moment.')
        else:
            delchoice = input('\nEnter task to be removed: ')
            try:
                self.todolist.removetask(int(delchoice))
            except IndexError:
                print('Please enter valid task!')
                self.removetask()
            except ValueError:
                print('Please enter valid task in numeric!')
                self.removetask()
            else:
                self.todolist.save()
        
    def completetask(self):
        '''Mark completed task to Done by index'''
        try:
            self.todolist.display('Undone')
        except Exception:
            print('There is no any completed tasks at the moment.')
        else:
            taskcompleted = input('\nPlease enter completed tasks: ')
            try:
                self.todolist.completetask(int(taskcompleted))
            except IndexError:
                print('Please enter valid task!')
                self.completetask()
            except ValueError:
                print('Please enter valid task in numeric!')
                self.completetask()
            else:
                self.todolist.save()
            
    def quit(self):
        '''Serialize file into pickle and quit'''
        self.todolist.save()
        print("Thank you for using this app.")
        sys.exit()


if __name__ == '__main__':
    Main().run()