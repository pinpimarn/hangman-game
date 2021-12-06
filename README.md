# ✧･ﾟ:* ✧･ﾟ:HANGMAN GAME Project :･ﾟ✧*:･ﾟ✧

This project is the final project for 01219114/01219115 Programming 1.
In this project, I have met all the requirements from teacher which are
1. Display results on Python Turtle Graphics window; direct use of tkinter
   window is not allowed
2. Interact with user on the console, i.e., ask input and show output 
3. Implement at least 3 classes, one of which contains a list or dict 
   of objects from another class as an attribute
4. Read/write data from/to text files

## ♡ Overview and features

This project is a Hangman game that we usually play when we were young
but the game will be shown and play in the computer, not on the
blackboard.

### ☀ How to play?
At the start of the game, you will go to the main menu page to 
choose whether you want to start the game or want to exit the game. 
* If you want to start the game, you must press `1` + `enter`.
* If you want to exit the game you can press `2` + `enter`.

Then a window will appear for selecting the difficulty level of the game.
The levels of the game are divided according to the difficulty of the words.
You can choose to play according to your aptitude. There are three levels 
in this game:

* **Basic level [1]** : contains vocabulary words for elementary students.
* **Intermediate level [2]** : contains vocabulary words for middle and high school
  students.
* **Expert level [3]** : contains vocabulary words for university students.

You can select one of these three levels by pressing `number` + `enter`.



## ♡ Modules

My game consists of five modules as the following...

### ☀ 1. Module `vocab.py`

This module contains the `Vocabulary` class. There are 4 methods in this class 
which are:
* readfile() → open the .txt file and return a list of vocabulary words. 
* choose_word() → random words from the read file 
* index_clue() → change the full word to a clue for the user with some alphabets clue.

### ☀ 2. Module `vocabContainer.py`

This module contains the `VocabContainer` class for collecting
the number of vocabulary words you want to play. There are 4 methods
in this class which are:
* add() → collect n vocabulary word(s) as a user wants.

### ☀ 3. Module `outplay.py`
This module contains the `Outplay` class for setting the game on the screen
that is not included in the game processing. There are 4 methods in this class
which are:
* rec() → 
* choose_start() → use the Python Turtle Graphics window to interact with the user by asking whether the user 
  wants to start or exit the game.
* choose_level() → use the Python Turtle Graphics window to interact with the user by asking whether the user
  wants to play which level (from 3 levels) in this game.
* times_input() → use the Python Turtle Graphics window to interact with the user by asking how many times
  the user wants to play this game (in one round).
* board() → use the Python Turtle to draw the board background for wrong alphabet input.
* lose() → use the Python Turtle to draw the board background for wrong alphabet input.
* win() →
* summarize() → use the Python Turtle Graphics window to interact with the user by letting the user guess an alphabet for the shown word.

### ☀ 4. Module `play.py`
This module provides the `Play` class for creating a `Stage` object that
incorporates a `Border` object and a list of `Ball` objects.  It is also
responsible for creating a graphical screen and a turtle-based painter object
to be used by the `Border` and `Ball` objects to draw themselves on the
screen.

This module is already completely implemented.  You don't have to add
anything.

### ☀ 5. Module `main.py`
This module implements the game that let the users play.


## Graphical Output

The graphical output elements is taken care of by the `stage.py` module.
However, you are required to implement the `draw` method in your `ball.py` and
`border.py`.  The `draw` method takes one `painter` argument which is a
`Turtle` object.  Consult [this
document](https://docs.python.org/3/library/turtle.html#turtle-methods) for
the list of turtle's drawing commands.

There is no definite rule on how you should draw your objects.  However, at
least the following is required:

* A `Ball` object must show with its current `color` property.
* A `Ball` object must show its movement trail, which keep track of the past
  10 positions of the ball.
* A `Border` object must clearly display its boundary.


## Your Task

1. Complete the implementations of the `vector.py`, `border.py`, and `ball.py`
   modules.  Make sure they all pass the tests.
2. Implement the `draw` methods in `ball.py` and `border.py`, then run
   `app.py` to see the graphical result and visually inspect the
   correctness.
3. Modify the `summary.txt` file.  In this summary, tell us what you have
   completed and what you have not.

**Notes:** Please do not change any file inside the `docs` directory.  These
files will be used to run tests against your submitted code.
