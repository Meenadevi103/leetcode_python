class Solution(object):
    def checkValidString(self, s):
        ostack=[]
        sstack=[]
        for i in range(len(s)):
            if s[i]=="(":
                ostack.append(i)
            elif s[i]=="*":
                sstack.append(i)
            
            else:
                if ostack:
                    ostack.pop()
                elif sstack:
                    sstack.pop()
                else:
                    return False
        while ostack and sstack:
            if ostack[-1]<sstack[-1]:
                ostack.pop()
                sstack.pop()
            else:
                return False
        return len(ostack)==0
                

        