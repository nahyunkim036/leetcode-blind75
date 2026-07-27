class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        # 1. 가운데 노드 찾기
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 리스트 분리 후 뒤쪽 리스트 뒤집기
        curr = slow.next
        slow.next = None
        prev = None # prev는 뒤집힌 리스트의 초기 상태
         # 보통 prev는 현재 노드보다 하나 앞에 있는 (이미 처리한) 노드를 의미
        
        # 여기서 부터 리스트 뒤집기
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. 앞쪽과 뒤쪽 리스트를 번갈아 연결
        first = head
        second = prev

        while second:
            # first는 마지막에 노드가 하나 남을 수 있지만, 그 노드는 이미 올바른 마지막 위치에 있다.
            # second가 없어지는 순간 모든 끼워 넣기가 끝난다.
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2