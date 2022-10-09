number_of_steps = int(input())
element = input()

empty_list = []


for times in range(number_of_steps):
    prompt = input()
    empty_list.append(prompt)

print(empty_list)

for i in range(len(empty_list), -1):
    word = empty_list[i]

    if element not in word:
        empty_list.remove(word)

print(empty_list)




