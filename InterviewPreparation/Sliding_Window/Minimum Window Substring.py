'''Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 '''

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Count the frequency of each character in t
        t_count = Counter(t)
        required = len(t_count)  # Number of unique characters in t needed

        # Left and right pointers
        l, r = 0, 0

        # Variables to track the current window
        formed = 0
        window_counts = {}

        # (window length, left pointer, right pointer)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the frequency of the current character matches the desired count in t
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            # Try and contract the window until it ceases to be 'desirable'
            while l <= r and formed == required:
                char = s[l]

                # Save the smallest window until now
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the left pointer is no longer in the window
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1

                # Move the left pointer ahead
                l += 1

            # Keep expanding the window by moving the right pointer
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
