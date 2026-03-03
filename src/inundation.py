# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:26:21 2026

@author: Kwihoon
"""

import numpy as np
import itertools
from src.drainage import drainage_flow, vol_to_level


SECONDS_PER_HOUR = 3600


def simulate_inundation(
    hydro_time,
    hydrograph,
    interval,
    elevation_volume,
    width1,
    height1,
    sill_elev1,
    pump_max,
):

    runoff_volume = hydrograph * interval * SECONDS_PER_HOUR

    inun_results_storage = []
    inun_results_inflow = []

    for pump in range(pump_max):

        storage = 0
        level = vol_to_level(storage, elevation_volume)
        results = []

        for k in range(len(hydro_time)):

            inflow = runoff_volume[k]

            outflow1 = drainage_flow(
                level, sill_elev1, sill_elev1, width1, height1
            ) * interval * SECONDS_PER_HOUR

            outflow2 = 0
            if level > sill_elev1:
                outflow2 = min(pump * interval * SECONDS_PER_HOUR, storage)

            storage = max(0, storage + inflow - outflow1 - outflow2)
            level = vol_to_level(storage, elevation_volume)

            results.append((storage, level, inflow))

        results = np.array(results)

        max_storage = np.max(results[:, 0])
        total_inflow = np.sum(results[:, 2])

        inun_results_storage.append(round(max_storage, 0))
        inun_results_inflow.append(round(total_inflow, 0))

    return inun_results_storage, inun_results_inflow