//======================================================================
// Github: https://github.com/thjsimmons
//======================================================================


#include <utility>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

extern string nospaces(string input);

class Tree {
public:
   Tree(); // default contstructor
   Tree(char c, bool e, int d); // constructor
   void add_word(string word); // add word from dictionary to tree
   vector<string> get_anagrams(string word); // get anagrams of word from dictionary
   vector<string> find_anagrams(unordered_map<char,int> chars, vector<char> path, Tree* root, int MIN_WORD_LENGTH, int MIN_SENTENCE_LENGTH);
   void print_tree(); // for testing tree structure


private:
   char chr; // node character
   bool end; // node at end of branch t/f
   int depth; // node depth
   unordered_map<char, Tree*> branches;  // nodes connected to this node
   vector<string> sentences; // get_anagrams returns anagram sentences/words

};

