def main():
    print("Hello, day 4.")
    f = open('test.txt', 'rt')
    total = 0
    
    rolls = f.read().splitlines()



    print(f'Total: {total}')
    f.close()
if __name__ == "__main__":
    """
    https://adventofcode.com/2025/day/4
    Author: https://github.com/rpiga
    """
    main()