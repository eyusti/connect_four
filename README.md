# Connect Four AIs
This is the second project in a series of projects to learn how to optimize game AIs. Take a look at  [Tic Tac Toe](https://github.com/eyusti/tic_tac_toe) to check out the first project and get more background.

I've chosen Connect Four as a follow-up to Tic Tac Toe because of its large state space (4,531,985,219,092). Because of the large state space, searching the entire tree to solve the game is not feasible. Like Tic Tac Toe, Connect Four is solved such that the first player should always win given perfect play from both players with a known correct first move - the center.

## First, a baseline
To get us started with the appraisal of AI solutions, let's take a look at two RNG AIs playing against one another.

```
AI      Turn order    Games won      %
----  ------------  -----------  -----
rng              1          548  0.548
rng              2          449  0.449
tie                           3  0.003
```

Much like Tic Tac Toe, Connect Four also has a first person advantage. Unlike Tic Tac Toe, the likelyhood of a tie occuring naturally appears to be much smaller. This seems to make intuitive sense since optimal play from both players in Tic Tac Toe leads to a draw whereas in Connect Four it should lead to a win.

## Min Max AIs
The first tact I took towards building an AI player was to apply the same min-max algorithm from Tic Tac Toe. However, since you can't search the entire move space, this implementation generates a score for a board at a given depth based from a heuristic. This genre of AI player can be optimized across three parameters: heuristic used, depth searched, and future reward discounting. 

### Future reward discounting
I'll start with future reward discounting since it is a varaible that could affect outcome but, for our purposes, we are leaving mostly constant. Future reward discounting is the idea that outcomes with the same score aren't actually all created equal. The turn in which you recieve a certain score also holds value. For instance, let's say you are given a board where no matter what, you will eventually lose. However, you could lose either this turn or a couple turns from now. You could play at random and assume the loss or you can preference the future loss and hold out for a missplay from your opponent. The inverse holds for a series of wins. I'd rather win sooner than a few turns from now.

While this is less interesting to include if you assume perfect play from both players. This has an interesting implications on the exercise we are performing since an AI has the ability to missplay such as the RNG AI or a min-max AI at too shallow a depth with an non-optimal heuristic etc. 

### Heuristics
The first heuristic I created checks for permutations of three of a kind and a playable space. In other words, count how many `["1", "1", "?" ,"1"] , ["1", "1", "1", "?"]` etc. exist for the current ai and opposing ai and use the difference as the score. I'll refer to this as the three-check heuristic.

There are a few immediatly known problems with this, the first is that the first few moves of the game will be made not taking into account any new board information. This is because at most depths early game, you're not going to have many of these positions available to score. Given the current implementation, the AI will keep playing in the left most column until it has any score information to use. The second problem is that we know that the far left column is not the best first move. In fact, the second player is able to force a win from this position.

The second heuristic I created additionally checks for permutations of two of a kind and two playable spaces. This theoretically gets you more information in early play and it also helps prevent situations where the opponenet can set up some double win conditions. I'll refer to this one as the two-check. We do know that this second heuristic will share the same problem with three-check of not going in the center first. 

In an attempt to improve upon this performance, I layered weighting and a first move preference on top of the two check AI. I decided to weigh 3 move permutations above 2 move permutations. The logic behind this being that if a three move permutation exists it is much more important to block or attempt to win rather than set up or defeat a potential setup.  I've made 3 move permutations 3x more important. This is a pretty arbitrary starting point and can be tested to optimal performance. Finally, I made it so that this AI will always go in the middle slot if it is available. 

> Known Issue: All of these implementations have an issue where the scoring double counts some win permutations twice that really should only be scored as one opportunity such as `?xx?xx?`

### Depth

Depth refers to how many turns ahead the AI is looking for any particular move. For the purposes of run time, it is ideal to have a shallower depth. However, this is a balance since deeper depths lead to greater accuracy.

The interplay between depth and heuristic here is interesting. A heuristic may perform worse against another AI at the same depth but ourperform it by searching deeper. 

## Monte Carlo