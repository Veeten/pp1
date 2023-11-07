dec_number = int(input('Enter decimal number: '))
dec_number_original = dec_number
bin_number = ''
while True:
    x = int(dec_number % 2)
    print(x)
    bin_number = str(x) + bin_number
    if x == 1:
        dec_number = (dec_number - 1) / 2
    else:
        dec_number = dec_number / 2
    if dec_number == 0: break
print(f"{dec_number_original}(10) = {bin_number}(2)")
