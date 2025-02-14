'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''

def merge(nums1,m,nums2,n):
    for i in range(n):
        inserted=False
        
        for j in range(m+i):
            if nums2[i]<nums1[j]:
                nums1.insert(j,nums2[i])
                nums1.pop()
                inserted=True
                break
            if not inserted:
                nums1[m+i]=nums2[i]

nums1=[1,3,5,0,0,0]
nums2=[2,3,4]
m,n=len(nums1)-len(nums2),len(nums2)
merge(nums1,m,nums2,n)
print(nums1)