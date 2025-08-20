from lib.todo import *

"""
Initialised with a task (string)
Sets up 'task' and 'complete' properties
"""
def test_todo_sets_up_properties():
    task1 = Todo("Walk dog")
    assert task1.task_name == "Walk dog"
    assert task1.complete == False

"""
When mark_complete() method runs,
"Complete" property is set to True
"""
def test_task_complete_sets_complete_to_true():
    task1 = Todo("Walk dog")
    task1.mark_complete() 
    assert task1.complete == True