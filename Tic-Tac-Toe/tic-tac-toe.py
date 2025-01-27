my_board={
        '7':'7','8':'8','9':'9',
        '4':'4','5':'5','6':'6',
        '1':'1','2':'2','3':'3',
}

def board():
    
    print(f"{my_board['7']} | {my_board['8']} | {my_board['9']}")
    print(f'---------')
    print(f"{my_board['4']} | {my_board['5']} | {my_board['6']}")
    print(f'---------')
    print(f"{my_board['1']} | {my_board['2']} | {my_board['3']}")

def game():
    turn='X'
    count=0

    for x in range(10):

        while True:
            board()
            print(f"It's your turn: {turn} , move to which place?\n")
            move=input()
                
            try:
                if my_board[move]!="X" and my_board[move]!="O":
                    my_board[move]=turn
                    count+=1
                    break
                else:
                    print("There is a value in that position please choose again:")
            except:
                print('please enter a number between 1 and 9')
                continue
                
        
        if count>=5:
            if my_board['7']==my_board['8']==my_board['9']:
                print('Game Over')
                print(f'The winner is: {turn}')
                break
            if my_board['4']==my_board['5']==my_board['6']:
                    print('Game Over')
                    print(f'The winner is: {turn}')
                    break
            if my_board['1']==my_board['2']==my_board['3']:
                print('Game Over')
                print(f'The winner is: {turn}')
                break

            if my_board['7']==my_board['4']==my_board['1']:
                print('Game Over')
                print(f'The winner is: {turn}')
                break
            if my_board['8']==my_board['5']==my_board['2']:
                print('Game Over')
                print(f'The winner is: {turn}')
                break
            if my_board['9']==my_board['6']==my_board['3']:
                print('Game Over')
                print(f'The winner is: {turn}')
                break

            if my_board['7']==my_board['5']==my_board['3']:
                print('Game Over')
                print(f'The winner is: {turn}')
                break
            if my_board['1']==my_board['5']==my_board['9']:
                print('Game Over')
                print(f'The winner is: {turn}')
                break

        if turn=='X':
            turn='O'
        else:
            turn='X'
    if count==9:
        print('Game Over')
        print('Nobody won')




game()

