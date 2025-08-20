import pytest
from lib.diary_entry import *

"""
format() method
Returns formatted diary entry 
"""
def test_format_returns_formatted_diary_entry():
    entry = DiaryEntry("My Birthday", "Details about my birthday")
    result = entry.format()
    assert result == "My Birthday: Details about my birthday"

"""
Given no title
Raises error: "Diary entries must have a title and contents!"
"""
def test_no_title_raises_error():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "Details about my birthday")
    error_message = str(e.value)
    assert error_message == "Diary entries must have a title and contents!"

"""
Given no contents
Raises error: "Diary entries must have a title and contents!"
"""
def test_no_contents_raises_error():
    with pytest.raises(Exception) as e:
        DiaryEntry("My Birthday", "")
    error_message = str(e.value)
    assert error_message == "Diary entries must have a title and contents!"

"""
Given notitle and no contents
Raises error: "Diary entries must have a title and contents!"
"""
def test_no_title_and_no_contents_raises_error():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    error_message = str(e.value)
    assert error_message == "Diary entries must have a title and contents!"

"""
count_words() method 
Returns wordcount of diary entry
"""
def test_count_words_returns_wordcount():
    entry = DiaryEntry("My sister's birthday", "Details about my sister's birthday")
    result = entry.count_words()
    assert result == 5

"""
Given contents as a non-string
Raises error: "Diary entries must be strings!"
"""
def test_contents_non_string_raises_error():
    with pytest.raises(Exception) as e:
        DiaryEntry("My Birthday", 1)
    error_message = str(e.value)
    assert error_message == "Diary entries must have a title and contents!"

"""
Given title as a non-string
Raises error: "Diary entries must be strings!"
"""
def test_title_non_string_raises_error():
    with pytest.raises(Exception) as e:
        DiaryEntry(1, "It was a really good day")
    error_message = str(e.value)
    assert error_message == "Diary entries must have a title and contents!"

"""
Given a WPM figure, reading_time() method
Returns estimate of reading time (mins) for contents rounded up to nearest integer
"""
def test_reading_time():
    entry = DiaryEntry("Holiday", "Details about my favourite holiday ever")
    result = entry.reading_time(3)
    assert result == 2

"""
Given a WPM figure, reading_time() method
Returns estimate of reading time (mins) for contents
"""
def test_reading_time_rounded():
    entry = DiaryEntry("Holiday", "Details about my favourite holiday ever")
    result = entry.reading_time(3)
    assert result == 2

"""
Given a WPM figure, reading_time() method
Returns estimate of reading time (mins) for contents
"""
def test_reading_time2():
    entry = DiaryEntry("Holiday", str("word " * 400))
    result = entry.reading_time(100)
    assert result == 4

"""
Given a WPM figure of 0
Raises error "Words per minute can't be 0!"
"""
def test_0_WPM_reading_time_raises_error():
    entry = DiaryEntry("Holiday", str("word " * 400))
    with pytest.raises(Exception) as e:
        entry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "Words per minute can't be 0!"

"""
Given a WPM figure, and a number of minutes
Returns a portion of the contents that the user can read in the timeframe
"""
def test_reading_chunk():
    entry = DiaryEntry("Holiday", " ".join("word" for i in range(0, 12)))
    result = entry.reading_chunk(6, 1)
    assert result == " ".join("word" for i in range(0, 6))

"""
Calling reading_chunk again 
Returns NEXT portion of the contents that the user can read in the timeframe
"""
def test_reading_chunk_extended():
    entry = DiaryEntry("Holiday", " ".join("word" for i in range(0, 6)) + " " +  " ".join("text" for i in range(0, 6)))
    result = entry.reading_chunk(6, 1)
    result = entry.reading_chunk(6, 1)
    assert result == " ".join("text" for i in range(0, 6))

"""
Calling reading_chunk when less of contents is left than is in a reading chunk
Returns final portion of the contents
"""
def test_reading_chunk_returns_end_of_contents():
    entry = DiaryEntry("Holiday", " ".join("word" for i in range(0, 3)) + " " +  " ".join("text" for i in range(0, 3)) + " " +  " ".join("end" for i in range(0, 3)))
    result = entry.reading_chunk(6, 1)
    result = entry.reading_chunk(6, 1)
    assert result == " ".join("end" for i in range(0, 3))