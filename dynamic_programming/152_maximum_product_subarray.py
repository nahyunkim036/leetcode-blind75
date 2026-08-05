class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 예외 처리: 배열에 원소가 1개뿐일 때 (예: [-2])
        if len(nums) == 1:
            return nums[0]

        array = []

        # 2. 첫 번째 포인터 i (시작 인덱스)
        for i in range(len(nums)):
            count = 1  # 구간이 시작될 때 곱을 1로 초기화
            
            # 3. 두 번째 포인터 j (끝 인덱스) -> i부터 시작해서 연속으로 곱함
            for j in range(i, len(nums)):
                count = count * nums[j]  # nums[j]로 '값'을 가져와 곱함
                array.append(count)      # 지금까지의 연속 곱 결과를 저장

        # 4. 구해진 모든 연속 곱 중 최댓값을 반환
        return max(array)
    
    ## ----여기까지가 내가 접근한 방식-----

    ## ----정석 정답----
    
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 전체 최대 곱을 저장할 변수 (첫 번째 원소로 초기화)
        result = nums[0]
        
        # 현재 위치까지의 최대/최소 곱
        curr_max = nums[0]
        curr_min = nums[0]
        
        # 두 번째 원소부터 순회
        for i in range(1, len(nums)):
            n = nums[i]
            
            # n이 음수이면 곱했을 때 최댓값과 최솟값이 서로 뒤바뀜!
            if n < 0:
                curr_max, curr_min = curr_min, curr_max
            
            # 1) 현재 숫자 자체 vs 2) 이전까지의 곱에 현재 숫자를 곱한 것 중 비교
            curr_max = max(n, curr_max * n)
            curr_min = min(n, curr_min * n)
            
            # 전체 최댓값 갱신
            result = max(result, curr_max)
            
        return result
