# File: lib/diary.py
from lib.diary_entry import *

class Diary():
    def __init__(self):
        self.entries = []

    def add(self, entry):
        if not isinstance(entry, DiaryEntry):
            raise Exception("Cannot add strings to entries, only DiaryEntry() instances")
        else:
            self.entries.append(entry)

    def all(self):
        return list(self.entries)
    
    def count_words(self):
        total_words = 0
        for i in self.entries:
            total_words += i.count_words()
        return total_words
    # ALTERNATIVE - REFACTORED:
        # return sum([i.count_words() for i in self.entries])
    
    def reading_time_total(self, wpm):
        time = 0
        for i in self.entries:
            time += i.reading_time(wpm)
        return time
    
    def find_best_entry_for_reading_time(self, wpm, mins):
        # Refactored my work to make it scalable and return longest (word_length) readable entry
        words_readable = wpm * mins
        entry_lengths = {}
        for entry in self.entries:
            entry_lengths[entry] = entry.count_words()
        best_entry = max((k for k, value in entry_lengths.items() if value <= words_readable), 
                            key = lambda k: entry_lengths[k], 
                            default = None)
        answer = best_entry.format()
        return answer

    # KAY'S ANSWER:
        # words_readable = wpm * mins
        # best_entry = None
        # entry_length = 0
        # for entry in self.entries:
        #     if entry.count_words() <= words_readable:
        #         if entry.count_words() > entry_length:
        #             best_entry = entry
        #             entry_length = entry.count_words()
        # answer = best_entry.format()
        # return answer

    # INITIAL THOUGHTS FOR THIS METHOD:
    # Passes tests but wouldn't differentiate between two entries of slightly different word lengths with same reading time (want to return the longer one)
        # reading_times = {}
        # for entry in self.entries:
        #     reading_times[entry] = entry.reading_time(wpm)
        # best_entry = max((k for k, value in reading_times.items() if value <= mins), 
        #                     key = lambda k: reading_times[k], 
        #                     default = None)
        # answer = best_entry.format()
        # return answer
    
    """
    ___EXPLAINING THE find_best_entry_for_reading_time() METHOD:____
    
    reading_times = {} -> creates an empty dictionary to store each DiaryEntry instance and their reading time

    for entry in self.entries -> loops through the items in the list of DiaryEntry instances

    reading_times[entry] = entry.reading_time(wpm) -> uses the reading_time() method from the DiaryEntry class to calculate the reading time for each entry, assigns this as the value to the corresponding key within reading_times

    best_entry -> 

        (k for k, value in reading_times.items()...) -> loops over the keys and values in the .items() list of tuples, only keeps the keys

        (...if value <= mins) -> filters the keys on a condition, only keeps k if its value is less than or equal to the value of mins

        max(..., key = lambda k: reading_times[k]) -> as max() can't directly compare class instances, we use a key and a lambda function to tell Python what to compare (the values associated with the keys it wants to compare)

    best_entry.format() -> Uses the format() method from DiaryEntry class to return the best_entry in a human-readable manner

    """
    