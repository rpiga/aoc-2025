def main():
    f = open('test.txt', 'rt')

    list = f.read().split(',')

    for l in list:
        item = l.split('-')
        item_top = item[0]
        item_bottom = item[1]
        
        print(f'>>> {item}\t{item_top}\t{item_bottom}')

    f.close()

if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/2
    """
    main()