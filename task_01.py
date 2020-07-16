from collections import Counter

n = 4#int(input())
list_a = [1,1,1,2,2]#list(input().split())
votes = Counter(list_a)
dict_a = {}
for value in votes.values():
    dict_a[value] = []
for (key, value) in votes.items():
    dict_a[value].append(key)

print(dict_a[3])