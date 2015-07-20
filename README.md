# Alphabear Solver

A simple python script that is intended to be used to solve game boards on the mobile game 
[Alphabear](https://play.google.com/store/apps/details?id=com.spryfox.alphabear&hl=en) by Spry Fox.

The `solver.py` script uses a dictionary, located in `dictionary.txt`, which is simply an ordered list of "all" English words.
Probably need to use a better one (see todo)

## Todo

* Basic functionality ie. matching available letters to dictionary words.
* Read letters from game input.
* Weight letters so that ones with less moves remaining, worth more points etc. are preferred by the matching algorithm.
* Grab better dictionary, preferably the one used in the actual game.

## References

* Dictionary (`dictionary.txt`) is taken from here: http://www.math.sjsu.edu/~foster/dictionary.txt
* [The World's Fastest Scrabble Program](http://www.cs.cmu.edu/afs/cs/academic/class/15451-s06/www/lectures/scrabble.pdf) - 
Andrew W. Appel & Guy J. Jacobson (1988)
