from dataclasses import dataclass
from typing import Callable

from common.domain.domain.PhysicalAction import PhysicalAction
from symbolic.fact.Fact import Fact
from Decision import Decision
from common.domain.domain.SensorReading import SensorReading

@dataclass
class Rule:
    id: str
    priority: int
    condition: Callable[[Fact, SensorReading, PhysicalAction], bool]
    action: Callable[[Fact, SensorReading], Decision]
