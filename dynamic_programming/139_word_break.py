class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 빠른 검색을 위해 set으로 변환
        word_set = set(wordDict)
        
        # dp[i] : s[:i] 가 wordDict 단어로 완성 가능한지 여부
        dp = [False] * (len(s) + 1)
        dp[0] = True  # 빈 문자열은 항상 가능하다고 시작
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # s[:j]가 이미 만들어질 수 있고, 나머지 부분(s[j:i])이 word_set에 있다면
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # i번째 위치가 완성 가능함을 확인했으므로 다음 i로 넘어가도 됨
                    
        return dp[len(s)]