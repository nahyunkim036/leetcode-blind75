class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # 너비 = 오른쪽 인덱스 - 왼쪽 인덱스
            width = right - left
            
            # 높이는 둘 중 더 낮은 벽의 높이
            current_height = min(height[left], height[right])
            
            # 넓이 계산 및 최댓값 갱신
            current_area = width * current_height
            max_area = max(max_area, current_area)
            
            # 더 낮은 쪽의 포인터를 안쪽으로 이동시킵니다.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area