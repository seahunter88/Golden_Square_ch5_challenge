import math 

class DiaryEntry:
    def __init__(self, title, contents):
        if not isinstance(title, str) or not isinstance(contents, str) or not title or not contents:
            raise Exception("Diary entries must have a title and contents!")
        self.title = title
        self.contents = contents
        self.words = contents.split()
        self.current_index = 0

    def format(self):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        return len(self.words)
    
    def reading_time(self, wpm):
        if wpm <= 0:
            raise Exception("Words per minute can't be 0!")
        return math.ceil(self.count_words() / wpm)
    
    def reading_chunk(self, wpm, minutes):
        words_readable = wpm * minutes
        end_index = self.current_index + words_readable
        chunk = self.words[self.current_index:end_index]
        if end_index >= len(self.words):
            self.current_index = 0
        else:
            self.current_index = end_index
        return " ".join(chunk)
