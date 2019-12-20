# snake_game
An implementation of the classic Snake game, using Python with the Pygame library.

# Summary
The game is just like that of the classic - simple and sweet. The player controls a snake using the arrow keys, and they can only move forward, and cannot reverse directions. The goal is to eat as many of the apples, small blocks that appear at random locations on the screen, as possible. Each bite will increase the snakes length, which increases the liklihood of the game over condition; if the player collides with their own body, they lose, and the game can thus be restarted. The player cannot exit the borders, and the snake will move counter-clockwise among them. The player may exit at any time.

# Known Issues
Code needs a bit of refactoring. There's a lot of magic numbers and unused variables, and the display is done entirely in the __init__ method, which is non-ideal. Also, adjust text to fit to display window, rather than hard numbers.

- To fix this, obviously, refactor.

# Future Additions
- Aesthetic improvements.

I hope you enjoy this fun game as much as I do!
