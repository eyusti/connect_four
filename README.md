# Connect Four AIs
This is the second project in a series of projects to learn how to optimize game AIs. Take a look at  [Tic Tac Toe](https://github.com/eyusti/tic_tac_toe) to check out the first project and get more background.

I've chosen Connect Four as a follow-up to Tic Tac Toe because its large state space (4,531,985,219,092) adds the challenging dimension of not being able to search all possible results when making a move. Much like Tic Tac Toe, Connect Four is solved. The solution, however, is different - the first player should always win given perfect play from both players and if they play in the center as their first move.

## First, a baseline
I wanted to see how Connect Four would behave with two players moving at random. Similarly to Tic Tac Toe, you see that the first person has an advantage. Also interestingly, it seems that draws happen fewer times at random. 

```
AI      Turn order    Games won      %
----  ------------  -----------  -----
rng              1          548  0.548
rng              2          449  0.449
tie                           3  0.003
```

## Min Max AIs
The first AIs I built applied the same min-max algorithm from Tic Tac Toe. However, since you can't play out every possible game, rather than the outcome of a game branch, this implementation generates a score at a given depth based on a heuristic. There were a few parameters I played with for these AIs: heuristic, depth, and future reward discounting. 

### Heuristics
The first heuristic I created checks for permutations of three of a kind and a playable space. In other words, count how many `["1", "1", "?" ,"1"] , ["1", "1", "1", "?"]` etc. exist for the current ai and opposing ai and use the difference as the score. I'll refer to this as the three-check heuristic.

There are a few immediatly known problems with this, the first is that the first few moves of the game will be made not taking into account any new board information since, at most depths early game, you're not going to have many of these positions available to score. Given the current implementation, the AI will keep playing in the left most column until it has any score information to use. The second problem is that we know that the far left column is not the best first move. In fact, the second player is able to force a win from this position.

The second heuristic I created additionally checks for permutations of two of a kind and two playable spaces. This theoretically gets you more information in early play and it also helps prevent situations where the opponenet can set up some double win conditions. I'll refer to this one as the two-check. This second heuristic does share the same problem with three-check of not going in the center first. 

In an attempt to improve upon this performance, I layered weighting and a first move preference on top of the two check AI. I decided to weigh 3 move permutations above 2 move permutations. The logic behind this being that if a three move permutation exists it is much more important to block or attempt to win rather than set up or defeat a potential setup.  I've made 3 move permutations 3x more important. This is a pretty arbitrary starting point and can be tested to optimal performance. Finally, I made it so that this AI will always go in the middle slot if it is available. 

> Known Issue: All of these implementations have an issue where the scoring double counts some win permutations twice that really should only be scored as one opportunity such as `?xx?xx?`

### Depth

Depth refers to how many turns ahead the AI is looking for any particular move. For the purposes of run time, it is ideal to have a shallower depth. However, deeper depths lead to more informed moves.

The interplay between depth and heuristic is interesting. A heuristic may perform worse against another AI at the same depth but ourperform it by searching deeper. 

### Future reward discounting
Future reward discounting allows you to preference scores based on turn order. For instance, if you could lose either this turn or a couple turns from now, I'd like to loose a few turns from now. The inverse holds for a series of wins. I'd rather win sooner than a few turns from now.

This doesn't matter if the two players playing the game are actually playing perfectly. But, this has interesting implications for me since a poorly programmed AI has the ability to missplay such as the RNG AI or poorly built AI. 

## Monte Carlo Game Tree Search
This algorithm builds the game tree for the current state of Connect Four and explores 