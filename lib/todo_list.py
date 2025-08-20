from lib.todo import *

class TodoList():

    def __init__(self):
        self.incomplete_tasks = []
        self.complete_tasks = []

    def add(self, task):
        if not isinstance(task, Todo):
            raise Exception("Has to be an instance of Todo()")
        if task.complete == False:
            self.incomplete_tasks.append(task.task_name)
        else:
            self.complete_tasks.append(task.task_name)

    def incomplete(self):
        return self.incomplete_tasks

    def complete(self):
        return self.complete_tasks
    
    def giveup(self):
        if len(self.incomplete_tasks) > 0:
            for i in self.incomplete_tasks:
                self.complete_tasks.append(i)
            self.incomplete_tasks = []
        else:
            raise Exception("All tasks are complete!")