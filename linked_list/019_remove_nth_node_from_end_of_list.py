# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # 1. dummy 노드 생성 후 head 연결
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # 2. fast를 (n + 1)번 먼저 보냄
        for _ in range(n + 1):
            fast = fast.next

        # 3. fast가 None이 될 때까지 둘 다 이동! (while fast.next -> while fast)
        while fast:
            fast = fast.next
            slow = slow.next

        # 4. slow 다음 노드(삭제 대상)를 건너뛰어 연결 끊기
        slow.next = slow.next.next

        # 5. 변경된 리스트의 진짜 head 반환
        return dummy.next