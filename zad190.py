# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy
# jednokierunkowej, przenosi na początek listy te z nich, które mają parzystą ilość piątek w zapisie ósemkowym.


def count_fives(n):
    octal_n=oct(n)
    return octal_n.count('5')

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


def solve(head):

    if head is None:
        return None

    even_head=None
    even_current=None
    odd_head=None
    odd_current=None
    current=head

    while current:
        fives=count_fives(current.value)
        new_node=current.next
        current.next=None
        if fives % 2 == 0:
            if even_head is None:
                even_head=even_current=current
            else:
                even_current.next=current
                even_current=current
        else:
            if odd_head is None:
                odd_head=odd_current=current
            else:
                odd_current.next=current
                odd_current=current
        current=new_node

    if even_current:
        even_current.next=odd_head
    return even_head if even_head else odd_head

def print_linked_list(head, octal=False):
    current = head
    while current:
        value = oct(current.value)[2:] if octal else current.value
        print(value, end=" -> ")
        current = current.next
    print("None")

head = Node(65)  
head.next = Node(125) 
head.next.next = Node(80) 
head.next.next.next = Node(45)  
head.next.next.next.next = Node(200)  

print("Oryginalna lista w systemie dziesiętnym:")
print_linked_list(head)

print("Oryginalna lista w systemie ósemkowym:")
print_linked_list(head, octal=True)

processed_head = solve(head)

print("Przetworzona lista w systemie dziesiętnym:")
print_linked_list(processed_head)

print("Przetworzona lista w systemie ósemkowym:")
print_linked_list(processed_head, octal=True)
                





