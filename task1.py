def solution(head):
    t = head
    while t.next_item is not None:
        print(t.value)
        t = t.next_item
    print(t.value)