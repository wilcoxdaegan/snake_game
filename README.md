# snake_game
An implementation of the classic Snake game, using Python with the Pygame library.

# Summary
The game is just like that of the classic - simple and sweet. The player controls a snake using the arrow keys, and they can only move forward, and cannot reverse directions. The goal is to eat as many of the apples, small blocks that appear at random locations on the screen, as possible. Each bite will increase the snakes length, which increases the liklihood of the game over condition; if the player collides with their own body, they lose, and the game can thus be restarted. The player cannot exit the borders, and the snake will move counter-clockwise among them. The player may exit at any time.

# Known Issues
When the apple spawns, it doesn't check the location of the snake at all. While rare at small snake lengths, it's possible for it to spawn where the snake is. With the way the snake is rendered, this will cause the apple to become invisible, not even counting for the obvious problems with having the apple spawn in the snake. At large lengths, it may take 20 seconds to even appear, but again, it will become invisible. 

- To fix this, upon the apple deciding a location, it should check if the snake exists at that location.

When on the border, the player can still manually go outside it. They will eventually be automatically be brought back, but it means they can leave for a short time, which is unintended.

- To fix this, when the player is on a border, one solution may to be not to take any keyboard input that could lead them astray.

Code needs a bit of refactoring. There's a lot of magic numbers and unused variables, and the display is done entirely in the __init__ method, which is non-ideal.

- To fix this, obviously, refactor.

# Future Additions
- Score counter.
- Command line args to decide initial snake length, and perhaps size, or even apple size increase.
- Aesthetic improvements.

I hope you enjoy this fun game as much as I do!
