//======================================================================
// Github: https://github.com/thjsimmons
//======================================================================

#include <iostream>
#include <stdio.h>

#include <vector>
#include <set>
#include <string>

#include <fstream>
#include <sstream>

#include <boost/algorithm/string.hpp>

#include "Tree.h"
#include "Timer.h"

using namespace std;

Tree load_dictionary(string path){ // load words from txt file into prefix tree object
   Tree tree = Tree();
   ifstream file(path);

   string line;

   while(file >> line) {
      boost::algorithm::to_lower(line);
      tree.add_word(line);
   }
   return tree;
}

void write_sentences(vector<string> sentences){ // write list of sentences/words to txt file
   ofstream newfile ("/home/hg/CLionProjects/wiw/cout.txt");

   for (string &s : sentences)
   {
      newfile << s << endl;
   };
}

set<string> split(string input){ // split sentence into set of words
   vector<string> v;
   boost::algorithm::split(v, input, boost::is_any_of(" "));
   set<string> st(v.begin(), v.end());
   return st;
}

bool sent_equiv(string s1, string s2){ // e.g. "big red truck" ~= "big truck red"
   set<string> a = split(s1);
   set<string> b = split(s2);

   return a == b;
}

vector<string> unique(vector<string> input){ // reduce sentence list to unique word combinations
   vector<string> output;

   for (auto input_sent: input) {
      if (output.empty()) {
         output.push_back(input_sent);

      }
      else {
         bool flag = false;
         for (auto output_sent: output) {
            if (sent_equiv(input_sent, output_sent)) {
               flag = true;
               break;
            }
         }
         if (!flag){
            output.push_back(input_sent);
         }
      }
   }
   return output;
}

int main() {

   cout << "Loading dictionary to tree ..." << endl;
   Tree dictionary = load_dictionary("/home/hg/CLionProjects/wiw/scrabble.txt"); // get words from text file

   string word;

   cout << "Enter a word: " << endl;
   cin >> word; // Get user's word
   word = nospaces(word);
   boost::algorithm::to_lower(word);

   Timer timer;
   timer.Start();

   vector<string> result = dictionary.get_anagrams(word); // Get anagram list

   vector<string> unique_result;
   unique_result = unique(result); // reduce to unique word combinations

   for (int i = 0; i < unique_result.size(); i++){
      string w = unique_result[i];
      cout << w << std::endl;
   }

   timer.Stop();
   cout << unique_result.size() << " results."  << endl;

   write_sentences(unique_result); cout <<""<<endl; // write to text file
   return 0;
}

