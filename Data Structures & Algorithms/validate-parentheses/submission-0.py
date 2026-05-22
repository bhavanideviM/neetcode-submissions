class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        dic = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in dic:
                if a and a[-1] == dic[i]:
                    a.pop()
                else:
                    return False
            else:
                a.append(i)
        return True if not a else False
            
        