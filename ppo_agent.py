import ray
from ray.rllib.agents import ppo
from ray.tune.logger import pretty_print

from environment import CorridorEnv

# Runs PPO (via Ray) to solve the CorridorEnv
class PPOAgent:
    def train(self, environment, env_config):
        ray.init()
        trainer = ppo.PPOTrainer(
            env=environment, config={"env_config": env_config},
        )
        while True:
            results = trainer.train()
            episodes = results.get("episodes_total")
            print(f"\nEpisodes: {episodes}")
            print(f'Reward mean: {results.get("episode_reward_mean")}\n')
            if episodes >= 1000:
                break
        print("\n\n============")
        print(pretty_print(results))


if __name__ == "__main__":
    print("\nTraining PPO Agent (this will take ~1min)...\n")
    agent = PPOAgent()
    agent.train(CorridorEnv, {})
