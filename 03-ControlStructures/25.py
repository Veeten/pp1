number = int(input('Enter the number of products purchased'))
price = float(input('Enter product price'))
if number > 2:
    to_pay = 2 * price + (number - 2) * price * 0.75
else:
    to_pay = number * price
print(f'Ammount to pay: {to_pay}')