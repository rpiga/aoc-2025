def main():
    f=open('test.txt', 'rt')

    list = f.read().split(',')

    total=0
    for l in list:
        item = l.rstrip().split('-')
        item_bottom = int(item[0])
        item_top = int(item[1])
        
        # print(f'>>> {item}\t{item_top}\t{item_bottom}')

        for i in range(item_bottom, item_top+1):
            if len(str(i))%2 != 0:
                pass
                # print(f'{i}: pass')
            else:
                i_s = str(i)
                item_left, item_right = i_s[:len(i_s)//2], i_s[len(i_s)//2:]

                if item_left == item_right:
                    total+=i
                    # print(f'{i}: {item_left} {item_right}')
                    
        
    print(f'Total: {total}')

    f.close()

if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/2
    """
    main()