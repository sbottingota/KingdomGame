# Kingdom Game
A simple game I created using python.

## How to play
Run `main.py` in the command line.
You will need `matplotlib` installed.
This game uses a `matplotlib` window,
but all user interactions will be in the command line.

## Rules
### Overview
In this game, there can be 2-4 players.
Each player owns a "kingdom".
Each turn, you are approached by a person or group of people,
and they give you a request.
Your answer alters how well your kingdom is doing.
The aim of the game is to be the last kingdom standing.

### Stats
Stats represent how well your kingdom is doing.
Each player has 4 stats: Money, Resources, Population and Happiness.
Each stat starts at 50, and you can have up to 100 of each stat.
When you answer a request, your answer alters these stats.
If any of your stats reaches 0, you are out of the game.
(Having 100 of a stat doesn't do anything, it's just a cap.)

### Other
- You can take stats away from other players.
- For some questions, there is a random chance for outcomes.
- Stats will be shown in a seperate window.

This game was created just for fun and to learn more about python.
