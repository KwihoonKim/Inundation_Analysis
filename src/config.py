# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:31:59 2026

@author: Kwihoon
"""

from dataclasses import dataclass

@dataclass
class SimulationConfig:
    var: str = "a"
    r: float = 0.875
    quant: int = 4
    pump_max: int = 40
    max_duration: int = 48
    freq: int = 20