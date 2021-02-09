#======================================================================
# Github: https://github.com/thjsimmons
#======================================================================

import timeit

class Tree(object): # Prefix-tree object https://en.wikipedia.org/wiki/Trie
    def __init__(self, char='', end=False, depth=0):
        self.char = char   # character at this node
        self.end = end     # bool: is last node in branch?
        self.depth = depth # node depth
        self.branches = {} # child nodes of this node (tree)
        
    def add_word(self, word): # add word into tree structure
        tree = self
        for i, char in enumerate(word): 
            if char not in tree.branches: # if character not already a branch from this node, create branch
                tree.branches[char] = Tree(char, i==len(word)-1, i+1)
            tree = tree.branches[char]    # go to new branch, continue adding characters from word

    def get_anagrams(self, word): # Get output list of anagram sentences
        chars = {}
        for char in word: # chars = dicts of characters and their multiplicities
            chars[char] = chars.get(char, 0) + 1 

        MIN_SENTENCE_LENGTH = 13 # minimum length of anagram sentence
        MIN_WORD_LENGTH = 3            # minimum length of each word in sentence
        return self.find_anagram(chars, [], self, MIN_WORD_LENGTH, MIN_SENTENCE_LENGTH) # yield generates list of sentences output

    def find_anagram(self, chars, path, root, MIN_WORD_LENGTH, MIN_SENTENCE_LENGTH): # generate anagram from user's word and prefix-tree
        # root -> root node
        # path -> list of characters on branch path
        if self.end and self.depth >= MIN_WORD_LENGTH: 
            word = ''.join(path)
            length = len(word.replace(' ', ''))

            if length >= MIN_SENTENCE_LENGTH: # if node completes a sentence of length > min word length -> append sentence
                yield word  

            path.append(' ') # else add space to list of characters, b/c sentence contains multiple words

            for word in root.find_anagram(chars, path, root, MIN_WORD_LENGTH, MIN_SENTENCE_LENGTH): # repeat to find complete sentence
                yield word
            path.pop() # if no complete sentence, move back to previous node

        for char, tree in self.branches.iteritems(): # if sentence not yet min length:
            count = chars.get(char, 0) # Multiplicity of char in user string:

            if count == 0: # if none of that char remaining, cycle to next branch
                continue

            chars[char] = count - 1 # else use char
            path.append(char) 

            for word in tree.find_anagram(chars, path, root, MIN_WORD_LENGTH, MIN_SENTENCE_LENGTH): # repeat to find complete sentence
                yield word
            path.pop() # if no complete sentence, move back to previous node
            chars[char] = count # un-use char

def unique(L): # Get only unique word combinations in sentence list from get_anagrams
    sets = []
    sents = []
    for s in L:
        st = set(s.split(' '))
        if st not in sets:
            sets.append(st)
            sents.append(s)
    return sents


def load_dictionary(path): # load dictionary words from text file
    result = Tree()
    for line in open(path, 'r'):
        word = line.strip().lower()
        result.add_word(word)
    return result

def write_sentences(my_list):
    with open('py_output', 'w') as f:
        for item in my_list:
            print >> f, item

    
def main():
    dictionary = load_dictionary('scrabble.txt') # load dictionary words into tree object
    word = raw_input('Enter word: ').lower().replace(' ', '') # User enters their word
   
    start = timeit.default_timer() # start timer

    result = dictionary.get_anagrams(word) # get_anagrams of user's word from tree
    unique_result = unique(result)         # get unique anagrams only

    count = 0
    for word in unique_result:
        print word
        count += 1

    print "Time = ", timeit.default_timer() - start, "seconds"
    print '%d results.' % count  

    write_sentences(unique_result) # write anagrams to text file 

if __name__ == '__main__':
    main()