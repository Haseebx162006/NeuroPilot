from gymnasium.envs.registration import register

register(
    id="Racing-v0",
    entry_point="env.racing_env:RacingEnv",
    max_episode_steps=2000,
)
