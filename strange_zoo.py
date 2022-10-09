tail = input()
body = input()
head = input()
lst = []
mix_variable = tail, body, head
for u in mix_variable:
    swap = u[0], u[2] = u[2], u[0]
    lst.append(swap)
print(lst)
