# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:31:34 2026

@author: Kwihoon
"""
from src.config import SimulationConfig
from src.simulator import UrbanDrainageSimulator
import numpy as np

def main():

    config = SimulationConfig(
        var="a",
        r=0.875,
        pump_max=40,
        max_duration=48,
    )

    simulator = UrbanDrainageSimulator(config)

    storage, inflow = simulator.run()
    np.savetxt('storage.txt', storage)
    np.savetxt('inflow.txt', inflow)

    print("Simulation complete")
    print("Max storage matrix shape:", len(storage))


if __name__ == "__main__":
    main()