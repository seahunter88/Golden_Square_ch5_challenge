from lib.todo_list import *
import pytest

"""
When instantiated, TodoList()
Creates two empty lists, "incomplete" and "complete"
"""
def test_TodoList_instantiates_empty_lists():
    my_todo_list = TodoList()
    assert my_todo_list.incomplete_tasks == []
    assert my_todo_list.complete_tasks == []

"""
Given a non-Todo-instance object (string, etc)
Raises error = "Has to be an instance of Todo()"
add() does not add object to any list
Lists remain unaffected
"""
def test_add_only_accepts_instances():
    my_todo_list = TodoList()
    with pytest.raises(Exception) as e:
        my_todo_list.add("task as a string")
    error_message = str(e.value)
    assert error_message == "Has to be an instance of Todo()"
    assert my_todo_list.incomplete_tasks == []
    assert my_todo_list.complete_tasks == []

"""
If incomplete tasks list is empty, giveup()
Raises error - "All tasks are complete!"
"""
def test_giveup_raises_error_if_no_incomplete_tasks():
    my_todo_list = TodoList()
    with pytest.raises(Exception) as e:
        my_todo_list.giveup()
    assert str(e.value) == "All tasks are complete!"