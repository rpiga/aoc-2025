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
    f = open('input.txt', 'rt')
    total = 0
    
    rolls = f.read().splitlines()

    # Convert to boolean
    rolls_bool = []
    for i in range(len(rolls)):
        rolls_bool.append(list( map(lambda x: True if x=='@' else False , rolls[i]) ))

    # print(rolls)
    # print(rolls_bool)

    for i, v in enumerate(rolls_bool):
        # print(f'> {i} {v}')
        
        for j, w in enumerate(v):
            if w:
                if i == 0:
                    test = [
                    False, False, False,
                    rolls_bool[i][j-1] if j > 0 else False, False,  rolls_bool[i][j+1] if j < len(v)-1 else False,
                    rolls_bool[i+1][j-1] if j > 0 else False, rolls_bool[i+1][j],  rolls_bool[i+1][j+1] if j < len(v)-1 else False,
                    ]
                elif i > 0 and i < len(rolls_bool) - 1:
                    test = [
                    rolls_bool[i-1][j-1] if j > 0 else False, rolls_bool[i-1][j],  rolls_bool[i-1][j+1] if j < len(v)-1 else False,
                    rolls_bool[i][j-1] if j > 0 else False, False,  rolls_bool[i][j+1] if j < len(v)-1 else False,
                    rolls_bool[i+1][j-1] if j > 0 else False, rolls_bool[i+1][j],  rolls_bool[i+1][j+1] if j < len(v)-1 else False,
                    ]
                else:
                    test = [
                    rolls_bool[i-1][j-1] if j > 0 else False, rolls_bool[i-1][j],  rolls_bool[i-1][j+1] if j < len(v)-1 else False,
                    rolls_bool[i][j-1] if j > 0 else False, False,  rolls_bool[i][j+1] if j < len(v)-1 else False,
                    False, False, False,
                    ]
                total += 1 if sum(test) < 4 else 0

    print(f'Total: {total}')
    f.close()

if __name__ == "__main__":
    """
    https://adventofcode.com/2025/day/4
    Author: https://github.com/rpiga
    """
    main()