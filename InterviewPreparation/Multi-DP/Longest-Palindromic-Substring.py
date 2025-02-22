'''Given a string s, return the longest 
palindromic
 
substring
 in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.'''

def longestPalindrome(s):
    if len(s) <= 1:
        return s

    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Extract the valid palindrome

    longest = ""
    for i in range(len(s)):
        # Check odd-length palindrome
        odd_palindrome = expandAroundCenter(i, i)
        # Check even-length palindrome
        even_palindrome = expandAroundCenter(i, i + 1)

        # Update longest palindrome found
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest
