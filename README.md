# Python Dice Game
Python script[^fn] for a two-player dice game. The game features colorful aesthetics, password protection, and a leaderboard to track top scores.

### Rules
This game involves two players rolling two 6-sided dice each over five rounds. The rules include: 
1. Each player's rolled dice points are added to their score.
2. If the total is even, 10 points are added; if odd, 5 points are subtracted.
3. Rolling a double grants an extra die roll, adding its points to the score.
4. Scores cannot drop below 0.
5. The highest score after five rounds wins. And they are added to the leaderboard.
6. Ties resolved by rolling a single die, with the higher roll winning.
7. Participation restricted to authorized players through a password.

Upon login you will be greeted with something simlar to the below:
```bash
To continue you must enter a password...
Enter password: diceGAM3Z

LOADING...
PLAYER-1 - Enter your name: Jack
Welcome Jack! Now who will you be facing today?
PLAYER-2 - Enter your name: Jill
Welcome Jill!

```

[^fn]: Made on python 3.8
