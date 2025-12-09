def main():
    print("Hello.")
    f=open('input.txt', 'rt')

    banks=f.read().splitlines()
    total = 0
    digits = 12

    for line in banks:
        batteries=[int(n) for n in line]
        # print(batteries)
        high=0

        max1 = max(batteries[0:len(batteries)-digits])
        idx(max1) = batteries
        
        # print(high)
        total += high

    print(f'Total: {total}')

    f.close()

if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/3
    Author: https://github.com/rpiga
    """
    main()