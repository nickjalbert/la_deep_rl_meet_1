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
        # =========
        # TODO - Implement a 1D corridor environment:
        #   * self.position is the agent's current position in the env
        #   * agent starts in self.position 0 (far left)
        #   * agent must walk right to the end of the corridor (self.length)
        #   * action is either a 0 (move left) or 1 (move right)
        #   * the agent hits wall if it walks left at self.position == 0
        #   * the agent succeeds when self.position == self.length
        #   * reward scheme motivates the agent to traverse the corridor
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
