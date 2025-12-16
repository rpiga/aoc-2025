"""
Sample:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Note: Adjacent = surrounding
1 2 3
4 @ 5
6 7 8
"""

def main():
    print("Hello, day 4.")
    f = open('test.txt', 'rt')
    total = 0
    
    rolls = f.read().splitlines()
    LENGTH = len(rolls[0])
    check_matrix=[[-LENGTH-1, -LENGTH, -LENGTH+1],[-1,0,1],[LENGTH-1,LENGTH,LENGTH+1]]

    for line in range(len(rolls)):
        line_bool = list( map(lambda x: True if x=='@' else False , rolls[line]) )
        print(f'> {line} {line_bool}')
        
        for roll in range(len(line_bool)):
            if line_bool[roll]:
                a,b = [ (i, v+roll)  for i,v in enumerate(check_matrix) ]
                print(f'>> {roll} {a}{b}')


    print(f'Total: {total}')
    f.close()


def main_old():
    print("Hello, day 4.")
    
    f = open('test.txt', 'rt')
    
    rolls = f.read().splitlines()
    LENGTH = len(rolls[0])
    check_matrix=[-LENGTH-1, -LENGTH, -LENGTH+1,-1,1,LENGTH-1,LENGTH,LENGTH+1]

    rolls_line = ''.join(rolls)
    rolls_bool = list( map(lambda x: True if x=='@' else False , rolls_line) )

    total = 0

    for i in range(len(rolls_bool[:30])):
        print(i, rolls_bool[i])
        if rolls_bool[i]:
            c = 0
            for j in check_matrix:
                print(f'> {i}, {j} {i+j}:{rolls_bool[i+j]}')
                if i+j >= 0 and i+j < len(rolls_line)-LENGTH:
                    c += 1 if rolls_bool[i+j] else 0
            if c < 4:
                total += 1 
                print(f'{i}: {total}')

    print(rolls_line)
    print(rolls_bool)
    
    print(f'Total: {total}')
    f.close()
    
if __name__ == "__main__":
    """
    https://adventofcode.com/2025/day/4
    Author: https://github.com/rpiga
    """
    main()