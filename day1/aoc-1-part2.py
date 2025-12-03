
def main():
    dial=50
    password=0

    print('Hello.')
    input_file = open('input.txt', 'r')

    for line in input_file:
        item = line.rstrip()
        turn = 1 if item[0] == 'R' else -1
        value = turn * int(item[1:])
        # print(f'>>> {dial+value}')

        temp=0
        if abs(value) > 99:
            temp = abs(value)//100
            remainder=0+(abs(value)-(temp*100))
            value=turn*remainder
            # print(f'>>>>> {value}\t{temp}\t{remainder}')

        if (dial == 0):
            dial = (dial + value)%100
            password+=temp
        else:
            dial = (dial + value)
            if dial%100==0 or dial< 0 or dial > 99:
                password+=1
            password+=temp
            dial%=100
        # print(f'>> {item}\t\t{value}\t{dial}\t{password}')
    print(f'Result: {password}')

if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/1
    """
    main()

