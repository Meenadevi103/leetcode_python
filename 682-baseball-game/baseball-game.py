class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i=="D":
                d=stack[-1]*2
                stack.append(d)
            elif i=="C":
                stack.pop()
            elif i=="+":
                a=stack[-1]
                b=stack[-2]
                stack.append(a+b)
            else:
                stack.append(int(i))
        return sum(stack)
