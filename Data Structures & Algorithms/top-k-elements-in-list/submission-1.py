class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic ={}

        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        m =[]
        sort_itms = sorted(dic.items(), key = lambda x: x[1], reverse = True)
        print(sort_itms)
        for num, count in sort_itms[:k]:
            
            m.append(num)
        return m
        