def printboard(xstate,zstate):
    Zero = 'x' if xstate[0] else ('O' if zstate[0] else 0)
    one = 'x' if xstate[1] else ('O' if zstate[1] else 1)
    two = 'x' if xstate[2] else ('O' if zstate[2] else 2)
    three = 'x' if xstate[3] else ('O' if zstate[3] else 3)
    Four = 'x' if xstate[4] else ('O' if zstate[4] else 4) 
    five = 'x' if xstate[5] else ('O' if zstate[5] else 5)
    six = 'x' if xstate[6] else ('O' if zstate[6] else 6)
    seven = 'x' if xstate[7] else ('O' if zstate[7] else 7)
    eight = 'x' if xstate[8] else ('O' if zstate[8] else 8)
    print(f"{Zero} | {one} | {two}")
    print(f"-- --- ---")
    print(f"{three} | {Four} | {five}")
    print(f"-- --- ---")
    print(f"{six} | {seven} | {eight}")

if __name__=="__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zstate=  [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn=1
    print("welcome to tic tac toe")
    while(True):
        printboard(xstate,zstate )
        if (turn ==1):
            print("X's chance")
            value=int(input("Enter the value: "))
            xstate[value]=1
        else:
            print("O's chance")
            value=int(input("Enter the value: "))
            zstate[value]=1
        turn= 1-turn