# your code goes here!
class Anagram:
    def __init__(self, word):
        # self.word_letters = sorted([letter for letter in word])
        self.word = word
    
    def match(self, word_list):
            match_word_list = []
            word_letters = [letter for letter in self.word]
            for word in word_list:
                # if sorted([letter for letter in word]) == self.word_letters:
                if sorted([letter for letter in word]) == sorted(word_letters):
                    match_word_list.append(word)
        
            return match_word_list