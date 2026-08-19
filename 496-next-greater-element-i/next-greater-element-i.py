class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ar=[]

        for i in nums1:
            for j in range(len(nums2)):

                if i==nums2[j]:

                    for k in range(j+1,len(nums2)):

                        if nums2[j]<nums2[k]:
                            ar.append(nums2[k])
                            break

                    else:
                        ar.append(-1)

        return ar