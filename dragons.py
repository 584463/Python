import random
import time
#########################FUNCTION###################################################
def displayIntro():
    print(""" You are in alnd full of dragons. in front of you,
    you see two caves. in one cave, there is a friendly dragon
    how will share his treasure with you. in the order is a
    hungry dragon, who will eat you on sight.

    _----~~~~~~~~~~~------___
                                  .  .   ~~//====......          __--~ ~~
                  -.            \_|//     |||\\  ~~~~~~::::... /~
               ___-==_       _-~o~  \/    |||  \\            _/~~-
       __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
   _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
 .~       .~       |   \\ -_    /  /-   /   ||      \   /
/  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
|~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
         '         ~-|      /|    |-~\~~       __--~~
                     |-~~-_/ |    |   ~\_   _-~            /\
                          /  \     \__   \/~                \__
                      _--~ _/ | .-~~____--~-/                  ~~==.
                     ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                -_     ~\      ~~---l__i__i__i--~~_/
                                _-~-__   ~)  \--______________--~~
                              //.-~~~-~_--~- |-------~~~~~~~~
                                     //.-~~~--\
    """
    )
def chooseCave():
    cave = None
    while cave != "1" and cave != "2":
        print("Wich cave  will you choose? (1 or 2)")
        cave = input()    
        return cave

def checkCave(chooseCave):
    print("You approach thr cave.")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A dragon jumps out in front of you! He opens his jaws and...")

    friendlyCave = random.randint(1,2)

    if friendlyCave == chooseCave:
        print("Gives you his treasure!")
    else:
        print("Eats you alive. The pain, the agony.")



#############################################################################
play = "Y"

while play == "Y":
    displayIntro()
    myCave = chooseCave()
    checkCave(myCave)
    play = input("Would you play again (Y/N)")