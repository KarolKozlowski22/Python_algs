# Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę. Do
# funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wskazanie do
# scalonej listy. - funkcja iteracyjna, - funkcja rekurencyjna.

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

def create_linked_list(values):
    if values is None:
        return None
    head=Node(values[0])
    current=head
    for value in values[1:]:
        current.next=Node(value)
        current=current.next
    return head

values_1=[1,2,3,4,5,6]
values_2=[4,5,6,7,9]
list_1=create_linked_list(values_1)
list_2=create_linked_list(values_2)
print_linked_list(list_1)
print_linked_list(list_2)
