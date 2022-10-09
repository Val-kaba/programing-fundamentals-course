steps_counter = int(input())

positive_list = []
negative_list = []
blank_list = []
is_positive = False

for _ in range(steps_counter):
    current_numbers = int(input())
    blank_list.append(current_numbers)

for num in blank_list:

    if num < 0:
        is_positive = False
        negative_list.append(num)
    else:
        is_positive = True
        positive_list.append(num)




print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")





