class Solution(object):
    def finalValueAfterOperations(self, operations):
        X=0
        sum =0
        for i in operations:
            if i=="X++" or  i=="++X":
                sum+=1
            else:
                sum-=1
        return sum
