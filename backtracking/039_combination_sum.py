class Solution(object):
    def combinationSum(self, candidates, target):

        result = []   # 최종 정답 조합들을 저장

        def backtrack(start, path, total):

            # 현재 합이 target과 같으면 정답
            if total == target:
                result.append(path[:])   # 현재 path를 복사해서 저장
                return

            # 현재 합이 target보다 크면 더 볼 필요 없음
            if total > target:
                return

            # start부터 끝까지 후보 확인
            for i in range(start, len(candidates)):

                # 1. 현재 숫자 선택
                path.append(candidates[i])

                # 2. 선택한 상태로 더 깊게 탐색
                # i를 그대로 넘기는 이유:
                # 같은 숫자를 다시 사용할 수 있기 때문
                backtrack(
                    i,
                    path,
                    total + candidates[i]
                )

                # 3. 방금 선택한 숫자 취소
                # 다른 경우를 보기 위해 원래 상태로 복구
                path.pop()

        # 처음에는
        # start = 0
        # path = []
        # total = 0
        backtrack(0, [], 0)

        return result