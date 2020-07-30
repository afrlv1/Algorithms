# H. Все наоборот
def swap(node):
    prev = node.prev
    node.prev = node.next
    node.next = prev

def print_linked_list(head):
    t = head
    while t.next_item is not None:
        print(t.value)
        t = t.next_item
    print(t.value)

def solution(node):
    head = node

    while head is not None:
        swap(head)
        prev = head
        head = head.prev

    if prev:
        node = prev

    return node

