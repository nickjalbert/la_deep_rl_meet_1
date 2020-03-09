from environment import CorridorEnv

class MonteCarloAgent:
    def __init__(self, epsilon=0.1):
        self.state_rewards = {}
        self.epsilon = epsilon
        self.q = {}
        self.returns = {}

    def train(self, env, num_rollouts=1000):
        # =========
        # TODO - Implement a training function that runs some rollouts and,
        #        for each state encountered, memorizes the future return
        #        of the rollout.
        # =========
        for rollout_num in num_rollouts:
            state = environment.reset()
            done = False
            states, actions, rewards = [], [], []
            while not done:
                states.append(state)

                action = agent.choose_action(state)
                actions.append(action)

                state, reward, done, info =  environment.step(action)
                rewards.append(reward)

            print(f"updating q for rollout {rollout_num} with {len(rollout_rewards)} steps")
            # work backwards through rewards in this rollout, updating Q at each step.
            for i in range(len(rollout_rewards), 0, -1):
                print(i)
            
    def choose_action(self, state):
        # =========
        # TODO - Implement an epsilong-greedy policy function from state to next agent action
        # =========

        rewards = state_rewards.get(state, [])
        
        return 1


if __name__ == '__main__':
    agent = MonteCarloAgent()
    environment = CorridorEnv()

    # Train agent
    agent.train(environment, num_rollouts=1)

    # Test our agent
    state = environment.reset()
    done = False
    step_count = 0
    cumulative_reward = 0
    while not done:
        action = agent.choose_action(state)
        state, reward, done, info =  environment.step(action)
        step_count += 1
        cumulative_reward += reward
    print(f'Total steps: {step_count}')
    print(f'Cumulative reward: {cumulative_reward}')
