from gamepath import like,won,finger,died,room,haha, intro, gun, one, boss,oneelse, door,doorif1, doorif2, doorelse, trap1,sad, trapwon

game = input('Type yes to start the game: ')
intro()
machiengun = input(' type "gun" for gun and "door" for the door and "room" to go the mysteirous treasure room. ')
if machiengun == 'gun' :
    gun() 
    leader = input('Type "1" or "2" fill in ur answer befor their leader rip u apart :D ')
    if leader == '1' :
        one()
        boss()
    else :
        oneelse()
if machiengun =='door' :
    door()
    deur = input('Type in "right" to go right and "left" to go left: ')
    if deur == 'right' :
        doorif1()
        trap = input('Type "1" to run through, type "2" to walk carfully. ')
        if trap == '1' :
            doorif2()
            print(haha())
    else : 
        doorelse()
        trap = input('Type "1" to run through, type "2" to walk carfully. ')
        print('')
        if trap == '1' :
            trap1()
            print(sad())
        else :
            trapwon()
if machiengun == "room":
    room()
    fruit = int(input('How many bites do u want to take? '))
    if fruit >= 3 :
        died() 
        print(finger())
    if fruit == 2 : 
        died()
        print(boss())
    if fruit == 1 : 
        print('u gained the power, and killed the mosnter king!')
        print('')
        won() 
        print(like())