"""
Test values:
987654321111111
811111111111119
234234234234278
818181911112111
"""

def main():    
    print("Hello.")
    f=open('input.txt', 'rt')

    banks=f.read().splitlines()
    total = 0

    for line in banks:
        # print(line)
        batteries=[int(n) for n in line]
        bottom = 0
        top = len(batteries)

        digits = 12
        idx = 0
        high_list = []
        while digits > 0:
            digits -= 1
            # print(batteries[bottom+idx:top-digits], idx)
            high = max(batteries[bottom+idx:top-digits])
            high_list.append(high)
            idx = idx + batteries[bottom+idx:top-digits].index(high)+1
            # print(batteries[bottom+idx:top-digits], idx)

        # print(high_list)
        total += int(''.join(map(str,high_list)))
    
    print(f'Total: {total}')

    f.close()


if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/3
    Author: https://github.com/rpiga
    """
    test()