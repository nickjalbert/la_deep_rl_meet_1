# Env that models a 1D corridor (you can move left or right)
# Goal is to get to the end (i.e. move right [length] number of times)
import gym


class CorridorEnv(gym.Env):
    metadata = {"render.modes": ["human"]}

    # Check [env_config] for corridor length, default to 10
    def __init__(self, env_config=None):
        self.env_config = env_config if env_config else {}
        self.length = int(self.env_config.get("length", 10))
        self.action_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.Discrete(self.length + 1)
        self.reset()

    def step(self, action):
        # If done, we stand still
        if self.done:
            return (self.position, 0, self.done, {})
        # Walk left if we are not at the far left of the corridor
        if action == 0 and self.position > 0:
            self.position -= 1
        # Walk right if we are not at the far right of the corridor
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
