USA_points = 1
Argentina_points = 0
Spain_points = 0
# hey this is the first question to the soccer game you got it!
answer1 = input ("you are on team USA vs Spain, and Argentina in a three way match. Your teammate has the soccer ball. Do you A call for the ball, B do not do anything, and wait for your team to do something, or C go get open and then call for the ball ")
if answer1 == "A" or answer1 == "a":
    print ("your teammate sees you and attempts to pass it but then argentina interceps the pass and passes it to Messi and he obviously scores. BAD DECISION.")
    Argentina_points += 1
elif answer1 == "B":
    print ("Your teammate make a big mistake that spain capitolizes on and takes the bal passes it to the goat lamine yamal, and obviously scores on you. BAD DECISION.")
    Spain_points += 1
elif answer1 == "C":
    print ("you get open near the goalie box, call for the ball, and you bang it top left corner and score. GREAT DECISION")
    USA_points += 1

answer2 = input ("You and your team reset and are feeling good, but right after spain gets the ball again lamine yamal is coming straight at you looking thirsty for a goal and zoned in, what do you do? A, do nothing. B, lunge out and attempt to steal the ball. C stay in a good position and wait to see what he is going to do?")
if answer2 == "A":
    print ("You get nutmeged and get clowned for it. Lamine yamal then dribbles your entire team and obviously scores. BAD CHOICE ")
    Spain_points += 1
elif answer2 == "B":
    print ("you lunge out, but then lamine just does a maradona and you are cooked lamine yamal then decides to play with your team and meg 5 people then score obviously. BAD CHOICE")
    Spain_points += 1
elif answer2 == "C":
    print ("You make lamine yamal pass the ball off to a teammate because of your position and a teammate of yours steals the ball from that person and gives you a through ball you easily pass it in bottom right corner. GREAT DECISION")
    USA_points += 1

answer3 = input ("You now have the ball and are going straight for argentina what move are you going to pull out of yoyr bag? A, do some scizors and go left, B do a mardona to the right, or C do five fakes to the right do a maradona some scizors, a stepover fake meg rainbow bycicle and shoot from half field?")
if answer3 == "A":
    print ("You do the scizors but a fan of messi runs on the pitch steals the ball and passes it to messi, he scores obviously. BAD CHOICE ")
    Argentina_points += 1
elif answer3 == "B":
    print ("You mess up in the spin lose control of the ball it rolls to the defence feet lamine... you know what, you already know what is going to happen... BAD CHOICE")
    Spain_points += 1
elif answer3 == "C":
    print ("You bang it into top bins from half field. GREAT DECISION")
    USA_points += 1


answer4 = input ("You are in your box argentina has a corner on you, do you A try to header it out of the box. B try to bycicle kick it from your box all the way to the opponents goal, or C use your chest to control it then kick it out.")
if answer4 == "A":
        print ("You header it out but of course the main character: Lionel Messi is there waiting. you are cooked, and I think you know what happens. BAD CHOICE ")
        Argentina_points += 1
elif answer4 == "B":
        print ("You somehow make the bycicle kick from your goalie box everyone goes crazy. AMAZING CHOICE")
        USA_points += 1
elif answer4 == "C":
        print ("You succesfully trap it and get it out. jk lamine crossed it back in and raphina headers it in. BAD DECISION")
        Spain_points += 1



answer5 = input ("It is the end of the game,you have the ball, and you are feeling the pressure, A what is your move try to meg defender 1 to the left. B, defender 2 in the middle, or C the right defender?")
if answer5 == "A":
                print ("You go to the left and the defender cuts off your angle you get trapped by the other 2 spain defenders they take the ball, and they score. BAD CHOICE ")
                Spain_points += 1
elif answer5 == "B":
                print ("You try to meg the guy in the middle, but the other two defenders on the right and the left trap you you realize one of the defenders in messi you give up and just let them take it they score. AMAZING CHOICE")
                Argentina_points += 1
elif answer5 == "C":
                print ("You are right, right is the right decision you cut to the right, your just about to get called out of bounds but you tap the ball and it stays in, you cross it in the box and someone on your team headers it in. BAD DECISION")
                USA_points += 1

                # end of game! 
if USA_points > Argentina_points and USA_points > Spain_points:
      print ("YOU ARE THE WINNER LETS GOOOOOOOOOO!!!!!")
elif Argentina_points > USA_points and Argentina_points > Spain_points:
      print ("you lost argentina wins")
elif Spain_points > Argentina_points and Spain_points > USA_points:
      print ("you lose spain wins....... LETS GO LAMINE YAMAL")

      #if argentina gets the most points then argentina wins, if USA gets the most points USA wins, if Spain gets the most points then spain wins the game.