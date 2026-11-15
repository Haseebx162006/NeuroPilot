import gymnasium as gym
from gymnasium import spaces 
import numpy as np
from common.domain.constants import(
    DT,
    V_MAX,
    MAX_STEER,
    HALF_TRACK_WIDTH,
    MAX_EPISODE_STEPS,
)

from common.domain.domain.PhysicalAction import PhysicalAction
from common.domain.domain.SensorReading import SensorReading


class RacingEnv(gym.Env):

    # creating a gymnasium environment for racing car simulation
    metadata = {
        "render_modes": ["human","rgb_array"],
    }

    def __init__(self,render_mode:str):
        super().__init__()
        self.render_mode=render_mode

        self.action_space = spaces.Box(
            low=-1.0,
            high=1.0,   
            shape=(3,),
            dtype=np.float32
        )

        self.observation_space = spaces.Box(
            low=-1.0,
            high=1.0,
            shape=(14,),
            dtype=np.float32
        )

        self.step_count = 0
        self.np_random=np.random.default_rng()


    def decode_action(self,action:np.ndarray)->PhysicalAction:

        # This function will recerive an neural array of shape 3
        # and decode it into a PhysicalAction object with steer, throttle, and brake values.

        steer = float(np.clip(action[0],-1.0,1.0))
        throttle = float(np.clip((action[1] + 1.0) / 2.0, 0.0, 1.0))
        brake = float(np.clip((action[2] + 1.0) / 2.0, 0.0, 1.0))

        return PhysicalAction(steer=steer,throttle=throttle,brake=brake)


    def _get_stub_sensor_reading(self) -> SensorReading:
        
        #Generates dummy sensor data matching Hamza's SensorReading schema.
        
        return SensorReading(
            speed=15.0,                        
            steer=0.0,                          
            headingError=0.0,                  
            lateralOffset=0.0,                  
            halfWidth=HALF_TRACK_WIDTH,        
            rays=np.full(7, 25.0, dtype=float),
            curvatureOfRoad=0.0,                
            opponentGapInMeter=50.0,            
            opponentClosingSpeed=0.0,           
            timeToCollide=0.0,                 
        )
    def _normalize_observation(self, s: SensorReading) -> np.ndarray:

        # Receieve Sensor Readindgs from the env and convert them to a normalized vector.
        # [0] Speed
        # [1] Steering: -0.5 to 0.5 rad -> [-1, 1]
        # [2] Heading Error: -pi to pi rad -> [-1, 1]
        # [3] Lateral Offset: -6 to 6 m -> [-1, 1]
        # [4..10] 7 LiDAR rays: 0 to 50 m -> [0, 1]
        # [11] Curvature 20m ahead: -0.1 to 0.1 rad/m -> [-1, 1]
        # [12] Opponent distance: 0 to 50 m -> [0, 1] (1.0 = none)
        # [13] Opponent closing speed: -15 to 15 m/s -> [-1, 1]

        obs = np.zeros(14, dtype=np.float32)
        obs[0] = np.clip(s.speed / V_MAX, 0.0, 1.0)
        obs[1] = np.clip(s.steer / MAX_STEER, -1.0, 1.0)
        obs[2] = np.clip(s.headingError / np.pi, -1.0, 1.0)
        obs[3] = np.clip(s.lateralOffset / HALF_TRACK_WIDTH, -1.0, 1.0)
        obs[4:11] = np.clip(s.rays / 50.0, 0.0, 1.0)
        obs[11] = np.clip(s.curvatureOfRoad / 0.1, -1.0, 1.0)
        opp_gap = s.opponentGapInMeter if s.opponentGapInMeter is not None else 50.0
        obs[12] = np.clip(opp_gap / 50.0, 0.0, 1.0)
        obs[13] = np.clip(s.opponentClosingSpeed / 15.0, -1.0, 1.0)
        return obs
    
    def reset(self,seed=None,options=None):

        # Reset the environment to an initial state and return the initial observation and info dictionary.
        super().reset(seed=seed)
        self.step_count = 0
        sensor_reading = self._get_stub_sensor_reading()
        observation = self._normalize_observation(sensor_reading)
        info = {"sensors": sensor_reading}
        return observation, info

    def step(self, action: np.ndarray):
        """
        Main Function to step the environment forward by one time step.
        """
        self.step_count += 1
        physical_action = self.decode_action(action)
        sensor_reading = self._get_stub_sensor_reading()
        observation = self._normalize_observation(sensor_reading)
        # Dummy reward: small progress reward
        reward = 0.5 * physical_action.throttle - 0.01
        # Termination: crashes or lap completion (False in stub)
        terminated = False
        # Truncation: time limit (2000 steps = ~66s)
        truncated = self.step_count >= MAX_EPISODE_STEPS
        info = {
            "sensors": sensor_reading,
            "step": self.step_count,
            "action": physical_action,
            "lap_completed": False,
            "crashed": False,
        }
        return observation, reward, terminated, truncated, info
    def render(self,render_mode:str|None=None):
        """Placeholder for Pygame renderer (added in Phase 2)"""
        pass
    def close(self):
        """Cleanup any active windows or resources"""