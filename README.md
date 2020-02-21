# Connect Four AIs
This is the second project in a series of projects to learn how to optimize game AIs. Take a look at  [Tic Tac Toe](https://github.com/eyusti/tic_tac_toe) to check out the first project and get more background.

I've chosen Connect Four as a follow-up to Tic Tac Toe because its large state space adds the challenging dimension of not being able to search all possible results when making a move. Much like Tic Tac Toe, Connect Four is solved. The solution, however, is different - the first player should always win given perfect play from both players and if they play in the center as their first move.

## Connect Four AI Variations

### Min Max AI
The first AI I built applies the same min-max algorithm from Tic Tac Toe. However, since the state space is too large to play out every possible game from a position before making a move, a heuristic is used to score a game state at a specified depth. 

The heuristic I settled on checks for permutations of 1-4 player tokens and 3-0 playable spaces respectively for both players. So, it would look for formations like`["1", "1", "1", "1"], ["1", "1", "?" ,"1"], ["1", "?", "1", "?"], ["1", "?", "?", "?"]` for both players. It then assigns a value to the permutation: 5 for 4 player tokens, 3 for 3 player tokens and a playable space, 2 for 2 player tokens and 2 playable spaces, and 1 for 1 player tokens and 3 playable spaces. These value then have a discount applied based on when you actualize that value. So, if all turns appear to lead to losses, it would prefer the loss that is the furthest turn from now. Likewise, it prefers to win as soon as possible. It then scores a move based on the total value of your permutations minus the value of your opponenets total. 

This heuristic always beats RNG as player one at a depth of 1. 

> The code allows you to adjust depth searched and the future discounting of permutations as well as some permutations of the heuristic I eventually settled on if you want to experiment.

> Known Issue: This implementations has an issue where scoring counts permutations multiple times that should really only be scored as one opportunity such as `?xx?xx?`

### Monte Carlo Game Tree Search(MCGTS)
The second AI I built uses purely a Monte Carlo Game Tree search to find the best next move. I used this [tutorial](https://int8.io/monte-carlo-tree-search-beginners-guide/) and highly recommend it. There were a few things that were non-obvious to me around how to apply this tutorial specifically around Connect Four:

1. Don't score losses as negative. My mind defaulted to this scoring system since I build this directly after minmax which scores wins as 1, ties as 0 and losses as -1. I currently score wins as 1, ties as .1 and losses as 0.

2. I've seen some conflicting information about what constant to use in UCB with the general advice being to use whatever works for the problem you are working on. I've found the sqrt(2) worked well for Connect Four.

3. You have to consider the UCB relative to the player that took a turn that round when applying MCGTS to a competative game. There are a lot of tutorials that discuss MCGTS in the abstract and don't touch on this piece as a critical part of implementation.

