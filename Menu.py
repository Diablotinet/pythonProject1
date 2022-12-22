print("Welcome")
time.sleep(1)
choice_intro =str(input("Do you want to play to this awesome game ??    Yes or No    :"))
while choice_intro != "Yes" :
    time.sleep(1)
    print("Game over!!! You can't win if you don't play")
    choice_intro = str(input("Do you want to play to this awesome game ??    Yes or No    :"))

print()
print ( "You have made the right choice    You win ", end="")
time.sleep(2)
print("the right to begin the game")

choice_menu=int(input("1.Play\n2.Rules"))
if choice_menu== 2 :
    print("To win, you have to complete all the empty line by using the block available.\nYou loose if you fail to place correctly three times in a row a block on the board.")
if choice_menu == 1:
    print("LOADING OF THE TEXTURES [0            ]")
    time.sleep(1)
    print("LOADING OF THE TEXTURES [000          ]")
    time.sleep(1)
    print("LOADING OF THE TEXTURES [00000        ]")
    time.sleep(1)
    print("LOADING OF THE TEXTURES [000000000000 ]\nLoading complete")
