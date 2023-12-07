print("PongSimulator")
print ("You arrive at the pong arena. In front of you is a controller and a giant screen. Your opponent sits adjacent to you, and picks up their controller. You pick up yours as well. The game starts. the pong ball is just about to pass your paddle.")
print ("What would you like to do?")

print ("1. Try to stop the ball with your paddle  2. Throw your controller at your opponent in an attempt to distract them 3.Let your opponent win out of the kindness of your heart")

responses = input("")



if(responses =="1"): 
    print ("You manage to block the ball from your goal, and your opponent tries the same, but fails. You currently have 1 point, and need 7 to win. What will you do now?")
    
elif (responses =="2"):
    print ("You knock out your opponent cold. You just committed a crime! you run away from the stage in panic and hide amongst the crowd.")
   
elif (responses == "3"):
    print (" You let the opponent score a point, perhaps out of pity or because you want to make this interesting. The opponent now has one point and is very confused. You need 7 Points to win.")
else:
    print('choose a correct number')