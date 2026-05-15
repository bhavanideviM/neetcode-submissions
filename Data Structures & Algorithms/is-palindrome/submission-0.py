class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for i in s:
            if i.isalnum():
                newstr+=i.lower()
        print(newstr[::-1])
        return newstr == newstr[::-1]
        