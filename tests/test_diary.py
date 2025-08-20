from lib.diary import *
import pytest

"""
Initially 
Returns empty list
"""
def test_Diary_has_entries_list():
    my_diary = Diary()
    assert my_diary.entries == []

"""
Given a non-instance entry, 
add() will not add to the list of entries
raises error
"""
def test_non_instance_raises_error_Diary_can_add_to_entry_list():
    my_diary = Diary()
    with pytest.raises(Exception) as e:
        my_diary.add("this is a diary entry")
    error_message = str(e.value)
    assert error_message == "Cannot add strings to entries, only DiaryEntry() instances"
    assert my_diary.entries == []


