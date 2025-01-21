'''You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 '''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])  # Length of each word in the array
        num_words = len(words)  # Number of words in the array
        concat_len = word_len * num_words  # Total length of the concatenated string
        word_count = {}  # Dictionary to count occurrences of each word in `words`

        # Initialize the word count dictionary
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        result = []

        # Loop over each possible starting point within the word length
        for i in range(word_len):
            left = i
            right = i
            current_count = {}  # Dictionary to count occurrences of words in the current window
            while right + word_len <= len(s):
                word = s[right:right + word_len]  # Extract a word of length `word_len`
                right += word_len
                if word in word_count:
                    current_count[word] = current_count.get(word, 0) + 1
                    # If a word is over-represented, slide the window
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                    # If the window matches the concatenated length, add the starting index
                    if right - left == concat_len:
                        result.append(left)
                else:
                    # Reset the window if the word is not in `words`
                    current_count.clear()
                    left = right

        return result