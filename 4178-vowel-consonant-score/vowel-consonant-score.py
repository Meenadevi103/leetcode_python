class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v={'a','e','o','i','u'}
        vowel=0
        con=0
        for i in s:
            if i.isalpha():
                if i in v:
                    vowel+=1
                else:
                    con+=1
        if con>0:
            r=vowel//con
            return r
        else:
            return 0
