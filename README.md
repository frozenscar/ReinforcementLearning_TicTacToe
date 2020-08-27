# ReinforcementLearning_TicTacToe
Reinforcement learning agent trained to play tic tac toe.

class TicTacToe has game logic with option to play agent against agent or agent agaisnt human.

Agents use epsilon-Greedy policy.
We update the action-values for the states visited during the episode(1 run of the game).(Monte Carlo method)

We update q(action,value) in updateActionValues method in Agent class.
  After the episode ends we get a reward of 1 if for winning, -1 for losing and 0 for tie,
  updateActionValues method is called after end of an episode.What it does is,

  let nm = total number of times (state,action) is visited over all the episodes.
  discount = (0.9**(lenOfEpisode-currentStep))
  
  q(state,action) = q(state,action)+ (1/(nm))*(discount*G - q(state,action))



The agent will only store q(state,action) only if they're visited at least once.


