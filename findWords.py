def load_words():
    word_list = "list_of_58k_words.txt"  # delete later
    while True:
        break  # delete later
        prompt = input("Use 58k words or 479k?: ").lower()
        if prompt == "58" or prompt == "58k":
            word_list = "list_of_58k_words.txt"
            break
        elif prompt == "479" or prompt == "479k":
            word_list = "words_dictionary.json"
            break

    with open(word_list) as word_file:  # 58,000 most common words in english language
        valid_words = set(word_file.read().split())
    return valid_words


theDict = load_words()  # list of words in the english dictionary

mystring = input("Enter some phrase to rearrange: ")

validWords = []  # output of program

stringDict = {}  # keys = letters in mystring, values = multiplicity of letter
wordList = []  # valid words
# Word is valid if multiplicity of each letter does not exceed that in string
# and letter in word contained in string

# make dictionary of characters in the mystring
for char in mystring.replace(" ", ""):  # strip removes spaces
    if char not in stringDict.keys():
        stringDict[char] = 1
    else:
        stringDict[char] += 1


def check_dict_words():
    for word in theDict:
        if check_word(word):
            validWords.append(word)


def check_word(word):
    wDict = {}
    for w in word.replace(" ", ""):
        if w not in wDict.keys():
            wDict[w] = 1
        else:
            wDict[w] += 1
    if len(word) > len(mystring):
        return False
    else:
        for c in word:
            if c not in stringDict.keys():
                return False
            elif wDict[c] > stringDict[c] != 0:
                return False
    return True


def checkMultiple():
    for word in validWords:
        wordList.append(word)
        while len(word) < len(mystring):
            breakit = False
            for w in validWords:
                if check_word(word.replace(" ", "") + w):
                    word = word + " " + w
                    wordList.append(word)
                    break
                elif w == validWords[-1]:
                    breakit = True
            if breakit:  # needed to break while loop from for loop too lazy to do cleaner
                break


check_dict_words()
checkMultiple()
wordList.sort(key=len)
for words in wordList:
    print(words)
