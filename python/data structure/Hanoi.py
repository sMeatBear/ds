'''
    To print the move progess
    Param:
    - num: the mark of the plate
    - start: Start point
    - end: destination
'''
def move(num: int, start: str, end: str) -> None:
    print("#", num, ": ", start, "->", end)


'''
    A recursive method to solve Hanoi problem
    Param:
    - scale: the total level of Hanoi
    - start: the original location
    - transfer: middle rod for transferring
    - end: the destination of plates
'''
def Hanoi(scale, start, transfer, end):
    if scale == 1:
        # if there is only one plate
        move(scale, start, end)
    else:
        # only focus how to move the n-1 plate to the middle rod,
        # using end rod as a transfer station4
        Hanoi(scale-1, start, end, transfer)
        # move the n plate to the destination
        move(scale, start, end)
        # move the n-1 plate to the destination
        Hanoi(scale-1, transfer, start, end)

n = int(input('Input the number of plates: '))
Hanoi(n, 'A', 'B', 'C')
