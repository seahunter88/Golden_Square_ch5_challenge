class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            else: # This is another way to fix it, only add 1 to i if we don't remove the current letter from the string
                i += 1
        return self.text
    # THIS WAS HOW I FIXED IT:
        # new_text = ""
        # for i in self.text:
        #     if i not in self.vowels:
                # new_text += i
        # return new_text
    
remover = VowelRemover("ab")
print(remover.remove_vowels())

remover2 = VowelRemover("aeiou")
print(remover2.remove_vowels())