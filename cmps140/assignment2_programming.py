# -*- coding: utf-8 -*-
"""Assignment2_programming.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qBRkJGyRhMA9uw2m6RITwSeGfvdDlLQP

# CMPS 140 Assignment 2

**Due Feb 11, 2019 11:59**

Solve the following MDP using both value iteration and policy iteration programmatically.

There is a self-driving taxi that takes from place to place. Its goal is to make the most money possible and it makes the most money in a particular town, MoneyTown. The taxi has a tendency to take routes that take it to different towns and it costs money for the taxi to drive from place to place.  

There are three states that the taxi can be in: 'In MoneyTown', 'MoneyTown Suburbs', and 'Outside MoneyTown'. There are two actions that the taxi can take in each state: drive and wait. Driving costs \\$10. When the taxi is in money town it makes \$30, in MoneyTown Suburbs and Outside MoneyTown it only makes $10. The reward for the taxi is:

(money made - cost) 

For example if the taxi is driving around in MoneyTown, the reward is \$30 - \$10 = \$20.

If the taxi is in MoneyTown and drives, then it is still MoneyTown in the next period with probability .9, and in the MoneyTown Suburbs in the next period with probability .1. If it is MoneyTown and does not drive, these probabilities are .7 (in the MoneyTown) and .3 (in the MoneyTown Suburbs), respectively. If it is in the MoneyTown Suburbs and drives, then with probability .3 it is in MoneyTown in the next period, with probability .6 it is still in MoneyTown Suburbs in the next period, and with probability .1 it is in Outside MoneyTown in the next period. If it is in MoneyTown Suburbs and does not drive, then with probability 1 it is Outside MoneyTown next period. Finally, if it is in Outside MoneyTown and drives, then in the next period it is in MoneyTown with probability .6, and at the OutSide MoneyTown with probability .4. If it does not drive, then with probability 1 it is at Outside MoneyTown in the next period. 

1. Draw the MDP graphically
  - A good way to do this is through [Google Drawings](https://docs.google.com/drawings)
  - When you're done you can embed it in the jupyter notebook using markdown syntax
  - \!\[alt-text\]\(url\)
  - To get the URL for your image in Google Draw goto File->Publish to the web...->Embed and copy the src portion of the html tag
  
2. Using a discount factor of .8, solve the MDP using value iteration (until the values have become reasonably stable). You should start with the values set to zero. You should show both the optimal policy and the optimal values.
3. Using a discount factor of .8, solve the MDP using policy iteration (until you have complete convergence). You should start with the policy that never drives. Again, you should show both the optimal policy and the optimal values (and of course they should be the same as in 2...).
4. Change the MDP in three different ways: by changing the discount factor, changing the transition probabilities for a single action from a single state, and by changing a reward for a single action at a single state. Each of these changes should be performed separately starting at the original MDP, resulting in three new MDPs (which you do not have to draw), each of which is different from the original MDP in a single way. In each case, the change should be so that the optimal policy changes, and you should state what the optimal policy becomes and give a short intuitive argument for this.

[PLESE PUT YOUR HTML TAG FOR MDP GRAPH HERE]

![alt-text](url)
"""

# Initialization

import collections

states=["M", "S", "O"]
actions=["drive", "stop"]

Transition_table = collections.defaultdict(lambda: collections.defaultdict(dict))
Transition_table["M"]["drive"]["M"] = 0.9
Transition_table["M"]["drive"]["S"] = 0.1
Transition_table["M"]["drive"]["O"] = 0
Transition_table["M"]["stop"]["M"] = 0.7
Transition_table["M"]["stop"]["S"] = 0.3
Transition_table["M"]["stop"]["O"] = 0

Transition_table["S"]["drive"]["M"] = 0.3
Transition_table["S"]["drive"]["S"] = 0.6
Transition_table["S"]["drive"]["O"] = 0.1
Transition_table["S"]["stop"]["M"] = 0
Transition_table["S"]["stop"]["S"] = 0
Transition_table["S"]["stop"]["O"] = 1


Transition_table["O"]["drive"]["M"] = 0.6
Transition_table["O"]["drive"]["S"] = 0
Transition_table["O"]["drive"]["O"] = 0.4
Transition_table["O"]["stop"]["M"] = 0
Transition_table["O"]["stop"]["S"] = 0
Transition_table["O"]["stop"]["O"] = 1

