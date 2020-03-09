# LA Deep RL Meetup 1

Repo for first meetup of LA Deep RL group


## Dev Setup

Developed on OS X 10.15.3 under Python 3.7.6.
You can setup your dev environment as follows:

* Clone the repo: `git clone git@github.com:nickjalbert/la_deep_rl_meet_1.git`
* Enter directory: `cd la_deep_rl_meet_1`
* Create a virtualenv: ``virtualenv -p `which python3` la_deep_rl_meet_1``
* Activate your virtualenv: `source la_deep_rl_meet_1/bin/activate`
* Install dependencies:
    * `pip install -r requirements.txt`, or
    * `pip install gym ray ray[rllib] ray[debug] pandas requests tensorflow`

## Files

* `environment.py` - skeleton of the Corridor environment
* `solutions/environment.py` - a full implementation fo the Corridor environment
* `random_agent.py` - skeleton of a random agent
* `solutions/random_agent.py` - a full implementation of a random agent
* `ppo_agent.py` - a full implementation of an agent that uses a state of the art PPO algorithm
