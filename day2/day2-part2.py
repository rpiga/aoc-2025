def divisors(n):
    v=[]
    for i in range(2, (n//2)+1):
        if n % i == 0:
            v.append(i)
    return v


def main():
    f=open('test.txt', 'rt')

    list = f.read().split(',')

    total=0
    for l in list:
        item = l.rstrip().split('-')
        item_bottom = int(item[0])
        item_top = int(item[1])
        
        for i in range(item_bottom, item_top+1):
            i_s = str(i)

            # Verify if all digits are the same
            i_list = [ int(n) for n in i_s ]
            if len(i_s) > 1 and len(set(i_list)) == 1:
                #print(f'{i}')
                total+=i
            else:
                divs = divisors(len(i_s))
                slices=[]
                for d in divs:
                    slices = [ i_s[k:k+d] for k in range(0, len(i_s), d) ]
                    if len(set(slices)) == 1:
                        #print(f'{i}\t{len(i_s)}\t{slices}')
                        total+=i
                        break                 
        
    print(f'Total: {total}')


    f.close()

if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/2
    """
    main()