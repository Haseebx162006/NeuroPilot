from dataclasses import dataclass, field

from Strategy import Startegy
from Rule import Rule
from common.domain.domain.SensorReading import SensorReading
from symbolic.facts.Facts import Fact

@dataclass
class Decision:
    activeRules: list[Rule] | None = None
    throttleMax: float = 1.0
    throttleMin: float = 0.0
    brakeMin: float = 0.0
    brakeMax: float = 1.0
    steerLimit: float = 1.0 # max absolute steering
    steerBias: float = 0.0 # additive, in [-1, 1]
    strategy: Startegy = Startegy.CRUISE
    explanation: list[str] = field(default_factory=list)

    @staticmethod
    def makeDecision(rules: list[Rule], facts: Fact, sensorReading: SensorReading) -> Decision:
        # TODO
        pass