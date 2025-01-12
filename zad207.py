# Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza” od pierwszej litery s2.
# Według tej zasady rozmieszczono napisy w liście cyklicznej, na przykład:
# ??bartek??leszek??marek??ola??zosia?? ????????????????????????????????????? Proszę napisać stosowne
# definicje typów oraz funkcję wstawiającą do listy napis z zachowaniem zasady poprzedzania. Do funkcji należy
# przekazać wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą, czy
# udało się wstawić napis do listy. Po wstawieniu elementu wskaźnik do listy powinien wskazywać na nowo
# wstawiony element.


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    if values is None:
        return None
    head=Node(values[0])
    current=head
    for value in values[1:]:
        current.next=Node(value)
        current=current.next
    current.next=head
    return head

def print_linked_list(head, limit=20):
    current = head
    it=0
    while current:
        if it==limit:
            break
        print(current.val, end = " -> ")
        current = current.next
        it+=1
    print("None")

def my_insert(head, new_str):
    if head is None:
        head=Node(new_str)
        head.next=head
        return True, head
    current=head
    while current:
        if current.val[-1] < new_str[0] and current.next.val[0] > new_str[-1]:
            new_node=Node(new_str)
            new_node.next=current.next
            current.next=new_node
            return True, new_node
        else:
            current=current.next
        if current==head:
            return False, None
    

if __name__ == "__main__":
    values=["bartek", "leszek", "marek", "ola", "zosia"]
    my_list=create_linked_list(values)
    new_str="lalka"
    print_linked_list(my_list)
    is_inserted, current_node=my_insert(my_list, new_str)
    print(is_inserted, current_node.next.val)
    print_linked_list(my_list)

    