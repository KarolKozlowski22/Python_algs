# Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów. Krańce przedziałów
# określa uporządkowana para liczb całkowitych. Proszę napisać stosowne deklaracje oraz funkcję redukującą
# liczbę elementów listy. Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien zostać zredukowany
# do listy: [13,19] [2,6] [7,12]


# def reduce_intervals(intervals):
#     intervals.sort(key=lambda x: (x[0], x[1]))
#     result=[]
#     result.append(intervals[0])
#     for current_interval in intervals:
#         if result[-1][1]<current_interval[0]:
#             result.append(current_interval)
#         else:
#             result[-1]=(result[-1][0], max(result[-1][1],current_interval[1]))
#     return result

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

def create_linked_list(values):
    if values is None:
        return None
    head=Node((values[0][0], values[0][1]))
    current=head
    for value in values[1:]:
        current.next=Node((value[0], value[1]))
        current=current.next
    return head

def print_linked_list(head):
    current=head
    while current:
        print(f"({current.value[0]}, {current.value[1]})", end="->")
        current=current.next
    print("None")

def reduce_intervals(head):
    current=head
    while current and current.next and current.next.next:
        if current.value[1]>=current.next.value[0]:
            current=Node((current.value[0], max(current.value[1], current.next.value[1])))
            current=current.next.next
            current.next=None
        current=current.next
    return head


intervals=[(15,19), (2,5), (7,11), (8,12), (5,6), (13,17)]
intervals.sort()
linked_list=create_linked_list(intervals)
print_linked_list(linked_list)
reduced_linked_list=reduce_intervals(linked_list)
print_linked_list(reduced_linked_list)




