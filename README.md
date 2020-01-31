# Connect Four AIs
This is the second project in a series of projects to learn how to optimize game AIs. Click [here](https://github.com/eyusti/tic_tac_toe) to check out that project and get more background.

I've chosen Connect Four as a follow-up to Tic Tac Toe because of its large state space (4,531,985,219,092). Because of the large state space, searching the entire tree to solve the game is infeasible. Like Tic Tac Toe, Connect Four is solved such that the first player should always win given perfect play from both players. The correct first move for perfect play to force this move is the center.

## First, a baseline
To get us started with the appraisal of AI solutions, let's take a look at two RNG AIs playing against one another.
```
AI      Turn order    Games won      %
----  ------------  -----------  -----
rng              1          548  0.548
rng              2          449  0.449
tie                           3  0.003
```
Much like Tic Tac Toe, Connect Four also has a bit of a first person advantage. However, the likelyhood of a tie occuring naturally appears to be very slim.

## Min Max Optimizations
The first tact I took towards building an AI was to apply the same min-max algorithm from Tic Tac Toe. However, this implementation will score a game with an unknown outcome at a specified depth by applying a heuristic. Therefore, this algorithm can be optimized across two parameters: heuristic used and depth searched.

The first heuristic I used was to check for permutations of three of a kind and a playable space. In other words, count how many `["1", "1", "?" ,"1"] , ["1", "1", "1", "?"]` etc. exist for the current ai and opposing ai and use the difference as the score.

There are a few immediatly known problems with this, the first is that for the first few moves of the game, there will be no boards in this state at depths that are easy to quickly calculate. Given the current implementation, this means that the algorithim will keep playing in the right most column until it has any information to work with. The second problem is that we know that the far right column is not the best first move. In fact, it seems that a force with from the second player is possible from that first move state.

Despite this, it performs surprisingly ok against RNG and determinalistically against itself.
INSERT RNG/MINMAX MINMAX/RNG MINMAX/MINMAX

In the case of RNG, it essentially is setting a timer for random generation to create a four in a row in four moves as long as the column build up in the right isn't interrupted. This is surprisingly effective against RNG. It also appears to do the right column build-up behavior for all depths up to 5. This will clearly fail with anything a little bit more clever like our next contender.

This heuristic checks for permutations of two of a kind and two playable spaces. The goal of this was to get more information beginning at a shallower depth.
INSERT RNG/MINMAX MINMAX/RNG RNG/MINMAX2 MINMAX2/RNG 

