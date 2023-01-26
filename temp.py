# temp file for preston's question:

go_again = 'Y'
while go_again == 'Y':
    current_square = 0
    total = 0
    length = int(input("Input a integer number: ")) + 1
    for counter in range(length):
        current_square = counter ** 2
        total = total + current_square
        # print(f'{counter}^2 = {current_square}')
    print(f'Total = {total}')
    go_again = input('Again, Y or N?').upper()

