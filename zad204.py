# Dane są dwie niepuste listy, z których każda zawiera niepowtarzające się elementy. Elementy
# w pierwszej liście są uporządkowane rosnąco, w drugiej elementy występują w przypadkowej kolejności. Proszę
# napisać funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane elementy będą stanowić
# sumę mnogościową elementów z list wejściowych. Do funkcji należy przekazać wskazania na obie listy, funkcja
# powinna zwrócić wskazanie na listę wynikową. Na przykład dla list:
# 2 → 3 → 5 → 7 → 11
# 8 → 2 → 7 → 4
# powinna pozostać lista:
# 2 → 3 → 4 → 5 → 7 → 8 → 11

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

def solve(list_1, list_2):
    unique_values=set()
    current=list_1
    while current:
        unique_values.add(current.value)
        current=current.next
    current=list_2
    while current:
        unique_values.add(current.value)
        current=current.next
    result=Node(0)
    current=result
    for value in unique_values:
        current.next=Node(value)
        current=current.next
    return result.next

def create_linked_list(values):
    if values is None:
        return None
    head=Node(values[0])
    current=head
    for value in values[1:]:
        current.next=Node(value)
        current=current.next
    return head

values_1=[2,3,5,7,11]
values_2=[8,2,7,4]
list_1=create_linked_list(values_1)
list_2=create_linked_list(values_2)
result=solve(list_1, list_2)
print_linked_list(result)


