#Variables for the aesthetics of the game are created.
reset = "\033[0;0m"
bold = "\033[1m"
italics = '\x1B[3m'
underline = '\033[4m'
green = '\033[32m'
blue = '\033[94m'
yellow ='\033[93m'
red = '\033[31m'
hblack = "\033[40m"
oddred = '\033[91m'

#Imports the modules 'random' and 'time'.
import random
import time

#Prints the start message.
print("⊡ {0}{1}{2}DICE GAMEZ OFFICIAL™{3} ⊡ ".format(bold,underline,green,reset).center(60))
print("\n{0}{1}{2}~Play the game, rise to fame~{3}".format(italics,blue,hblack,reset))
print("{0}\nCREATOR: Ruben{1}".format(yellow,reset))
#Outputs 'LOADING...' and delays program for 2 seconds.
print("\nLOADING...")
time.sleep(2)

#Asks the user to enter the password. If the password is not 'diceGAM3Z' the user is asked to enter it again.
print("\nTo continue you must enter a password...")
userPassword = input("{0}Enter password:{1}\t".format(bold,reset))
while userPassword != "diceGAM3Z":
  print("{0}Invalid Password{1}".format(red,reset))
  userPassword = input("{0}Enter password:{1}\t".format(bold,reset))
#Outputs 'LOADING...' and delays program for 2 seconds.
print("\nLOADING...")
time.sleep(2)

#Asks player-1 and player-2 to enter their names and welcomes them to the game.
player1 = input("{0}{1}PLAYER-1{2}{1} - Enter your name:{2}\t".format(bold,blue,reset))
print("{1}{2}Welcome {0}! Now who will you be facing today?{3}".format(player1,italics,blue,reset))
player2 = input("{0}{1}PLAYER-2{2}{1} - Enter your name:{2}\t".format(bold,blue,reset))
print("{1}{2}Welcome {0}!{3}".format(player2,italics,blue,reset))
time.sleep(0.5)
print("\n{2}{0} VS {1}{3}".format(player1,player2,bold,reset))
time.sleep(0.5)

#Outputs the rules of the game.
print("\n{2}⇝ {0}{1}THE RULES{3}{2}⇜{3}".format(bold,underline,green,reset))
print("{0}• The points rolled on each player’s dice are added to their score.\n• If the total is an even number, an additional 10 points are added to their score.\n• If the total is an odd number, 5 points are subtracted from their score.\n• If they roll a double, they get to roll one extra die and get the number of points rolled added to their score.\n• The score of a player cannot go below 0 at any point.\n• The person with the highest score at the end of the 5 rounds wins.\n• If both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins).{1}\n".format(green,reset))

print("{0}⚔LET THE BATTLE COMMENCE⚔{1}".format(hblack,reset).center(60))

