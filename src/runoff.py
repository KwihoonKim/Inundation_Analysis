# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:21:33 2026

@author: Kwihoon
"""

from src.rainfall_distribution import idf
from src.unit_hydrograph import nrcs3
from src.eff_rainfall import nrcs_cn
from src.hydrograph import synthesize


def generate_hydrograph(duration, var, area, tc, cn, r):
    unit_time, unit_hydro = nrcs3(area, tc)
    interval = unit_time[1] - unit_time[0]

    rainfall = idf(duration, interval, var, r)
    rainfall_eff = nrcs_cn(rainfall, cn)

    hydro_time, hydro = synthesize(rainfall_eff, unit_hydro)

    return hydro_time, hydro, interval