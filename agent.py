import ray
from ray.rllib.agents import ppo
from ray.tune.logger import pretty_print


class RandomAgent:
    def run(self, environment, env_config):
        # =========
        # TODO - Implement an agent that randomly moves in the environment
        #        until it successfully passes through the corridor
        # =========
        pass



# Runs PPO (via Ray) to solve the CorridorEnv
class PPOAgent:
    def run(self, environment, env_config):
        ray.init()
        trainer = ppo.PPOTrainer(
            env=environment, config={"env_config": env_config},
        )
        while True:
            results = trainer.train()
            print("\n\n============")
            print(pretty_print(results))
            episodes = results.get("episodes_total")
            if episodes >= 1000:
                break

 
 

