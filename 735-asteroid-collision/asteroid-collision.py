class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        for i in asteroids:
            if i>0:
                stack.append(i)
            
            else:
                while stack and stack[-1]>0:
                    if stack[-1]<-i:
                        stack.pop()
                    elif stack[-1]==-i:
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(i)
        return stack


        