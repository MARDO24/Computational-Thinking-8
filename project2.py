place1 = input ("Where will you go? japan or paris?(No captials or spaces in your answer)")
if place1 == "paris":
    class1 = input ("Do you fly first class, or economy?")
    if class1 == "first class":
        print ("you drink some awesome grape koolaid!")
        input()
        crossaint = input ("do u eat croisan")
        if crossaint == "yes":
            print ("It was a very good Croisan and you are very happy")
            input()
        elif crossaint == "no":
            print ("Too bad you eat croisan and be happy")
            input()
    if class1 == "economy":
        print ("You are very uncomfortable your entire flight")
        input()
        eifle = input ("Do you want to go to the eifel tower")
        if eifle == "no":
            print ("You go home very sad")
        elif eifle == "yes":
            print ("You accidentaly fall of eifle tower and die")
            input()
    else:
        print ("Since you couldn't decided or spell correctly you miss your flight and go home sad")
elif place1 == "japan":
    place2 = input ("do you go to tokyo or kyoto first?")
    if place2 == "tokyo":
        place3 = input ("do you go to the poke center")
        if place3 == "yes":
            pull = input("Do you buy the 30th anniversary set or a different pack?")
            if pull == "30th anniversary set":
                print ("You pull the mew and the mewtwo and get a million dollar")
                input()
            if pull == "different pack":
                print ("You pull nothing and lose all of your money.")
            else:
                print ("mmm ok no nevermind you go home and get nothing.")
    if place3 == "kyoto":
        place3 = input ("do you go and visit an onsen, or in other words a hot spring?")
        if place3 == "yes":
            print ("you go to the hot spring, and chill for a really long time and fall asleep then you wake up and go to bed.")
        elif place3 == "no":
            print ("ok you go to see the really cool traditional archetecture and have a blast then go home and sleep.")
        else:
            print ("ok then I see how it is... you go home and are sad.")
else:
    print ("Since you couldn't spell correctly you realize that you have no money so you go take a nap and be sad.")