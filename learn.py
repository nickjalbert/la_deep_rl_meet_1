from environment import CorridorEnv
from agent import RandomAgent, PPOAgent


env_config = {'length': 10}

# Run random agent
random_agent = RandomAgent()
print('Running random agent')
random_agent.run(CorridorEnv, env_config)


# Run PPO agent
ppo_agent = PPOAgent()
print('Running PPO agent')
ppo_agent.run(CorridorEnv, env_config)



