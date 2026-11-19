from dataclasses import dataclass
from typing import Callable

from symbolic.facts.Facts import Fact
from Decision import Decision
from common.domain.domain.SensorReading import SensorReading

@dataclass
class Rule:
    id: str
    priority: int
    condition: Callable[[Fact, SensorReading], bool]
    action: Callable[[Fact, SensorReading], Decision]
