import random
from environment import CorridorEnv


class RandomAgent:
    def choose_action(self, state):
        return random.choice((0, 1))


if __name__ == "__main__":
    agent = RandomAgent()
    environment = CorridorEnv()
    state = environment.reset()
    done = False
    step_count = 0
    cumulative_reward = 0
    while not done:
        action = agent.choose_action(state)
        state, reward, done, info = environment.step(action)
        step_count += 1
        cumulative_reward += reward
    print(f"Total steps: {step_count}")
    print(f"Cumulative reward: {cumulative_reward}")
