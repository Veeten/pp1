pin = 3792
tries = 0
while True:
    user_pin = int(input('Enter the PIN code: '))
    if user_pin == pin:
        print('Correct')
        break
    else:
        print('Incorrect...')
    tries += 1
    if tries >= 3:
        print('Sorry, your payment card has been blocked')
        break