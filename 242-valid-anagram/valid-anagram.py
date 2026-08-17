class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=sorted(s)
        # m=len(x)
        y=sorted(t)
        # n=len(y)
        if x==y:
            return True
        else:
            return False

                