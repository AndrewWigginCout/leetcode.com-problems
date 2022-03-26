#https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def append(x,val):
    x.next=ListNode(val)
    return x.next
def convert(n):
    h=ListNode(n[0])
    rv=h
    n=n[1:]
    for e in n:
        append(h,e)
        h=h.next
    return rv
def printll(n):
    h=n
    #print(h.val,end=',')
    while h:
        print(h.val,end=',')
        h=h.next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if list1==None and list2==None: return None
        h,g=list1,list2
        rv2=[]
       
        while h and g:#maybe check for None
            if h.val<g.val:
                #tail=append(tail,ListNode(h.val))
                rv2.append(h.val)
                h=h.next
            else:
                #tail=append(tail,ListNode(g.val))
                rv2.append(g.val)
                g=g.next
        while h:
            #tail=append(tail,ListNode(h.val))
            rv2.append(h.val)
            h=h.next
        while g:
            #tail=append(tail,ListNode(g.val))
            rv2.append(g.val)
            g=g.next

        #print('rv2=',rv2)
        #print('rv=')
        #printll(rv)
        return convert(rv2)
