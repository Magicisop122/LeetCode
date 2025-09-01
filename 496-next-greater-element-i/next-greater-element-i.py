class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # solution 1

        # num1Index = {n : i for i, n in enumerate(nums1)}

        # res = [-1] * len(nums1)

        # for i in range(len(nums2)):
        #     if nums2[i] not in num1Index:
        #         continue
            
        #     for j in range(i + 1, len(nums2)):
        #         if nums2[j] > nums2[i]:
        #             idx = num1Index[nums2[i]]
        #             res[idx] = nums2[j]
        #             break

        # return res

        # solution 2

        stack = []
        nge = {}   

        for num in nums2:
            while stack and num > stack[-1]:
                nge[stack.pop()] = num
            stack.append(num)

       
            nge[num] = -1

        
        return [nge[num] for num in nums1]