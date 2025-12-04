
def main():
    dial=50
    password=0

    print('Hello.')
    input_file = open('input.txt', 'r')

    for line in input_file:
        item = line.rstrip()
        turn = 1 if item[0] == 'R' else -1
        value = turn * int(item[1:])

        dial = (dial + value) % 100
        if dial==0:
            password+=1
            print(f'>> {item}/ {turn}/ {value}/ {dial}/ {password}')

if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/1
    Author: https://github.com/rpiga
    """
    main()

