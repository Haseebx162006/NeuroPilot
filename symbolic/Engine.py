from common.domain.domain.PhysicalAction import PhysicalAction
from common.domain.domain.SensorReading import SensorReading
from symbolic.fact.Fact import Fact
from symbolic.fact.FactPredicateConfig import resolveFacts
from symbolic.rule.Strategy import Strategy
from symbolic.rule.Decision import Decision
from symbolic.rule.Rule import Rule
from symbolic.rule.rules.Rules import Rules


def decide(
    sensor: SensorReading,
    propsedAction: PhysicalAction,
    rules: list[Rule] = Rules
) -> Decision:
    facts: Fact = resolveFacts(sensor)

    rulesActivated: list[Rule] = sorted(
        [rule for rule in rules if rule.condition(facts, sensor, propsedAction)],
        key = lambda rule : rule.priority,
        reverse = True
    )

    decision: Decision = Decision()

    if len(rulesActivated) == 0:
        return decision

    ruleDecisions: list[tuple[Rule, Decision]] = [ (rule, rule.action(facts, sensor)) for rule in rulesActivated ]
    priorityTotal: int = sum([rule.priority for rule in rulesActivated])
    highestPriorityStrategyFound = Strategy.CRUISE
    weightedSteerBiasSum = 0.0
    throttleMin = 0.0

    for rule, ruleDecision in ruleDecisions:
        decision.brakeMax = min(decision.brakeMax, ruleDecision.brakeMax)
        decision.brakeMin = max(decision.brakeMin, ruleDecision.brakeMin)

        decision.steerLimit = min(decision.steerLimit, ruleDecision.steerLimit)
        
        decision.throttleMax = min(decision.throttleMax, ruleDecision.throttleMax)
        throttleMin = max(throttleMin, ruleDecision.throttleMin)

        weightedSteerBiasSum += ruleDecision.steerBias * (rule.priority / priorityTotal)

        if highestPriorityStrategyFound == Strategy.CRUISE:
            highestPriorityStrategyFound = ruleDecision.strategy


    decision.steerBias = max(-1, min(1, weightedSteerBiasSum))
    decision.strategy = highestPriorityStrategyFound

    if throttleMin <= decision.throttleMax:
        decision.throttleMin = throttleMin

    if decision.throttleMin > decision.throttleMax or decision.brakeMin > decision.brakeMax:
        return ruleDecisions[0][1]

    return decision