class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = temp = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next=list2
                list2 = list2.next
            temp = temp.next
        temp.next = list1 or list2
        return dummy.next
#Disclaimer: This solution is based on tutorials, which introduced me to the concept of a dummy variable and using the function Listnode
# A very useful youtube video explaining dummy variable https://www.youtube.com/watch?v=GfRQvf7MB3k
