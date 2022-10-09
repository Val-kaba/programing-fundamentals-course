steps = int(input())

POSITIVE = "positive"
NEGATIVE = "negative"
ODD = "odd"
EVEN = "even"

blank_list = []
even_list = []
odd_list = []
positive_list = []
negative_list = []
filters = []


for _ in range(steps):
    current_numbers = int(input())
    blank_list.append(current_numbers)


command = input()

for every_number in blank_list:
    filtering = (

        (command == POSITIVE and every_number >= 0)or
        (command == NEGATIVE and every_number < 0)or
        (command == EVEN and every_number % 2 == 0)or
        (command == ODD and every_number % 2 == 1)


    )
    if filtering:
        filters.append(every_number)

print(filters)
