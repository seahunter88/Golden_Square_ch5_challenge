# File: lib/diary.py

class Diary:
    def __init__(self):
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass


# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass


# TESTS:

# """
# Given an instance of DiaryEntry
# Adds the entry to the entries list
# """
# my_diary = Diary()
# my_diary.add(entry)
# self.entries == [entry]

# """
# Given that instances of DiaryEntry have been added to the entries list, all()
# Returns the entries list
# """
# my_diary = Diary()
# my_diary.add(entry)
# my_diary.all() => [entry]

# """
# When called, count_words() should
# Return an integer representing number of words in all diary entries
# """
# my_diary = Diary()
# my_diary.count_words()
# => integer (uses DiaryEntry.count_words())

"""
Given a wpm, reading_time() should
Return an integer representing reading time in minutes of all diary entries together
"""
my_diary = Diary()
my_diary.reading_time(wpm)
# => integer (time in mins, uses DiaryEntry.reading_time())

"""
Given wpm and minutes, find_best_entry_for_reading_time() should
Return instance of DiaryEntry that is closest to (but not over) the length that the user
could read in the given params 
"""
my_diary = Diary()
my_diary.find_best_entry_for_reading_time(wpm, mins)
# => entry 