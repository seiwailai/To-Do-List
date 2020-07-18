from datetime import datetime
import pickle


class ToDoList():
    '''Initialize list containing to-do objects. Specifically,
    we check on existence of serialized database in pickle format
    and deserialize database into a list. If the serialized database
    is empty, we then create an empty to-do list. If the
    serialized database file is not found, we create an empty
    to-do list and notify user new datafile is being created.
    '''
    def __init__(self, datafile):
        try:
            with open(datafile, 'rb') as file:
                self.todolist = pickle.load(file)
        except EOFError:
            self.todolist = {}
            self.todolist.setdefault('Done', [])
            self.todolist.setdefault('Undone', [])
        except FileNotFoundError:
            self.todolist = {}
            self.todolist.setdefault('Done', [])
            self.todolist.setdefault('Undone', [])
            print(f"Created new datafile named {datafile}")
        
    def addtask(self, task, deadline, label=[]):
        '''Create to-do object containing several attributes
        and append to our existing to-do list'''
        newtask = ToDo(task, deadline, label)
        self.todolist['Undone'].append(newtask)
    
    def removetask(self, index):
        '''Remove task by index'''
        index = index - 1
        removedtask = self.todolist['Undone'].pop(index)
        print(f'{removedtask.task} is removed')
    
    def completetask(self, index):
        '''Change progress of completed task to Done'''
        index = index - 1
        self.todolist['Undone'][index].completed = 'Done'
        tempfile = self.todolist['Undone'].pop(index)
        self.todolist['Done'].append(tempfile)
    
    def display(self, progress):
        '''Display undone tasks with appropriate paddings and alignment'''
        if len(self.todolist[progress]) > 0:
            print(f"{'No':<2} | {'Activity':^30} {'Deadline':^10} {'Tags':^30} {'Progress'}")
            print('-'*87)
            for index, tasks in enumerate(self.todolist[progress]):
                labels = ', '.join(tasks.label)
                print(f'{str(index+1):<2} | {tasks.task:<30} {datetime.strftime(tasks.deadline, "%d-%m-%Y"):<10} {labels:^30} {tasks.completed:^8}')
        else:
            raise Exception
    
    def save(self):
        '''Serialize to-do objects into pickle file'''
        with open("todolist", 'wb') as file:
            pickle.dump(self.todolist, file)
        

class ToDo():
    def __init__(self, task, deadline, label=[]):
        '''Initiate to-do task with several attributes'''
        self.task = task
        self.createdtime = datetime.now()
        self.deadline = datetime.strptime(deadline, "%d/%m/%Y")
        self.label = list(label)
        self.completed = "Undone"