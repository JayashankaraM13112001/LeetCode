'''A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.'''

from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)  # Convert wordList to a set for O(1) lookups
        if endWord not in wordSet:
            return 0  # If endWord is not in wordList, return 0
        
        queue = deque([(beginWord, 1)])  # (current word, transformation depth)
        alphabet = "abcdefghijklmnopqrstuvwxyz"  # All possible letters
        
        while queue:
            word, depth = queue.popleft()
            
            if word == endWord:
                return depth  # Found the shortest transformation path
            
            # Try changing each character in the word
            for i in range(len(word)):
                for char in alphabet:
                    if char != word[i]:  # Ensure only 1 character change
                        newWord = word[:i] + char + word[i+1:]
                        if newWord in wordSet:
                            queue.append((newWord, depth + 1))
                            wordSet.remove(newWord)  # Mark as visited
        
        return 0  # No path found
