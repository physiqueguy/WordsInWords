//======================================================================
// Github: https://github.com/thjsimmons
//======================================================================

#include "Tree.h"

string nospaces(string input) // remove spaces from string
{
   string output = input;

   for (int i = output.length()-1; i >= 0; --i) {
      if(output[i] == ' ')
         output.erase(i, 1);
   }
   return output;
}

Tree::Tree(){ // default constructor
   // char c empty
   end = false;
   depth = 0;
}

Tree::Tree(char c, bool e, int d){ // constructor
   chr = c;
   end = e;
   depth = d;
}

void Tree::add_word(string word) { // file dictionary words into prefix tree
   Tree* tree = this;
   unordered_map<char, int> chars;

   for(int i = 0; i < word.length(); i++){

      const char c = word[i];

      if (tree->branches.find(c) == tree->branches.end()) { // if character not a branch from node
         tree->branches.insert(make_pair(c, new Tree(c, i==word.length()-1, i+1))); // insert new node
      }
      tree = tree->branches.find(c)->second; // go to new node
   }
}

void Tree::print_tree(){ // recursive node character print function for testing tree structure
   for (auto const& pair: this->branches){
      char c = pair.first;
      cout << "char = " << c << endl; // print character at node
      Tree* tree = pair.second;
      tree->print_tree();             // print characters in branches
   }
}

vector<string> Tree::get_anagrams(string word){ // get vector<string> anagrams of word
   unordered_map<char, int> chars; // e.g. convert 'ball' to {{'a':1}, {'b':1'}, {'l':2}}

   for (char c: word)
   {
      unordered_map<char,int>::iterator it = chars.find(c);

      if (chars.find(c) != chars.end()) { // if character already in chars
         it->second++;    // increment that character's multiplicity
      }
      else {
         chars.insert(std::make_pair(c, 1)); // else add new character
      }
   }

   vector<char> path; // holds char path through prefix tree
   int MIN_SENTENCE_LENGTH =word.length(); // min length of anagram sentence
   int MIN_WORD_LENGTH = 1;   // min length of each word in sentence

   return this->find_anagrams(chars, path, this, MIN_WORD_LENGTH, MIN_SENTENCE_LENGTH);
}

vector<string> Tree::find_anagrams(unordered_map<char,int> chars, vector<char> path, Tree* root, int MIN_WORD_LENGTH, int MIN_SENTENCE_LENGTH){
   // recursively collect anagram sentences
   if (this->end && this->depth >= MIN_WORD_LENGTH){ // if node is end of branch and sufficient length

      string word;
      for (char c: path) {
         word.push_back(c);
      }

      if (nospaces(word).length() >= MIN_SENTENCE_LENGTH){
         root->sentences.push_back(word); // yield word
      }

      path.push_back(' '); // word complete, ' ', next word in sentence (going forward a node)

      for (auto word : root->find_anagrams(chars, path, root, MIN_WORD_LENGTH, MIN_SENTENCE_LENGTH)){
         this->sentences.push_back(word); // yield word
      }
      root->sentences.clear(); // clear generator
      path.pop_back(); // going back a node ...
   }

   unordered_map<char,Tree*>::iterator it;

   for (it = this->branches.begin(); it != this->branches.end(); it++){ // search for continuations

      char c = it->first;
      Tree* tree = it->second;

      int count;

      if (chars.find(c) == chars.end()){
         count = 0;
      }
      else{
         count = chars.find(c)->second;
      }

      if (count == 0){ // if character not found in branches, goto next branch
         continue;
      }

      chars.find(c)->second = count - 1; // going forward a node
      path.push_back(c);

      for (auto word : tree->find_anagrams(chars, path, root, MIN_WORD_LENGTH, MIN_SENTENCE_LENGTH)){
         this->sentences.push_back(word); // yield word
      }

      tree->sentences.clear(); // clear generator
      path.pop_back();  // going back a node ...
      chars.find(c)->second = count;
   }
   return this->sentences;
}
