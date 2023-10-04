def draw_board(spaces):
    #print('\n * 30')
    print(f"{spaces[0]}|{spaces[1]}|{spaces[2]}")
    print("-+-+-")
    print(f"{spaces[3]}|{spaces[4]}|{spaces[5]}")
    print("-+-+-")
    print(f"{spaces[6]}|{spaces[7]}|{spaces[8]}")
    
def take_turn(player, spaces):


    choosing = True
    while choosing:
        spot =(
            int(input(f"Wich spot would you like, {player} ?")) - 1 
        )
        in_spot = spaces[spot]
        if isinstance(in_spot, int):
            spaces[spot] = player
            choosing = False
        else:
            print("That spot is full, try again.")

def check_win(spaces):
    '''
    [0, 1, 2,
    3, 4, 5,
    6, 7,8] '''
    if spaces[0] == spaces[1] and spaces[1] == spaces[2]:
        return True
    if spaces[3] == spaces[4] and spaces[4] == spaces[5]:
        return True
    if spaces[6] == spaces[7] and spaces[7] == spaces[8]:
        return True
    if spaces[0] == spaces[3] and spaces[3] == spaces[6]:
        return True
    if spaces[1] == spaces[4] and spaces[4] == spaces[7]:
        return True
    if spaces[2] == spaces[5] and spaces[5] == spaces[8]:
        return True
    if spaces[0] == spaces[4] and spaces[4] == spaces[8]:
        return True
    if spaces[2] == spaces[4] and spaces[4] == spaces[6]:
        return True

    return False #not a win.
 
 
def main():
    player = "X"
    spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
    draw_board(spaces)
    count = 0
    while count < 8:

        take_turn(player, spaces)
        draw_board(spaces)
        if check_win(spaces):
            print(f"Player {player} wins!")
            break
        else:
            count += 1
        if player == "X":
            player = "O"
        else:
            player = "X"
    if count == 8:
        print("It's a tie!")

main()
