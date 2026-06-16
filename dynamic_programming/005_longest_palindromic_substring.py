class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        array = []
        for i in range(len(s)):
            array.append(s[i])
            if array[0] != array[-1]:
                array.append(s[len(array)])
                if array[0] != array[-1]:
                   array.pop(0)
                   break
                break
            
        result = "".join(array)

        return result 
    
# Inital try => fail [passed few cases but couldn't cover every case]

class Solution(object):
    def longestPalindrome(self, s):
        result = ""

        for i in range(len(s)):
            # 홀수 길이 palindrome
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                current = s[left:right + 1]

                if len(current) > len(result):
                    result = current

                left -= 1
                right += 1

            # 짝수 길이 palindrome
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                current = s[left:right + 1]

                if len(current) > len(result):
                    result = current

                left -= 1
                right += 1

        return result
    
# 정석 풀이 

class Solution(object):
    def longestPalindrome(self, s):
        result = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                current = s[i:j + 1]

                if current == current[::-1]:
                    if len(current) > len(result):
                        result = current

        return result
    
# 풀어서 쓴 풀이? -> 완전탐색 이여서 시간복잡도 O(n^3)