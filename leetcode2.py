'''
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val     # int类型
        self.next = next   # ListNode类型

class Solution:
    def addTwoNumbers(self, l1, l2) :
        l3 = ListNode(0, ListNode())  # 定义一个头节点方便操作
        p_1 = l1
        p_2 = l2
        p = l3
        while p_1 is not None or p_2 is not None:
            if p_1 is not None and p_2 is not None:
                if p_1.val + p_2.val + p.val < 10:
                    p.next.val = p_1.val + p_2.val + p.val
                    p.next.next = ListNode()
                else:
                    p.next.val = (p_1.val + p_2.val + p.val) % 10
                    p.next.next = ListNode(1)
            p_1 = p_1.next
            p_2 = p_2.next
            '''else:
                 p_1 = ListNode()
            if p_2.next is not None:
                p_2 = p_2.next
            else:
                p_2 = ListNode()
            p = p.next
            if p_1 is None and p_2 is None:
                break'''

        return l3.next
    pass


'''单链表由嵌套定义实现'''
l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))
l =[]
result = Solution()
p = result.addTwoNumbers(l1, l2)
while p is not None:
    print(p.val)
    p = p.next
# print(l)