print(Transition_table)

Reward_table = collections.defaultdict(lambda: collections.defaultdict(dict))
Reward_table["M"]["drive"]["M"] = -10 + 30
Reward_table["M"]["drive"]["S"] = -10 + 10
Reward_table["M"]["drive"]["O"] = -10 + 10
Reward_table["M"]["stop"]["M"] = 30
Reward_table["M"]["stop"]["S"] = 10
Reward_table["M"]["stop"]["O"] = 10

Reward_table["S"]["drive"]["M"] = -10 + 30
Reward_table["S"]["drive"]["S"] = -10 + 10
Reward_table["S"]["drive"]["O"] = -10 + 10
Reward_table["S"]["stop"]["M"] = 30
Reward_table["S"]["stop"]["S"] = 10
Reward_table["S"]["stop"]["O"] = 10

Reward_table["O"]["drive"]["M"] = -10 + 30
Reward_table["O"]["drive"]["S"] = -10 + 10
Reward_table["O"]["drive"]["O"] = -10 + 10
Reward_table["O"]["stop"]["M"] = 30
Reward_table["O"]["stop"]["S"] = 10
Reward_table["O"]["stop"]["O"] = 10

print(Reward_table)

"""** Please put your code below to solve the problem programmatically, You can add cells as you feel the need.**"""

# Implementation

import numpy as np
import math

def value_iteration(discount, states,  actions, Transition_table, Reward_table, max_iteration=10000):
  
  # You might use a two dimensional array for Q table instead of dictionary.
  #Q_table = np.zeros((len(states), len(actions)), dtype='int32')
  # Use a dictionary to define Q_table, then you may have something like, Q_table["M"]["drive"] = 0.0
  Q_table = collections.defaultdict(lambda: collections.defaultdict(float))
  # Example value in P_star: P_star["M"] = "drive"
  P_star = {}
  # # Initialize V* with zeros
  V_star = {}
  V_star["M"] = 0
  V_star["S"] = 0
  V_star["O"] = 0
  
  # TODO: Implement your code here. Do the iteration until the value is stable or it exceeds max_iteration.
  return P_star, V_star






def policy_iteration(discount, states,  actions, Transition_table, Reward_table):
  
  # You might use a dictionary structure for Q table instead of arrays.
  Q_table = np.zeros((len(states), len(actions)), dtype='float32')
  # Example value in P_star: P_star["M"] = "drive"
  P_star = {}
  # Example value in V_star: V_star["M"] = 18
  V_star = {}
  

  
  #We start with a policy of always stop, as per instructions 
  P_star['M']="stop"
  P_star['S']="stop"
  P_star['O']="stop"
  
  flag = True
  firstPass= True 
  breaker = 0 
  while flag: 
    new_P_star = P_star.copy() 
    Q=policy_evaluation(discount,states,actions,Transition_table,Reward_table, P_star, Q_table)
    #print(Q) 
    i=0 
    for s in states: 
      j=0  
      maxVal = 0 
      for a in actions: 
        currentVal=0 
        if(Transition_table[s][a].get('M')!=None): 
          currentVal=currentVal+Transition_table[s][a].get('M')*max(Q_table[0][0],Q_table[0][1])
        if(Transition_table[s][a].get('S')!=None): 
          currentVal=currentVal+Transition_table[s][a].get('S')*max(Q_table[1][0],Q_table[1][0])
        if(Transition_table[s][a].get('O')!=None): 
          currentVal=currentVal+Transition_table[s][a].get('O')*max(Q_table[2][0],Q_table[2][1])
        currentVal=Reward_table[s][a]+discount*currentVal 
        if(currentVal>maxVal): 
          maxVal=currentVal
          P_star[s]=a 
        #print("Current value is: "+str(currentVal)+", and maxVal is: "+str(maxVal)) 
        j+=1 
      i+=1 
    Q_table = Q
    """flag2 = False
    for p in P_star: 
      if P_star[p]!=new_P_star[p]: 
        flag2 = True
        break 
    flag = flag2   
    if firstPass: 
      flag= True 
      firstPass = False""" 
    breaker += 1
    if breaker == 30: flag = False 
  
  # print(Q_table) 
  return P_star, V_star

