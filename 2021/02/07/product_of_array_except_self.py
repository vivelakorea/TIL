
"""
    https://leetcode.com/problems/best
    반복문 시작할때 어떤 값을 계산 후 넣기 vs 반복문 끝에 다음에 넣을 값을 계산
"""


def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = []
    p = 1
    for i in range(len(nums)):
        res.append(p)
        p *= nums[i]
    p = 1
    for i in range(len(nums)):
        res[len(nums) - i - 1] *= p
        p *= nums[len(nums) - i - 1]

    return res

# 반복문 시작할때 어떤 값을 계산 후 넣기 vs 반복문 끝에 다음에 넣을 값을 계산
