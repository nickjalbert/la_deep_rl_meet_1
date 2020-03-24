# Env that models a 1D corridor (you can move left or right)
# Goal is to get to the end (i.e. move right [length] number of times)
# Inspired by Ray's RLlib example environment: https://github.com/ray-project/ray/blob/master/rllib/examples/custom_env.py
# See also Sutton and Barto (e.g. example 13.1 on page 323).
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
        #   * each step should award the agent -1 until goal is reached
        #   * Returns a 4-tuple: (new state, reward, done, info)
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


# Unit tests for CorridorEnv
def run_tests():
    print("Testing CorridorEnv...")
    env = CorridorEnv({"length": 5})
    assert env.reset() == 0, "Initial position is 0"
    # Left step in initial position hits a wall and does not change state
    state, reward, done, info = env.step(0)
    assert state == 0
    assert reward == -1
    assert done is False
    # Right step should move agent closer to goal
    state, reward, done, info = env.step(1)
    assert state == 1
    assert reward == -1
    assert done is False
    # Left step returns agent to initial position
    state, reward, done, info = env.step(0)
    assert state == 0
    assert reward == -1
    assert done is False
    # Step to end of corridor
    state, reward, done, info = env.step(1)
    assert state == 1
    assert done is False
    state, reward, done, info = env.step(1)
    assert state == 2
    assert done is False
    state, reward, done, info = env.step(1)
    assert state == 3
    assert done is False
    state, reward, done, info = env.step(1)
    assert state == 4
    assert done is False
    state, reward, done, info = env.step(1)
    assert state == 5
    assert done is True
    print("Tests passed!")


if __name__ == "__main__":
    run_tests()
