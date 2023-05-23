class Anagram:
    def __init__(self, word):
        if word in word:
            self.word = word

    def match(self, list):
        match_list = []
        for i in list:
            if sorted(self.word) == sorted(i):
                match_list.append(i)
        return match_list
                