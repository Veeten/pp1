age = float(input("Enter the dog's age in human years:"))
if age <= 2:
    print(f"The dog's age in dog’s years is {age*10.5} years.")
else:
    dogAge = 2*10.5 + 4*(age-2)
    print(f"The dog's age in dog’s years is {dogAge} years.")