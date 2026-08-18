class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stack=[]
        for i in sandwiches:
            stack.append(i)
    
        count=0
        while(len(students)>0 and count<len(students)):
            if students[0]==stack[0]:
                stack.pop(0)
                students.pop(0)
                count=0
            else:
                students.append(students.pop(0))
                count+=1
                
        if not stack:
            return 0
        else:
            return len(students)




