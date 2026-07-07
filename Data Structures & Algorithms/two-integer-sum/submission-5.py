class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        arr=[(num,i) for i, num in enumerate(nums)]

        arr.sort()

        left=0
        right=len(arr)-1

        while left<right:
            curr=arr[left][0]+arr[right][0]

            if curr==target:
                res = [arr[left][1],arr[right][1]]
                res.sort()
                return res
            elif curr < target:
                left+=1
            else:
                right-=1
