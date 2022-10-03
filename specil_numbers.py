number_count = int(input())
for steps in range(1, number_count + 1):
    sum_digits = 0
    num = steps

    while num > 0:
        sum_digits += steps % 10
        num = int(num / 10)

        if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
            print(f"{steps} -> True")
        else:
            print(f"{steps} -> False")
