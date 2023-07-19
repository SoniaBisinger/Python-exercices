print("Math Game!")

number = int(input("Name your multiples: "))

for i in range(10):
    result = (i+1) * number
    print(f'{i+1} * {number} =')
    answer = int(input())
    if result == answer:
        print("Great work!")
    else:
        print(f"Nope! 🙁 The answer was {result})")
