from collections import defaultdict
import numpy as np
import random
from environment import CorridorEnv

class MonteCarloAgent:
    def __init__(self, env, epsilon=0.9):
        self.env = env
        self.epsilon = epsilon
        self.q = {}  # key is (state,action) tuple
        self.returns = defaultdict(list) # key is (state, action) tuple
        self.reward_discount = 0.9

    def train(self, num_rollouts=1000):
        print("Length of training rollouts:")
        for rollout_num in range(num_rollouts):
            state = self.env.reset()
            i, done = 0, False
            states, actions, rewards = [], [], []
            while not done:
                states.append(state)

                action = agent.choose_action(state, self.epsilon/(rollout_num + 1))
                actions.append(action)

                state, reward, done, info =  self.env.step(action)
                rewards.append(reward)
                i += 1

            print(len(rewards), end=", ")
            # work backwards through rewards in this rollout, for each step:
            #   - calculate return observed for (s,a), and append it to self.returns((s,a))
            #   - update Q
            returns_per_step = list(rewards)
            for i in range(len(rewards) - 2, -1, -1):
                s, a, r = states[i], actions[i], rewards[i]
                returns_per_step[i] = r + self.reward_discount * returns_per_step[i + 1]
                self.returns[(s, a)].append(returns_per_step[i])
                self.q[(s,a)] = np.mean(self.returns[(s,a)])
            
    def choose_action(self, state, prob_random):
        if random.random() < prob_random:
            return self.env.action_space.sample()
        else:
            rewards = [self.q.get((state, a), 0) for a in range(self.env.action_space.n)]
            return np.argmax(rewards)


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
