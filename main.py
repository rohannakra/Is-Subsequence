# https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1

def is_subsequence(s, t):
    if s == "": return True

    counter = 0
    for char in t:
        try:
            if char == s[counter]:
                counter += 1
        except IndexError:
            continue
    
    return True if counter == len(s) else False

print(is_subsequence('abc', 'ahbgdc'))
print(is_subsequence('axc', 'ahbgdc'))
print(is_subsequence("", 'abggdc'))
print(is_subsequence('b', 'abc'))

# ----------------------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True

        counter = 0
        for char in t:
            try:
                if char == s[counter]:
                    counter += 1
            except IndexError:
                continue
    
        return True if counter == len(s) else False

# Beats 93.74% of solutions in runtime, 72.11% of solutions in memory
