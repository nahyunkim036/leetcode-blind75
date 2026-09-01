class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            # 현재 탐색 범위의 가운데
            mid = (left + right) // 2

            # mid가 right보다 크면
            # 회전 지점(최소값)은 반드시 mid 오른쪽에 있음
            if nums[mid] > nums[right]:
                left = mid + 1

            # mid가 right보다 작으면
            # 최소값은 mid 또는 mid 왼쪽에 있음
            else:
                right = mid

        # left == right → 최소값 위치에서 만남
        return nums[left]