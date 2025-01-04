# Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy unikalne. Do funkcji
# należy przekazać wskazanie na pierwszy element listy

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

def print_linked_list(head):
    current=head
    while current:
        print(current.value, end="->")
        current=current.next
    print("None")

def remove_duplicates(head):
    
    if head is None or head.next is None:
        return head
    
    count={}
    current=head

    while current:
        if current.value not in count:
            count[current.value] = 0
        count[current.value]+=1
        current=current.next
    
    head_2=Node(0)
    current=head_2

    while head:
        if count[head.value]==1:
            current.next=Node(head.value)
            current=current.next
        head=head.next

    return head_2.next

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(3)
head.next.next.next.next=Node(6)
head.next.next.next.next.next=Node(4)

print_linked_list(head)
unique=remove_duplicates(head)
print_linked_list(unique)

    

