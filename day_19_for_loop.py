#Loan Calculator

#got $1'000 at 5% APR (0.05) for 10 years

loan = 1000

annualPercentageRate = 0.05

interest = 0

for i in range(10):
    result = loan * annualPercentageRate
    loan = round(loan + result, 2)
    interest = round(loan - 1000, 2)
    print(f"Year {i+1} is ${loan}")

print(f'You paid ${interest} in interest!')
