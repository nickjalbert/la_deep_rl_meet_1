# Env that models a 1D corridor (you can move left or right)
# Goal is to get to the end (i.e. move right [length] number of times)
import gym


class CorridorEnv(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self, config_env=None):
        self.config_env = config_env if config_env else {}
        self.length = int(self.config_env.get("length", 10))
        self.action_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.Discrete(self.length + 1)
        self.reset()

    def step(self, action):
        # =========
        # TODO - Implement a model of a 1D corridor:
        #   * action is either a 0 (move left) or 1 (move right)
        #   * self.position is the agent's current position in the env
        #   * the agent hits a wall if it tries to walk to the left at self.position = 0
        #   * the agent succeeds when self.position == self.length
        #   * the reward scheme should motivate the agent to traverse the corridor
        # =========
        pass

    @property
    def done(self):
        return self.position >= self.length

    def reset(self):
        self.position = 0
        return self.position

    def render(self, mode="human"):
        pass

    def close(self):
        pass
