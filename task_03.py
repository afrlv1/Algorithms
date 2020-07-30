class StackMax:
    items = []
    maxim = []
    def isEmpty(self):
        return self.items == []
    def get_max(self):
        if self.isEmpty():
            print('None')
            return
        print (self.maxim[-1])
        return
    def push(self, item):
        if self.items:
            last_known_max = self.maxim[-1]
            if item > last_known_max:
                last_known_max = item
            self.items.append(item)
            self.maxim.append(last_known_max)

        else:
            self.items.append(item)
            self.maxim.append(item)
    def pop(self):
        if self.isEmpty():
            print('error')
            return
        result = self.items[-1]
        del self.items[-1]
        del self.maxim[-1]
        return result

t = int(input())
stack = StackMax()
while t:
    l = input().split()
    if l[0] == 'push':
        stack.push(int(l[1]))
    if l[0] == 'pop':
        stack.pop()
    if l[0] == 'get_max':
        stack.get_max()
    t -= 1