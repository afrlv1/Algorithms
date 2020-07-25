def solution(head, index):
    if index == 0:
        return
    while index-1:
        head = head.next_item
        index -= 1


    tmp = head.next_item
    head.next_item = new_node
    new_node.next_item = tmp
    return head



    old = curr = self.first
    count = 0
        if count == i:
          if curr.next == self.last:
            self.last = curr
            break
          else:
            old.next = curr.next
          break
        old = curr
        curr = curr.next
        count += 1