class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_duplicates(self):
        current = self.head
        prev = None
        seen_data = set()
        while current:
            if current.data in seen_data:
                prev.next = current.next
            else:
                seen_data.add(current.data)
                prev = current
            current = current.next

def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print("Middle element:", ll.find_middle())  

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print("Has cycle:", ll.has_cycle())  

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
ll.remove_duplicates()
print("After removing duplicates:")
ll.display()  

ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

merged_ll = merge_sorted_lists(ll1.head, ll2.head)
print("Merged sorted lists:")
merged_ll.display()  
