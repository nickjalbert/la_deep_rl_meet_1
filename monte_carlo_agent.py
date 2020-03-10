from collections import defaultdict
import numpy as np
import random
from solutions.environment import CorridorEnv

class MonteCarloAgent:
    def __init__(self, env, epsilon=0.9):
        self.env = env
        self.epsilon = epsilon
        self.reward_discount = 0.9
        self.q = {}  # key is (state,action) tuple
        self.returns = defaultdict(list) # key is (state, action) tuple

    def train(self, num_rollouts=1000):
        # =========
        # TODO - Implement a training function that runs some rollouts and,
        #        for each state encountered, memorizes the future return of the
        #        rollout. Use the self.returns and self.q to do the memorizing.
        # =========
            
    def choose_action(self, state, prob_random):
        # =========
        # TODO - Implement an epsilon-greedy policy function from state to next agent action
        # =========


if __name__ == '__main__':
    environment = CorridorEnv({"length": 10})
    agent = MonteCarloAgent(environment)

    # Train agent
    print("== training MC agent ==")
    agent.train(num_rollouts=100)

    # Test our agent
    print("\n== testing agent ==")
    state = environment.reset()
    done = False
    step_count = 0
    cumulative_reward = 0
    while not done:
        action = agent.choose_action(state, 0)
        state, reward, done, info =  environment.step(action)
        step_count += 1
        cumulative_reward += reward
    print(f'Total steps: {step_count}')
    print(f'Cumulative reward: {cumulative_reward}')
