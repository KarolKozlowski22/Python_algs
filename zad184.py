# Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą
# dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.

# import random

# def add_two_lists(list_1, list_2):
#     n=len(list_1)
#     m=len(list_2)
#     if n>m:
#         list_2=(n-m)*[0]+list_2
#     else:
#         list_1=(m-n)*[0]+list_1
#     result=[]
#     rest=0
#     for i in range(n-1,-1,-1):
#         current_sum=list_1[i]+list_2[i]+rest
#         result.append(current_sum%10)
#         rest=current_sum//10
#     return result[::-1]

# list_1=[random.randint(0,9) for _ in range(5)]
# list_2=[random.randint(0,9) for _ in range(5)]
# print(list_1)
# print(list_2)
# print(add_two_lists(list_1, list_2))

class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

def print_linked_list(head):
    current=head
    while current:
        print(current.value, end="->")
        current=current.next
    print("None")

def reverse_linked_list(head):
    prev=None
    current=head
    
    while current:
        new_node=current.next
        current.next=prev
        prev=current
        current=new_node
    return prev

def add_two_linked_lists(list_1, list_2):
    list_1=reverse_linked_list(list_1)
    list_2=reverse_linked_list(list_2)
    rest=0
    result=Node(0)
    current=result
    while list_1 or list_2 or rest:
        list_1_val=list_1.value if list_1 else 0
        list_2_val=list_2.value if list_2 else 0
        current_sum=list_1_val+list_2_val+rest
        rest=current_sum//10
        current.next=Node(current_sum%10)
        current=current.next
        if list_1:
            list_1=list_1.next
        if list_2:
            list_2=list_2.next
    result=reverse_linked_list(result.next)
    return result


        

list_1=Node(3)
list_1.next=Node(5)
list_1.next.next=Node(7)
list_1.next.next.next=Node(4)

list_2=Node(8)
list_2.next=Node(1)
list_2.next.next=Node(6)
list_1.next.next.next=Node(9)

print_linked_list(list_1)
print_linked_list(list_2)

result=add_two_linked_lists(list_1, list_2)
print_linked_list(result)




