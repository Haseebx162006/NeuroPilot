
from typing import Callable
from common.domain.domain.SensorReading import SensorReading
from symbolic.fact.Fact import Fact
from symbolic.rule.rules.AntiSpin import AntiSpin
from symbolic.rule.rules.AntiTimidity import AntiTimidity
from symbolic.rule.rules.CornerEntry import CornerEntry
from symbolic.rule.rules.Misalignment import Misalignment
from symbolic.rule.rules.StallRecovery import StallRecovery
from symbolic.rule.rules.CollionAvoidance import CollionAvoidance
from symbolic.rule.rules.CornerBraking import CornerBraking
from symbolic.rule.rules.EdgeCorrection import EdgeCorrection
from symbolic.rule.rules.EmergencyBrake import EmergencyBrake
from symbolic.rule.rules.ObstacleDetour import ObstacleDetour
from symbolic.rule.rules.OverSpeedGuard import OverSpeedGuard
from symbolic.rule.rules.Overtake import Overtake
from symbolic.rule.rules.Recovery import Recovery

def TODO():
    pass
# TODO implement these
FuzzyCollisionRisk = Callable[[Fact, SensorReading], float] 
FuzzyBrakeIntensity = Callable[[Fact, SensorReading], float] 
AStartWayPintSteerBias = Callable[[Fact, SensorReading], float]

Rules = [
    Recovery,
    EmergencyBrake,
    CollionAvoidance,
    CornerBraking,
    OverSpeedGuard,
    EdgeCorrection,
    ObstacleDetour,
    Overtake,
    AntiSpin,
    Misalignment,
    CornerEntry,
    AntiTimidity,
    StallRecovery
]