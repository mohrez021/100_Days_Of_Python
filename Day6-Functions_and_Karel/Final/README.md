# Lost in a maze
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

Reeborg was exploring a dark maze and the battery in its flashlight ran out.

Write a program using an `if/elif/else` statement so Reeborg can find the exit.

 The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

### What you need to know
1. The functions `move()` and `turn_left()`.
2. Either the test `front_is_clear()` or `wall_in_front()`, `right_is_clear()` or `wall_on_right()`, and `at_goal()`.
3. How to use a `while` loop and `if/elif/else` statements.
4. It might be useful to know how to use the negation of a test (not in Python).