#score1 and score2 gets the value of 0.
score1 = 0 
score2 = 0
#Will repeat 5 times for 5 rounds.
for rounds in range(1,6):
  #Delays program for 1 second.
  time.sleep(1)
  #Outputs Round number.
  print("\n{0}{1}{2}ROUND-{3}{4}".format(yellow,bold,hblack,rounds,reset))
  #Asks the user to enter 'X' to roll the dice.
  rollp1 = input("{0}{1}{2}{3}{0}, roll the dice! Press 'X' to roll:\t".format(bold,yellow,player1,reset)).upper()
  #WHILE the user entry is not equal to 'X' the program asks the user to enter it again.
  while rollp1 != 'X':
    print("{0}Invalid Entry{1}".format(red,reset))
    rollp1 = input("{0}{1}{2}{3}{0}, roll the dice! Press 'X' to roll:\t".format(bold,yellow,player1,reset)).upper()
  #Generates the random numbers for the dice.
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  #Outputs the dice that player-1 rolled.
  print("{0}{1} you rolled a {2} and a {3}{4}".format(bold,player1,dice1,dice2,reset))
  #Calculates the total of the dice by adding them together.
  total1 = dice1 + dice2
  #IF the total is EVEN...
  if (total1%2) == 0:
    #Adds 10 to the total.
    total1+=10
    #Outputs that player-1 has got an EVEN TOTAL.
    print("😸{0}{1}  EVEN TOTAL (+10){2}😸".format(bold,yellow,reset))
  #ELSE the total is ODD...
  else:
    #Subtracts 5 from the total.
    total1-=5
    #Outputs that player-1 has got an ODD TOTAL.
    print("😈{0}{1}  ODD TOTAL (-5){2}😈".format(bold,oddred,reset))
  #IF the user rolls a double...
  if dice1 == dice2:
    #Outputs a bonus round for player-1.
    print("🍀{0}{1}  DOUBLE TROUBLE ROUND{2}🍀".format(bold,green,reset))
    #Asks the user to enter 'X' to roll the bonus die.
    doubleRollp1 = input("{0}{1}{2}{3}{0}, roll the die! Press 'X' to roll:\t".format(bold,green,player1,reset)).upper()
    #WHILE the user entry is not equal to 'X' the program asks the user to enter it again.
    while doubleRollp1 != 'X':
      print("{0}Invalid Entry{1}".format(red,reset))
      doubleRollp1 = input("{0}{1}{2}{3}{0}, roll the die! Press 'X' to roll:\t".format(bold,green,player1,reset)).upper()
    #Generates the random numbers for the die.
    doubleDiep1 = random.randint(1,6)
    #Outputs the die that player-1 rolled.
    print("{0}{1}{2} you rolled a {3}{4}".format(bold,green,player1,doubleDiep1,reset))
    #Adds the bonus die to the total.
    total1 += doubleDiep1
  #Checks if the player-1 score goes below 0. If it is the score gets the value of 0.
  check1 = score1 + total1
  if check1 < 0:
    score1 = 0
  else:
    #Adds the final score of the round to the total.
    score1 += total1
  #Outputs the total for the round and the overall score.
  print("{0}Total for ROUND-{1} {6}: {2}{3}{4}\n{0}Overall SCORE: {2}{5}{4}".format(blue,rounds,bold,total1,reset,score1,player1))

  #Asks the user to enter 'X' to roll the dice.
  rollp2 = input("{0}{1}{2}{3}{0}, roll the dice! Press 'X' to roll:\t".format(bold,yellow,player2,reset)).upper()
  #WHILE the user entry is not equal to 'X' the program asks the user to enter it again.
  while rollp2 != 'X':
    print("{0}Invalid Entry{1}".format(red,reset))
    rollp2 = input("{0}{1}{2}{3}{0}, roll the dice! Press 'X' to roll:\t".format(bold,yellow,player2,reset)).upper()
  #Generates the random numbers for the dice.
  dice3 = random.randint(1,6)
  dice4 = random.randint(1,6)
  #Outputs the dice that player-2 rolled.
  print("{0}{1} you rolled a {2} and a {3}{4}".format(bold,player2,dice3,dice4,reset))
  #Calculates the total of the dice by adding them together.
  total2 = dice3 + dice4
  #IF the total is EVEN...
  if (total2%2) == 0:
    #Adds 10 to the total.
    total2+=10
    #Outputs that player-2 has got an EVEN TOTAL.
    print("😸{0}{1}  EVEN TOTAL (+10){2}😸".format(bold,yellow,reset))
  #ELSE the total is ODD...
  else:
    #Subtracts 5 from the total.
    total2-=5
    #Outputs that player-2 has got an ODD TOTAL.
    print("😈{0}{1}  ODD TOTAL (-5){2}😈".format(bold,oddred,reset))
  #IF the user rolls a double...
  if dice3 == dice4:
    #Outputs a bonus round for player-2.
    print("🍀{0}{1}  DOUBLE TROUBLE ROUND{2}🍀".format(bold,green,reset))
    #Asks the user to enter 'X' to roll the bonus die.
    doubleRollp2 = input("{0}{1}{2}{3}{0}, roll the die! Press 'X' to roll:\t".format(bold,green,player2,reset)).upper()
    #WHILE the user entry is not equal to 'X' the program asks the user to enter it again.
    while doubleRollp2 != 'X':
      print("{0}Invalid Entry{1}".format(red,reset))
      doubleRollp2 = input("{0}{1}{2}{3}{0}, roll the die! Press 'X' to roll:\t".format(bold,green,player2,reset)).upper()
    #Generates the random numbers for the die.
    doubleDiep2 = random.randint(1,6)
    #Outputs the die that player-1 rolled.
    print("{0}{1}{2} you rolled a {3}{4}".format(bold,green,player2,doubleDiep2,reset))
    #Adds the bonus die to the total.
    total2 += doubleDiep2
  #Checks if the player-1 score goes below 0. If it is the score gets the value of 0.   
  check2 = score2 + total2
  if check2 < 0:
    score2 = 0
  else:
    #Adds the final score of the round to the total.
    score2 += total2
  #Outputs the total for the round and the overall score.
  print("{0}Total for ROUND-{1} {6}: {2}{3}{4}\n{0}Overall SCORE: {2}{5}{4}".format(blue,rounds,bold,total2,reset,score2,player2))
  #Delays program for 0.5 seconds.
  time.sleep(0.5)
  #Outputs a divider for the next round.
  print("◍"*90)
