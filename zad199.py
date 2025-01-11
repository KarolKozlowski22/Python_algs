# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca wskaźnik do
# ostatniego elementu przed cyklem

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

def create_list_with_cycle(numbers, idx=-1):
    if numbers is None:
        return None
    head=Node(numbers[0])
    current=head
    cycle=None

    for i, number in enumerate(numbers[1:], 2):
        current.next=Node(number)
        current=current.next
        if i==idx:
            cycle=current
    if idx!=-1:
        current.next=cycle
    return head

def print_linked_list(head, limit=10):
    current=head
    count=0
    while current:
        print(current.value, end="->")
        current=current.next
        count+=1
        if count >=limit:
            break
    print("None")

def find_last_node(head):
    if head is None or head.next is None:
        return -1
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    else:
        return None
    slow=head
    while slow.next!=fast.next:
        slow=slow.next
        fast=fast.next
    slow=slow.next

    while fast.next!=slow:
        fast=fast.next
    return fast.value
    

numbers=[1,2,3,4,5,6]
head=create_list_with_cycle(numbers,3)
print_linked_list(head)
result=find_last_node(head)
print(result)


        


