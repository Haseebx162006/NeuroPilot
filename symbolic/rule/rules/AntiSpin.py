from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule


AntiSpin = Rule(
    id = "R9 AntiSpin",
    priority = 50,
    condition = lambda fact, sensor, action: fact.speedHigh and abs(action.steer) > 0.6,
    action = lambda fact, sensor: Decision(steerLimit = 0.6)
)