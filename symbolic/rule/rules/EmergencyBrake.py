from common.domain.domain.SensorReading import SensorReading
from symbolic.fact.Fact import Fact
from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule

EmergencyBrake = Rule(
    id = "R2 EmergencyBrake",
    priority = 95,
    condition = lambda fact, sensor, action: fact.obstacleClose and sensor.speed > 6.0,
    action = Decision(
        throttleMax = 0.0,
        brakeMin = 0.8
    )
)