import re

def create_dictionary():
    file = open("/usr/share/dict/words", "r")
    dictionary = []
    for word in file.readlines():
        dictionary.append(word[0:-1])
    file.close()
    return dictionary