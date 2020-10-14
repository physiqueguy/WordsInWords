def load_words():
    with open('list58k.txt') as word_file: # 58,000 most common words in english language 
        valid_words = set(word_file.read().split())
    return valid_words

theDict = load_words() # list of words in the english dictionary

mystring = 'spongebob'

validWords = [] # output of program

stringDict = {} # keys = letters in mystring, values = multiplicity of letter 

# Word is valid if multiplicity of each letter does not exceed that in string
# and letter in word contained in string 

# make dictionary of characters in the mystring
for char in mystring.strip(): # strip removes spaces 
    if char not in stringDict.keys():
        stringDict[char] = 1
    else:
        stringDict[char] += 1

for word in theDict:
    wordDict = {} # keys = letters in word, values = multiplicity of letter 

    # make dictionary of characters in the word
    for char in word:
        if char not in wordDict.keys():
            wordDict[char] = 1
        else:
            wordDict[char] += 1
            
    valid = True # assume word is contained mystring 
    
    # if word is longer than mystring, word does not appear
    if len(word) > len(mystring.strip()):
        valid = False
    else:
        for char in word:
            # if word contains character not in mystring, word does not appear
            if char not in mystring:
                valid = False
                break
            # if word contains a character appearing more times than in mystring, word does not appear
            elif wordDict[char] > stringDict[char]:
                valid = False
                break 
        
    if valid == True:
        validWords.append(word)
        print(word)

