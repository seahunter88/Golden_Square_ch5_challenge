import pytest
from lib.diary import *
from lib.diary_entry import *

"""
Given an instance of DiaryEntry
Adds the entry to the entries list
"""
def test_diary_can_add_instance_of_diary_entry():
    all_diaries = Diary()
    sarahs_diary = DiaryEntry("My title", "My contents")
    all_diaries.add(sarahs_diary)
    assert all_diaries.entries == [sarahs_diary]

"""
Given thatan instance of DiaryEntry have been added to the entries list, all()
Returns the entries list
"""
def test_all_returns_entries_list():
    my_diary = Diary()
    gees_diary = DiaryEntry("Day 1", "Anna and Birdy")
    my_diary.add(gees_diary)
    result = my_diary.all()
    assert result == [gees_diary]

"""
Given that multiple instances of DiaryEntry have been added to the entries list, all()
Returns the entries list
"""
def test_all_returns_entries_list_multiple_entries():
    my_diary = Diary()
    gees_diary = DiaryEntry("Day 1", "Anna and Birdy")
    sarahs_diary = DiaryEntry("Christmas", "Details about christmas")
    my_diary.add(gees_diary)
    my_diary.add(sarahs_diary)
    result = my_diary.all()
    assert result == [gees_diary, sarahs_diary]

"""
When called, count_words() should
Return an integer representing number of words in all diary entries
"""
def test_count_words_returns_total_words_in_entries_list():
    my_diary = Diary()
    gees_diary = DiaryEntry("Day 1", "Anna and Birdy")
    sarahs_diary = DiaryEntry("Christmas", "Details about christmas")
    my_diary.add(gees_diary)
    my_diary.add(sarahs_diary)
    result = my_diary.count_words()
    assert result == 6

"""
Given a wpm, reading_time() should
Return an integer representing reading time in minutes of all diary entries together
"""
def test_reading_time_returns_total_reading_time():
    my_diary = Diary()
    gees_diary = DiaryEntry("Day 1", "Anna and Birdy")
    sarahs_diary = DiaryEntry("Christmas", "Details about christmas")
    my_diary.add(gees_diary)
    my_diary.add(sarahs_diary)
    result = my_diary.reading_time_total(2)
    assert result == 4 # NOTE: this is '4' because I am rounding each entry up to the nearest minute, so these would be 2mins each (really 1.5mins)

"""
Given a wpm and minutes, find_best_entry_for_reading_time(),
Returns a DiaryEntry instance that is the closest to, but not over, the length the user could read in the params
"""
def test_find_best_reading_time_returns_best_entry():
    my_diary = Diary()
    day_1 = DiaryEntry("Day 1", "This is the contents about day 1")
    day_2 = DiaryEntry("Day 2", "Here are some more details about day 2 in a longer entry")
    day_3 = DiaryEntry("Day 3", "Short day")
    my_diary.add(day_1)
    my_diary.add(day_2)
    my_diary.add(day_3)
    result = my_diary.find_best_entry_for_reading_time(2, 4)
    assert result == "Day 1: This is the contents about day 1"

"""
Given a wpm and minutes, find_best_entry_for_reading_time(),
Returns a DiaryEntry instance that is the closest to, but not over, the length the user could read in the params
"""
def test_find_best_reading_time_returns_best_entry2():
    my_diary = Diary()
    day_1 = DiaryEntry("Day 1", "This is the contents about day 1")
    day_2 = DiaryEntry("Day 2", "Here are some more details about day 2 in a longer entry")
    day_3 = DiaryEntry("Day 3", "Short day")
    my_diary.add(day_1)
    my_diary.add(day_2)
    my_diary.add(day_3)
    result = my_diary.find_best_entry_for_reading_time(2, 1)
    assert result == "Day 3: Short day"

"""
Given a wpm and minutes, find_best_entry_for_reading_time(),
Returns a DiaryEntry instance that is the closest to, but not over, the length the user could read in the params
"""
def test_find_best_reading_time_returns_best_entry3():
    my_diary = Diary()
    day_1 = DiaryEntry("Day 1", "This is the contents about day 1")
    day_2 = DiaryEntry("Day 2", "Here are some more details about day 2 in a longer entry")
    day_3 = DiaryEntry("Day 3", "Short day")
    my_diary.add(day_1)
    my_diary.add(day_2)
    my_diary.add(day_3)
    result = my_diary.find_best_entry_for_reading_time(2, 2)
    assert result == "Day 3: Short day"

"""
Given a wpm and minutes, find_best_entry_for_reading_time(),
Returns a DiaryEntry instance that is the closest to, but not over, the length the user could read in the params
"""
def test_find_best_reading_time_returns_best_entry4():
    my_diary = Diary()
    day_1 = DiaryEntry("Day 1", "This is the contents about day 1")
    day_2 = DiaryEntry("Day 2", "Here are some more details about day 2 in a longer entry")
    day_3 = DiaryEntry("Day 3", "Short day")
    my_diary.add(day_1)
    my_diary.add(day_2)
    my_diary.add(day_3)
    result = my_diary.find_best_entry_for_reading_time(3, 7)
    assert result == "Day 2: Here are some more details about day 2 in a longer entry"

"""
Given there are two instances of same reading time but different word lengths, find_best_entry_for_reading_time(),
Returns a DiaryEntry instance that is the longest length
"""
def test_find_best_reading_time_returns_best_entry5():
    my_diary = Diary()
    day_1 = DiaryEntry("Day 1", "This is the contents about day 1, it was very nice")
    day_2 = DiaryEntry("Day 2", "Here are some more details about day 2 in a longer entry")
    my_diary.add(day_1)
    my_diary.add(day_2)
    result = my_diary.find_best_entry_for_reading_time(3, 4)
    assert result == "Day 2: Here are some more details about day 2 in a longer entry"