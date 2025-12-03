def factorize(n):
    factors=[]
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                factors.append(i)
                break
    return set(factors)

def main():
    f=open('test2.txt', 'rt')

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
            if len(set(i_list)) == 1:
                print(i)
                total+=i
            elif len(i_s)  in [3, 7, 11, 13]:
                pass
            else:
                fact = factorize(len(i_s))
                for j in fact:
                    slices=[ i_s[k:k+j] for k in range(0, len(i_s), j) ]

                    print(f'>> {i}\t\t{j}\t\t{slices}')
                    # if len(slices) > 1 and len(set(slices)) == 1:

            # for j in [i_list]:           
            #     if len(set(j)) == 1:
            #         total+=i
            #         break
            #     else:
            #         continue
            # print(f'>> {i_s}')

                    # print(f'>> {i}\t\t{len(i_list)}:{j[0]}:{sum(i_list)}')
                # elif len(j) in [3, 7, 11, 13]:
                #     break
                # else:
                #     fact = factorize(len(j))
                #     # print(f'>> {i}\t\t{j}\t\t{fact}')
                #     slices = []
                #     for k in fact:
                #         slices = [ str(i)[ia:ia+1] for ia in range(0, len(i_s), k) ]
                #         print(f'{i}\t\t{k}\t\t{slices}')
                    #     slices = []
                    #     parts.append(j[k:k+fact])
                    # print(f'>> {i}\t\t{parts}')
                        


                    
        
    print(f'Total: {total}')


    f.close()

if __name__ == '__main__':
    """
    https://adventofcode.com/2025/day/2
    """
    main()