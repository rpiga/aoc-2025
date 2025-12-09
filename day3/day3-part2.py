def main():
    print("Hello.")
    f=open('test.txt', 'rt')

    banks=f.read().splitlines()
    total = 0
    digits = 13

    for line in banks:
        batteries=[int(n) for n in line]
        # print(batteries)
        high=[]

        max1 = max(batteries[0:len(batteries)-digits])
        idx_max1 = batteries[0:len(batteries)-digits].index(max1)
        high.append(max1)

        print(f'{line}: {batteries[0:len(batteries)-digits]} {high}')

        max2 = max(batteries[idx_max1:len(batteries)-(digits+1)])
        # idx_max2 = batteries[idx_max1+1:len(batteries)-digits+1].index(max2)
        print(f'>> {line}: {batteries[idx_max1:len(batteries)-(digits+1)]} {high}')
        
        # high.append(max2)



        
        # print(high)
    total += int(''.join(map(str,high)))

    print(f'Total: {total}')

    f.close()




if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/3
    Author: https://github.com/rpiga
    """
    main()