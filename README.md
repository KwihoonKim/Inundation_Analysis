
<_Agricultural Watershed Drainage Simulation Framework_>
===

A modular Python framework for rainfall–runoff simulation and pump-assisted agricultural watershed drainage analysis.

The framework evaluates flood and inundation responses under various rainfall durations and pumping capacities by integrating hydrologic runoff generation and drainage routing processes.
This project integrates:

<_Features_>
- IDF-based design rainfall generation
- Huff temporal rainfall distribution
- NRCS Curve Number (CN) effective rainfall estimation
- Synthetic Unit Hydrograph runoff simulation
- Storage–outflow routing
- Gravity drainage calculation
- Pump-assisted drainage scenario analysis
- Duration–Pump Capacity sensitivity analysis

<_Modeling Workflow_>

      Design Rainfall
            ↓
      Time Distribution
            ↓
      Effective Rainfall
      (NRCS-CN Method)
            ↓
      Runoff Hydrograph (Synthetic UH)
            ↓
      Storage Routing
      ├── Sluice Gate Drainage
      └── Pump Drainage
            ↓
      Flooding Assessment
      
<_Project Structure_>

      Agricultural Watershed_drainage_simulation

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
