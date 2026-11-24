from dataclasses import dataclass
from typing import Callable

from common.domain.domain.PhysicalAction import PhysicalAction
from symbolic.fact.Fact import Fact
from Decision import Decision
from common.domain.domain.SensorReading import SensorReading

@dataclass
class Rule:
    """
        id: String unique id assigned to each rule
        priority: Int a higher value means higher priority
        condition: Function that retrn true if rule should be activated 
            Input:
                Fact: Facts from sensor reading
                SensorReading: Raw sensor reading
                PhysicalAction: proposed action that will be taken
            Output:
                True if rule should be activated 
                else False
    """

    id: str
    priority: int
    condition: Callable[[Fact, SensorReading, PhysicalAction], bool]
    action: Callable[[Fact, SensorReading], Decision]
