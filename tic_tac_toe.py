

#Display

#display_list = ["x","o","x","o","x","o","x","o","x"]
display_list = [' ']*10

def display():
    print(display_list[0] + '|' + display_list[1] + '|' + display_list[2])
    print(display_list[3] + '|' + display_list[4] + '|' + display_list[5])
    print(display_list[6] + '|' + display_list[7] + '|' + display_list[8])




def take_input():
    global player_one
    global player_two
    global p1_name
    global p2_name
    player_one = input("Enter your name PLayer one: ")
    player_two = input("Enter your name player two: ")
    p1_name = player_one
    p2_name = player_two
    

    options = ["x","o"]
    ask = "Wrong"
    while ask not in options:
        print(player_one, 'choose what you like to be (x or o? )')
        ask = input()


        if ask == options[0]:
            print(player_one, "chose {}".format(options[0]))
            print("And", player_two, " is {}".format(options[1]))
            player_one = options[0]
            player_two = options[1]
            
        elif ask == options[1]:
            print(player_one,"chose {}".format(options[1]))
            print("And", player_two," is {}".format(options[0]))
            player_one = options[0]
            player_two = options[1]
            
        else:
            print("Please chose 'x' or 'o' ")
        
                  
#Player one
def player1_choice():
    #display(display_list)
    print(p1_name,"what position would you like to change (0,8): ")
    ask = input()
    return int(ask)



   
def player1_replacement(default_list,position):
    global display_list
    if display_list[position] == ' ':
        display_list[position] = player_one
    else:
       print('That position is taken')

#player two
def player2_choice():
    #display(display_list)
    print(p2_name, "what position would you like to change (0,8): ")
    ask = input()
    return int(ask)


   
def player2_replacement(default_list,position):
    global display_list
    if display_list[position] == ' ':
        display_list[position] = player_two
    else:
       print('That position is taken')


def main():
    display()
    take_input()
    run = True
    while run:
        
        #player 1
        p1_choice = player1_choice()
        player1_replacement(display_list,p1_choice)
        #player 2
        p2_choice = player2_choice()
        player2_replacement(display_list,p2_choice)
        display()
        

main()
    
    
