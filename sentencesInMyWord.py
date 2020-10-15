import timeit

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
        words = set(word_file.read().split())
    return words


theDict = load_words()  # list of words in the english dictionary

myString = input("Enter some phrase to rearrange: ")
myStringDict = {}   # keys = letters in myString, values = multiplicity of letter

# Word is valid if multiplicity of each letter does not exceed that in string
# and letter in word contained in string

# make dictionary of characters in the myString
for char in myString.replace(" ", ""):  # strip removes spaces
    if char not in myStringDict.keys():
        myStringDict[char] = 1
    else:
        myStringDict[char] += 1


# iterates over dictionary and creates a more refined list of usable words
def check_dict_words():
    validWords = []
    for word in theDict:
        # add usable words to list
        if check_word(word):
            validWords.append(word)
    return validWords

# clean function for comparing possible word to myString  returns true when it can be made from our string
def check_word(word):
    cDict = {}
    # add character counts to our dictionary
    for c in word.replace(" ", ""):
        if c not in cDict.keys():
            cDict[c] = 1  # new letters
        else:
            cDict[c] += 1  # repeated
    #  words logically have to be smaller than starting string
    if len(word) > len(myString):
        return False
    else:
        # check to see if string contains enough letters to make word returns false when we can't
        for c in word:
            if c not in myStringDict.keys():
                return False
            elif cDict[c] > myStringDict[c] != 0:
                return False
    #  if all conditions aren't met we must be able to make the word
    return True

# Start timer
start = timeit.default_timer()
# Get list of words in myString (individual words)
wordsInMyString = check_dict_words()

# Checks for full sentences made by words in myString:
def checkMultiple(prevSentenceList, fullList):
    nextSentenceList = []
 
    for s in prevSentenceList:
        for w in wordsInMyString:
            # If length of word exceeds remaining # of characters in myString, cannot use it in sentence
             if len(w) <= len(myString) - len(s):
                # If sentence found in myString and not a duplicate, add sentence to fullList
                if check_word(s.replace(" ", "") + w) and s + " " + w not in fullList:
                    fullList.append(s + " " + w)
                    nextSentenceList.append(s + " " + w)
    
    if nextSentenceList == []:
        return fullList
    else:
        return checkMultiple(nextSentenceList, fullList)
           
                
  

# Reduce dictionary down to all usable words

# find working combinations of usable words
sentencesInMyString = checkMultiple(wordsInMyString, wordsInMyString)

# sort for aesthetic purposes and display
sentencesInMyString.sort(key=len)
for s in sentencesInMyString:
    print(s)


stop = timeit.default_timer()
print('Time: ', stop - start, "Seconds")  
