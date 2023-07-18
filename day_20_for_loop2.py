startingNumeber = int(input("Insert starting number: "))
endingNumber = int(input("Insert ending number: "))
incrementValue = int(input("Please specify incrementation: "))

print(f'Start at: {startingNumeber}')
print(f'End before: {endingNumber}')
print(f'Increment between values: {incrementValue}')

for i in range(startingNumeber, endingNumber, incrementValue):
	print(i)
