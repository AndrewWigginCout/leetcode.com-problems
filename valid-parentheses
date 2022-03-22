'''
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        for e in s:
            if e in ['(','{','[']:
                st.append(e)
            elif e == ')' and st!=[] and st[-1]=='(':
                st.pop()
            elif e == '}' and st!=[] and st[-1]=='{':
                st.pop()
            elif e == ']' and st!=[] and st[-1]=='[':
                st.pop()
            else:
                return False
        return st==[]
                
