def factorize(n):
    print('factorz.')
    factors=[]
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                factors.append(i)
                break
    return factors

def main():
    f=open('test.txt', 'rt')

    list = f.read().split(',')

    for l in list:
        item = l.rstrip().split('-')
        item_bottom = int(item[0])
        item_top = int(item[1])
        
        print(f'>>> {item}\t{item_top}\t{item_bottom}')

        item_length=0

        for i in range(item_bottom, item_top+1):
            if len(str(i))%2 != 0:
                print(f'{i}: pass')
            else:
                if len(str(i)) != item_length:
                    item_length=len(str(i))
                    fact=factorize(item_length)
                
                # if item_length%2 == 0:
                print(f'{i}: {fact}')

    f.close()

if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/2
    """
    main()