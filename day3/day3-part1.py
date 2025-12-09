def mainv2():
    print("Hello v2.")
    f=open('input.txt', 'rt')

    banks=f.read().splitlines()
    total = 0

    for line in banks:
        high = 0
        batteries=[int(n) for n in line]

        item_max = max(batteries[0:len(batteries)-1])
        idx_item_max = batteries[0:len(batteries)-1].index(item_max)
        
        item_low = max(batteries[idx_item_max+1:len(batteries)])
        
        high += (item_max*10) + item_low
        total += high

    print(f'Total: {total}')
    f.close()

def main():
    print("Hello.")
    f=open('test.txt', 'rt')

    banks=f.read().splitlines()
    total = 0

    for line in banks:
        batteries=[n for n in line]
        # print(batteries)
        high=0
        fb=''.join(batteries)
        for i in range(0, len(batteries)):
            for j in range(1+i, len(batteries)):
                temp = int(batteries[i])*10 + int(batteries[j])
                high = temp if temp > high else high
                #print(f"{fb[0:i]}\x1b[30;41m{fb[i]}{fb[j]}\x1b[0m{fb[j:len(batteries)]}")
        
        #print(high)
        total += high

    print(f'Total: {total}')

    f.close()

if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/3
    Author: https://github.com/rpiga
    """
    mainv2()