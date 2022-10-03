steps_in_loop = int(input())
first_letters = 0
second_letters = 0
combo = 0


for steps in range(steps_in_loop):
    text = input()
    if len(text) == 4:
        print(text[::-1])
    elif len(text) < 4:
        first_letters = text[:len(text)]
        second_letters = text[len(text)::-1]
        combo = first_letters + second_letters
        print(combo)
    else:
        first_letters = text[2:len(text)]
        second_letters = text[len(text)::-1]
        combo = first_letters + second_letters
        print(combo)








