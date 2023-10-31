currentPrice = float(input('Current product price:'))
previousPrice = float(input('Previous product price:'))
if previousPrice - currentPrice >= 0.1*previousPrice:
    priceReduction = 1-currentPrice/previousPrice
    print(f'Buy the product!!\nProduct price reduced by {round(100*priceReduction)}%')