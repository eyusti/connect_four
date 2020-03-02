# Connect Four AIs
This is the second project in a series of projects to learn how to optimize game AIs. Take a look at  [Tic Tac Toe](https://github.com/eyusti/tic_tac_toe) to check out the first project and get more background.

I've chosen Connect Four as a follow-up to Tic Tac Toe because its large state space adds the challenging dimension of not being able to search all possible results when making a move. Much like Tic Tac Toe, Connect Four is solved. The solution, however, is different - the first player should always win given perfect play from both players and if they play in the center as their first move.

## Connect Four AI Variations

### Min Max AI
The first AI I built applies the same min-max algorithm from Tic Tac Toe. However, since the state space is too large to play out every possible game from a position before making a move, a heuristic is used to score a game state at a specified depth. 

The heuristic I settled on checks for permutations of 1-4 player tokens and 3-0 playable spaces respectively for both players. So, it would look for formations like`["1", "1", "1", "1"], ["1", "1", "?" ,"1"], ["1", "?", "1", "?"], ["1", "?", "?", "?"]` for both players. It then assigns a value to the permutation: 5 for 4 player tokens, 3 for 3 player tokens and a playable space, 2 for 2 player tokens and 2 playable spaces, and 1 for 1 player tokens and 3 playable spaces. These values then have a discount applied based on when you actualize that value. So, if all turns appear to lead to losses, it would prefer the loss that is the furthest turn from now. Likewise, it prefers to win as soon as possible. It then scores a move based on the total value of your permutations minus the value of your opponents total. 

This heuristic always beats RNG as player one at a depth of 1 and beats the Monte Carlo algorithm(playing 1000 rollouts) at a depth of 5.

> The code allows you to adjust depth searched and the future discounting of permutations as well as some permutations of the heuristic I eventually settled on if you want to experiment.

> Known Issue: This implementation has an issue where scoring counts permutations multiple times that should really only be scored as one opportunity such as `?xx?xx?`

### Monte Carlo Game Tree Search(MCTS)
The second AI I built uses a Monte Carlo Tree search to find the best next move. I used this [tutorial](https://int8.io/monte-carlo-tree-search-beginners-guide/) and I highly recommend it. There were a few things that were non-obvious to me around how to apply this tutorial specifically around Connect Four:

1. I've seen some conflicting information about what constant to use in UCB with the general advice being to use whatever works for the problem you are working on. I've found that 4 worked the best for Connect Four with 10,000 rollouts and 2 worked the best at 100,000. My best guess is that with fewer rollouts, your certainty around a score is lower so aggressive exploration is more frequently rewarded than with more rollouts where you are more certain and benefit from using the score information more aggressively. 

2. Most diagrams I saw of the backpropagation stage of MCTS showed how to pass back values abstractly rather than for a competitive game where different players are acting at different depths of the tree. Much like the min max algorithm, you have to consider the UCB relative to the player that took a turn that round when backpropagation scores.

3. A large part of writing a good MCTS algorithm is speed optimization. I played around with some of the constants like the exploration constant in UCB and the range of scores , but the majority of time improving game outcomes was spent optimizing code to allow for more rollouts.

