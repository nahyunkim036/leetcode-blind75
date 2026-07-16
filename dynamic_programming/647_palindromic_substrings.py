class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        finalArray = []
        
        # 1. 모든 부분 문자열(Substring) 추출하기
        # i는 시작 지점, j는 끝 지점
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                # s[i:j]로 문자열을 직접 잘라서 리스트에 추가 (주소 참조 문제 없음!)
                finalArray.append(s[i:j])
        
        result = []
        
        # 2. 앞뒤가 똑같은 회문(Palindrome)인지 검사하기
        for ary in finalArray:
            if ary == ary[::-1]:
                result.append(ary)
                
        return len(result)