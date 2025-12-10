def main():
    print("Hello.")
    f=open('test.txt', 'rt')

    banks=f.read().splitlines()
    total = 0

    for line in banks:
        digits = 13
        batteries=[int(n) for n in line]
        # print(batteries)
        high=[]
        # idx_max = -1
        # while digits > 0:
        #     batteries_slice = batteries[idx_max + 1:len(batteries) - digits]
        #     batteries_max = max(batteries_slice)
        #     idx_max = batteries_slice.index(batteries_max)
        #     print(f'max: {batteries_max} idx: {idx_max}')
        #     high.append(batteries_max)
            
        #     digits-=1

        #     print(f'{line}: {batteries_slice} {batteries_max} {high} {digits}')
        idx_start = 0

        while digits > 0:
            batteries_slice = batteries[idx_start:len(batteries)-digits]
            battery_max = max(batteries_slice)
            high.append(battery_max)
            idx_max = batteries_slice.index(battery_max)
            idx_start += idx_max + 1

            print(f'{line}: {batteries_slice} {idx_start} {battery_max} {high} {digits}')
            digits-=1

        print(high)
        total += int(''.join(map(str,high)))
        # batteries_slice = batteries[idx_start:len(batteries)-11]
        # max1 = max(batteries_slice)
        # idx_max1 = batteries_slice.index(max1)
        # high.append(max1)

        # print(f'{line}: {batteries_slice}  {idx_start} {max1} {high}')
        # idx_start += idx_max1 +1
        # batteries_slice = batteries[idx_start:len(batteries)-10]
        # max2 = max(batteries_slice)
        # idx_max2 = batteries_slice.index(max2)
        # high.append(max2)

        # print(f'>> {line}: {batteries_slice} {idx_start} {max2} {high}')
        # idx_start += idx_max2+1
        # batteries_slice = batteries[idx_start :len(batteries)-9]
        # max3 = max(batteries_slice)
        # idx_max3 = batteries_slice.index(max3)
        # high.append(max2)

        # print(f'>> {line}: {batteries_slice}  {idx_start} {max3} {high}')

        
        # high.append(max2)



        
        # print(high)

    print(f'Total: {total}')

    f.close()




if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/3
    Author: https://github.com/rpiga
    """
    main()