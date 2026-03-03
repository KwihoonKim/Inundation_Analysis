
Agricultural Watershed Drainage Simulation Framework

A modular Python framework for rainfall–runoff simulation and pump-assisted Agricultural Watershed drainage analysis.

This project integrates:

IDF-based / Huff-based design rainfall

NRCS-CN effective rainfall method

Synthetic unit hydrograph

Storage–outflow routing

Pump capacity scenario analysis

The framework evaluates inundation risk under varying rainfall durations and pumping capacities.

<1. Overview>
===
   
Agricultural Watershed drainage systems must be evaluated under multiple rainfall durations and pumping scenarios.
This simulation engine performs:

Design Rainfall → Effective Rainfall → Runoff Hydrograph → Storage Routing → Pump Discharge Analysis

The final output is a 2D response matrix:

Rainfall Duration × Pump Capacity → Maximum Storage / Inflow

<2. Model Components>
===
Rainfall

IDF curve-based design rainfall

Temporal rainfall distribution

Runoff Generation

NRCS Curve Number (CN) method

Synthetic unit hydrograph (NRCS Type III)

Inundation Simulation

Storage–elevation relationship

Gravity drainage through culvert/weir

Pump-assisted discharge scenarios

<3. Project Structure>
===
   
   
Agricultural Watershed_drainage_sim


│

├── input/

│   ├── IDF_coef.txt

│   ├── variable.txt

│   └── volume_Flooding_A.txt
│

├── src/


│   ├── config.py

│   ├── io.py

│   ├── rainfall.py

│   ├── runoff.py

│   ├── inundation.py

│   ├── result.py

│   └── simulator.py
│

└── main.py

<4. How to Run>
===
python main.py

Simulation parameters are defined in:

src/config.py

Example:

SimulationConfig(
    var="a",
    r=0.875,
    pump_max=40,
    max_duration=48
)
<5. Output>
===

Results are saved in:

output/

Files:

max_storage.txt

total_inflow.txt

Matrix format:

Rows → Rainfall Duration (hr)
Columns → Pump Capacity

<6. Example Analysis>
===

Maximum storage heatmap:

import numpy as np
import matplotlib.pyplot as plt

storage = np.loadtxt("output/max_storage.txt")

plt.imshow(storage, aspect="auto")
plt.colorbar(label="Max Storage (m3)")
plt.xlabel("Pump Capacity")
plt.ylabel("Rainfall Duration (hr)")
plt.show()
<7. Applications>
===

Agricultural Watershed flood risk assessment

Pump design optimization

Drainage system planning

Sensitivity analysis of rainfall duration

<8. Future Extensions>
===

Probabilistic rainfall scenarios

Multi-site simulation

Optimization-based pump sizing

Climate change IDF adjustment

Author

Developed for research applications in Agricultural Watershed hydrology and drainage system design.

License

For academic and research purposes.
