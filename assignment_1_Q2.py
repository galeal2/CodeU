class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item
    def __len__(self):
        if self.is_empty():
          return 0
        ptr = self.head	
        length = 0
        while ptr != None:
            length += 1
            ptr = ptr.next
        return length    

            
    def is_empty(self):
        return self.head == None
        
    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += " " + str(ptr.item)
            ptr = ptr.next
            
        return tmp_str
        
    def rotate(self):
        ptr_c = self.head
        self.head = self.head.next
        ptr = self.head
        while ptr != None and ptr.next != None:
           ptr = ptr.next
        ptr.next = Node(ptr_c.item, None)

# find kth to last element in a linkedlist        
def find_kth_to_last(ll, k):
    if ll.is_empty():
        return 'LinkedList empty'
    length = len(ll)

    # check k to be in range len(ll)
    if k >= length:
        k = k % length
    ptr = ll.head

    # move pointer to position k
    while k:
        ptr = ptr.next
        k -= 1

    # create a pointer that starts at the head of ll
    # and move kth_to_last along with ptr
    # when ptr reaches the end kth_to_last will be the kth to last element
        
    kth_to_last = ll.head
    while ptr and ptr.next:
        ptr = ptr.next
        kth_to_last = kth_to_last.next
  
    return kth_to_last.item    



def main():
    
    # Create the linked list
    ll = LinkedList()
    ll2 = LinkedList()
    ll.add(12)
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(0)
    ll.add(5)
    print(ll)
    assert find_kth_to_last(ll, 100) == 0, "Incorrect"
    assert find_kth_to_last(ll2, 2) == 'LinkedList empty', "Incorrect"
    assert find_kth_to_last(ll, 3) == 3, "Incorrect"

if __name__ == "__main__":
    main()



