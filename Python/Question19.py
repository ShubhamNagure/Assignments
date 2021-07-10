def finalPosition(move):
 
    l = len(move)
    countUp, countDown = 0, 0
    countLeft, countRight = 0, 0
 
    # traverse the instruction string
    # 'move'
    for i in range(l):

        
        # for each movement increment
        # its respective counter
        if (move[i] == 'up'):
            countUp += 1
 
        elif(move[i] == 'down'):
            countDown += 1
 
        elif(move[i] == 'left'):
            countLeft += 1
 
        elif(move[i] == 'right'):
            countRight += 1
 
    # required final position of robot
    print("Total distance covered : ", (countRight + countLeft + countUp + countDown))

 
 
# Driver code
if __name__ == "__main__" :
    inp = ""
    valid_move=[]
    while inp != "stop":
        inp = input("Enter move 'UP','DOWN', 'RIGHT','LEFT','STOP' : ").lower()
        valid_move.append(inp)

    finalPosition(valid_move)