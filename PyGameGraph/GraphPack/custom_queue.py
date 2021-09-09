'''
Python's native PriorityQueue needs a wrapper class to ignore the data items and only sort by priority int
'''


from dataclasses import dataclass, field
from typing import Any

@dataclass(order = True)
class Custom_Queue:
    priority: int
    item: Any = field(compare = False)
