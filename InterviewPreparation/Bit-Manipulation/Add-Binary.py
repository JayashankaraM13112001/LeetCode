'''Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.'''

def addBinary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1  # Pointers to the end of both strings
    carry = 0
    result = []
    
    while i >= 0 or j >= 0 or carry:
        sum_val = carry
        
        if i >= 0:
            sum_val += int(a[i])
            i -= 1
        if j >= 0:
            sum_val += int(b[j])
            j -= 1
        
        result.append(str(sum_val % 2))  # Compute the current binary digit
        carry = sum_val // 2  # Compute carry for the next iteration
    
    return ''.join(result[::-1])  # Reverse the result and return
