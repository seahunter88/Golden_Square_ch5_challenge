from lib.todo import *
from lib.todo_list import *

"""
Given an instance of Todo, if task is not completed, add()
Adds the contents of the instance (task) to the incomplete list
"""
def test_add_takes_Todo_instance_and_adds_to_incomplete_list():
    task1 = Todo("Walk the dog")
    my_todo_list = TodoList()
    my_todo_list.add(task1)
    assert my_todo_list.incomplete_tasks == ["Walk the dog"]
    assert my_todo_list.complete_tasks == []

"""
Given an instance of Todo, if task is completed, add()
Adds the contents of the instance (task) to the complete list
"""
def test_add_takes_Todo_instance_and_adds_to_complete_list():
    task1 = Todo("Walk the dog")
    task1.mark_complete()
    my_todo_list = TodoList()
    my_todo_list.add(task1)
    assert my_todo_list.complete_tasks == ["Walk the dog"]
    assert my_todo_list.incomplete_tasks == []

"""
Given that tasks have been added to the TodoList, incomplete() 
Returns a list of the names of the tasks that are incomplete
"""
def test_incomplete_returns_incomplete_tasks():
    task1 = Todo("Walk the dog")
    my_todo_list = TodoList()
    my_todo_list.add(task1)
    assert my_todo_list.incomplete() == ["Walk the dog"]

"""
Given that tasks have been completed, complete()
Returns a list of the names of the tasks that are complete
"""
def test_complete_returns_complete_tasks_list():
    task1 = Todo("Walk the dog")
    task1.mark_complete()
    my_todo_list = TodoList()
    my_todo_list.add(task1)
    assert my_todo_list.complete() == ["Walk the dog"]
    assert my_todo_list.incomplete() == []

"""
Given that there are incomplete tasks, giveup()
Marks all tasks as complete
"""
def test_giveup_marks_all_tasks_as_complete():
    task1 = Todo("Walk the dog")
    task2 = Todo("Clean the bathroom")
    my_todo_list = TodoList()
    my_todo_list.add(task1)
    my_todo_list.add(task2)
    my_todo_list.giveup()
    assert my_todo_list.complete() == ["Walk the dog", "Clean the bathroom"]
    assert my_todo_list.incomplete() == []