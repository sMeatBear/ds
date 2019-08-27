"""
    Use queue structure to print coefficients of all the (a+b)**n (n>0) (Yanghui tri)

    Params:
    - n: the exponent of (a+b)**n
"""
def yanghui(n: int) -> None:
    # initial the first row
    q = [1, 1]
    # s is a pointer
    s = 0
    for i in range(1, n + 1):
        # add 0 to end of the row
        q.append(0)

        # add elem to a new line
        for j in  range(1, i + 3):
            # add elem to queue
            # first elem out of queue
            t = q.pop(0)
            
            q.append(s + t)
            # move to next
            s = t

            if j != i + 2: 
                print(s, end=' ')

        # end of the row
        print()


n = int(input('Please input n: '))
yanghui(n)

