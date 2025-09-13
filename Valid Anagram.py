"""Q) 
Valid Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
"""


"""1st approach:
Brute Force method
Time Complexity = O(n log n)
Space Complexity = O(n)"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)

        if slen == tlen:
            sorted_schar = sorted(s)
            sorted_tchar = sorted(t)

            for i in range(slen):
                if sorted_schar[i] != sorted_tchar[i]:
                    return False
            return True
        else:
            return False

"""2nd approach:
Hashmap method
Time Complexity = O(n)
Space Complexity = O(K) ~ O(1)"""



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)
        dicts = {}
        dictt = {}
        if(slen == tlen):
            for ch in s:
                if ch in dicts:
                    dicts[ch]+=1
                else:
                    dicts[ch] = 1
            for ch in t:
                if ch in dictt:
                    dictt[ch]+=1
                else:
                    dictt[ch] = 1

            for ch in s:
                if(dicts.get(ch,0)!=dictt.get(ch,0)):
                    return False
            return True
        
                
        else:
            return False