def policy_evaluation(discount,states,actions,Transition_table,Reward_table, P_star, Q):
  table = np.zeros((len(states),len(actions)), dtype='float32') 
  #print("IN BEGINNING") 
  i = 0 
  Q_table=Q.copy() 
  #print(Q_table) 
  print(P_star) 
  for s in states:
    currentVal=0 
    a = P_star[s]
    j=0 
    actionIndex = 0 
    for a in actions: 
      if(Transition_table[s][a].get('M')!=None): 
        currentVal=currentVal+Transition_table[s][a].get('M')*Q_table[i][actionIndex]#max(Q_table[0][0],Q_table[0][1])
      if(Transition_table[s][a].get('S')!=None): 
        currentVal=currentVal+Transition_table[s][a].get('S')*Q_table[i][actionIndex]#max(Q_table[1][0],Q_table[1][0])
      if(Transition_table[s][a].get('O')!=None): 
        currentVal=currentVal+Transition_table[s][a].get('O')*Q_table[i][actionIndex]#max(Q_table[2][0],Q_table[2][1]) 
      # print("Reward table value is: "+str(Reward_table[s][a])+", discount*val is: "+str(discount*currentVal))
      currentVal=Reward_table[s][a]+discount*currentVal
      #print("Current value is: "+str(currentVal)+", state is: "+s+" action is: "+a) 
      #print("Current Value is :"+str(currentVal)) 
      Q_table[i][actionIndex]=currentVal  
      actionIndex+=1 
    i+=1 
  #print("AT END: ")
  print(Q_table) 
  return Q_table 










def policy_iteration(discount, states,  actions, Transition_table, Reward_table, max_iteration=10000):
  
  # You might use a two dimensional array for Q table instead of dictionary.
  #Q_table = np.zeros((len(states), len(actions)), dtype='int32')
  # Use a dictionary to define Q_table, then you may have something like, Q_table["M"]["drive"] = 0.0
  Q_table = collections.defaultdict(lambda: collections.defaultdict(float))
  # Initialize pi* with never drive
  P_star = {}
  P_star["M"] = "stop"
  P_star["S"] = "stop"
  P_star["O"] = "stop"
  # Example value in V_star: V_star["M"] = 18
  V_star = {}
  V_star["M"] = 0
  V_star["S"] = 0
  V_star["O"] = 0
  
  # TODO: Implement your code here. Do the iteration until the value is stable or it exceeds max_iteration.
  return P_star, V_star

# Testing
discount = 0.8

P_star_vi, V_star_vi = value_iteration(discount, states,  actions, Transition_table, Reward_table)
print("P_star_vi", P_star_vi)
print("V_star_vi", V_star_vi)
# TODO: add your expected correct results to expected_P_star_vi and expected_V_star_vi for test cases.
expected_P_star_vi = {'M': 'stop', 'S': 'stop', 'O': 'drive'}
expected_V_star_vi = {'M': 97.83616682805929, 'S': 79.36630594506894, 'O': 86.70788245549603}
assert(P_star_vi == expected_P_star_vi)
assert(math.fabs(V_star_vi["M"] - expected_V_star_vi["M"]) < 0.0000001) 
assert(math.fabs(V_star_vi["S"] - expected_V_star_vi["S"]) < 0.0000001) 
assert(math.fabs(V_star_vi["O"] - expected_V_star_vi["O"]) < 0.0000001) 

P_star_pi, V_star_pi = policy_iteration(discount, states,  actions, Transition_table, Reward_table)
print("P_star_pi", P_star_pi)
print("V_star_pi", V_star_pi)
# TODO: add your expected correct results to expected_P_star_pi, expected_V_star_pi for test cases.
expected_P_star_pi = {'M': 'stop', 'S': 'stop', 'O': 'drive'}
expected_V_star_pi = {'M': 97.83616682097912, 'S': 79.36630593897894, 'O': 86.70788244966155}
assert(math.fabs(V_star_pi["M"] - expected_V_star_pi["M"]) < 0.0000001) 
assert(math.fabs(V_star_pi["S"] - expected_V_star_pi["S"]) < 0.0000001) 
assert(math.fabs(V_star_pi["O"] - expected_V_star_pi["O"]) < 0.0000001)

"""[YOUR ANSWER FOR 4 HERE]

Case 1: changing the MDP by the discount factor;

Case 2: changing the MDP by the transition probabilities for a single action from a single state;

Case 3: changing the MDP by a reward for a single action at a single state.
"""