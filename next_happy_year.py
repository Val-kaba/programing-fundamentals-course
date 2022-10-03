year = int(input())
is_happy_year = False

while not is_happy_year:
    year += 1
    set_digits = set()
    for i in range(len(str(year))):
        set_digits.add(str(year)[i])
        if len(str(year)) == len(set_digits):
            is_happy_year = True
            break

print(year)
