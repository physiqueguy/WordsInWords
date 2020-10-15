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


# iterates over dictionary and creates a more refined list of usable words
def check_dict_words():
    for word in theDict:
        # add usable words to list
        if check_word(word):
            validWords.append(word)


# clean function for comparing possible word to mystring  returns true when it can be made from our string
def check_word(word):
    wDict = {}
    # add character counts to our dictionary
    for w in word.replace(" ", ""):
        if w not in wDict.keys():
            wDict[w] = 1  # new letters
        else:
            wDict[w] += 1  # repeated
    #  words logically have to be smaller than starting string
    if len(word) > len(mystring):
        return False
    else:
        # check to see if string contains enough letters to make word returns false when we can't
        for c in word:
            if c not in stringDict.keys():
                return False
            elif wDict[c] > stringDict[c] != 0:
                return False
    #  if all conditions aren't met we must be able to make the word
    return True


# checks for possible combinations of already working words
def checkMultiple():
    # iterate over words
    for word in validWords:
        # copy words to new list
        wordList.append(word)
        # loops until we have exhausted all possible combinations for a word
        while len(word) < len(mystring):
            breakit = False
            # iterate through working words to add to current word
            for w in validWords:
                # add a word if it works with current word
                if check_word(word.replace(" ", "") + w):
                    word = word + " " + w
                    wordList.append(word)
                    # breaks for loop so we go back and try for another word yet
                    break  # I think this might force it to skip particular combinations, like if we find one early on and there is one later
                # break while loop when we exhaust all options  again it works but I think we're skipping some options
                elif w == validWords[-1]:
                    breakit = True
            if breakit:  # needed to break while loop from for loop too lazy to do cleaner
                break


# Reduce dictionary down to all usable words
check_dict_words()
# find working combinations of usable words
checkMultiple()
# sort for aesthetic purposes and display
wordList.sort(key=len)
for words in wordList:
    print(words)
