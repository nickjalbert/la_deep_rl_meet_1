from environment import CorridorEnv


class RandomAgent:
    def choose_action(self, state):
        # =========
        # TODO - Implement an agent that randomly moves in the environment
        #        until it successfully passes through the corridor
        # =========
        return 1


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
