def main():
    print("Hello.")
    f=open('input.txt', 'rt')

    banks=f.read().splitlines()
    total = 0

    for line in banks:
        batteries=[n for n in line]
        # print(batteries)
        high=0

        for i in range(0, len(batteries)):
            for j in range(1+i, len(batteries)):
                temp = int(batteries[i])*10 + int(batteries[j])
                high = temp if temp > high else high
        
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