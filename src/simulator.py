# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:20:25 2026

@author: Kwihoon
"""

from src.io import load_idf_table, load_variable, load_volume
from src.runoff import generate_hydrograph
from src.inundation import simulate_inundation
import numpy as np

class UrbanDrainageSimulator:

    def __init__(self, config):
        self.config = config
        self.idf_table = load_idf_table()
        self.variable = load_variable(config.var)
        self.elevation_volume = load_volume(config.var)

        (
            self.name,
            self.cn,
            self.area,
            self.tc,
            self.site,
            self.width1,
            self.height1,
            self.sill_elev1,
            *_,
        ) = self.variable

    def run(self):

        final_storage = []
        final_inflow = []

        for duration in range(1, self.config.max_duration + 1):

            hydro_time, hydrograph, interval = generate_hydrograph(
                duration,
                self.config.var,
                float(self.area),
                float(self.tc),
                float(self.cn),
                self.config.r,
            )

            storage_res, inflow_res = simulate_inundation(
                hydro_time,
                hydrograph,
                interval,
                self.elevation_volume,
                float(self.width1),
                float(self.height1),
                float(self.sill_elev1),
                self.config.pump_max,
            )

            final_storage.append(storage_res)
            final_inflow.append(inflow_res)
        final_storage = np.array(final_storage)
        final_inflow = np.array(final_inflow)

        return final_storage, final_inflow