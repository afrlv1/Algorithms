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