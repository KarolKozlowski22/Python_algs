# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
# ..def init(self,val,next=None):
# 18
# ....self.val = val
# ....self.next = next
# Lista zawierała wartości stanowiące kolejne wyrazy ciągu arytmetycznego. Z wnętrza listy usunięto pewną
# liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy) która uzupełnia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu arytmetycznego. Funkcja powinna
# zwrócić liczbę wstawionych elementów. Można założyć, że lista wejściowa liczy więcej niż 2 elementy.



class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end = " -> ")
        current = current.next
    print("None")

def repair(p):
    if p is None or p.next is None:
        return 0

    r = p.next.val - p.val

    current = p
    count_el = 0
    while current and current.next:
        # while current.next.value != current.value + r:
        #   new_node = Node(current.value + r)
        #   new_node.next = current.next
        #   current.next = new_node
        #   current = new_node
        #   count_el += 1
        # current = current.next
        expected_val=current.val+r
        if current.next.val!=expected_val and (current.next.val-current.val)%r==0:
            new_node=Node(current.val+r, current.next)
            current.next=new_node
            count_el+=1
        else:
            current=current.next
    if count_el==0:
        current=p
        while current and current.next:
            if current.next.val-current.val!=r:
                print("Nie da sie z tej listy utworzyć ciągu arytmetycznego")
                break
            current=current.next
    return count_el
    
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(4)
    head.next.next = Node(14)
    print_linked_list(head)

    print(repair(head))
    print_linked_list(head)