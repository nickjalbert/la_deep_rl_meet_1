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
        if self.done:
            return (self.position, 0, self.done, {})
        if action == 0 and self.position > 0:
            self.position -= 1
        if action == 1 and self.position < self.length:
            self.position += 1
        return (self.position, -1, self.done, {})

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