#WHILE the player-1 score is the smae as the player-2 score.
while score1 == score2:
  #Outputs Sudden Death round.
  print("{0}We have a tie!{1}".format(blue,reset))
  print("🗲{0}{1}SUDDEN DEATH{2}🗲".format(bold,blue,reset))
  #Asks player-1 to enter 'X' to roll the tiebreaker die.
  tieRollp1 = input("{0}{1}{2}{3}{0}, roll the die! Press 'X' to roll:\t".format(bold,blue,player1,reset)).upper()
  #WHILE the user entry is not equal to 'X' the programm asks the user to enter it again.
  while tieRollp1 != 'X':
    print("{0}Invalid Entry{1}".format(red,reset))
    tieRollp1 = input("{0}{1}{2}{3}{0}, roll the die! Press 'X' to roll:\t".format(bold,blue,player1,reset)).upper()
  #Generates the random numbers for the die.
  tieDiep1 = random.randint(1,6)
  #Outputs the total for the round and the overall score.
  print("{0}{1}{2} you rolled a {3}{4}".format(bold,blue,player1,tieDiep1,reset))
  #Adds the value of the die to the score.
  score1 += tieDiep1
  #Asks player-2 to enter 'X' to roll the tiebreaker die.
  tieRollp2 = input("{0}{1}{2}{3}{0}, roll the die! Press 'X' to roll:\t".format(bold,blue,player2,reset)).upper()
  #WHILE the user entry is not equal to 'X' the programm asks the user to enter it again.
  while tieRollp2 != 'X':
    print("{0}Invalid Entry{1}".format(red,reset))
    tieRollp2 = input("{0}{1}{2}{3}{0}, roll the die! Press 'X' to roll:\t".format(bold,blue,player2,reset)).upper()
  #Generates the random numbers for the die.
  tieDiep2 = random.randint(1,6)
  #Outputs the total for the round and the overall score.
  print("{0}{1}{2} you rolled a {3}{4}".format(bold,blue,player2,tieDiep2,reset))
  #Adds the value of the die to the score.
  score2 += tieDiep2
#IF the player-1 score is greater than the player-2 score...
if score1 > score2:
  print("\nThe victor has been decided...")
  #Delays program for one second.
  time.sleep(1)
  #Outputs the winner and the scores of both players.
  print("🥇  {0}{1}, you are the winner!{2}🥇".format(bold,player1,reset))
  print("↪ {0}{1}THE SCORES{2}↩".format(bold,underline,reset))
  print("{0}-{1}\n{2}-{3}".format(player1,score1,player2,score2))
  #Opens 'leaderboard.txt' in append mode.
  file1 = open("leaderboard.txt","a")
  #Adds the player-1 details (name and score) to the file.
  file1.write(player1 + ',' + str(score1) + '\n')
  #Closes the file.
  file1.close()
#ELSE the player-2 score is greater than the player-1 score...
else:
  print("\nThe victor has been decided...")
  #Delays program for one second.
  time.sleep(1)
  #Outputs the winner and the scores of both players.
  print("🥇  {0}{1}, you are the winner!{2}🥇".format(bold,player2,reset))
  print("↪ {0}{1}THE SCORES{2}↩".format(bold,underline,reset))
  print("{0}-{1}\n{2}-{3}".format(player1,score1,player2,score2))
  #Opens 'leaderboard.txt' in append mode.
  file2 = open("leaderboard.txt","a")
  #Adds the player-1 details (name and score) to the file.
  file2.write(player2 + ',' + str(score2) + '\n')
  #Closes the file.
  file2.close()
#An empty list is created to be later appended into.
leaderboardList = []
#Opens 'leaderboard.txt' in read mode.
leaderboardFile = open("leaderboard.txt","r")
for line in leaderboardFile:
  #Separates the values in the file with commas.
	values = line.split(',')
  #The player usernames in the file (at positon 0) are stored in the variable 'names'.
	names = values[0]
  #The player scores in the file (at positon 1) are stored in the variable 'scores'.
	scores = values[1]
  #The usernames and scores are put within 'list1' in that order.
	list1 = [names, scores]
  #'list1' is then added to 'leaderboardList'.
	leaderboardList.append(list1)
#The file is then closed.
leaderboardFile.close()
#Sorts the list in descending order.
sortedList = sorted(leaderboardList, key = lambda x:x[1], reverse = True)
print("\n\n")
#Outputs the leaderboard.
print("🏆 {0}{1}{2}LEADERBOARD{3}🏆".format(bold,underline,yellow,reset))
print('\n')
#Stores the top 5 scores in the sorted list in the variable 'highscores'.
highscores = sortedList[0:5]
#Outputs the top 5 scores under the headings 'PLAYER' and 'SCORE'.
print("%-20s%17s"%("\033[40;93mPLAYER","SCORE\033[0m"))
for each in highscores:
  print("%-20s%-20s"%(each[0],each[1]))