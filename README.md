
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



<_Model Components_>

      a. Rainfall Module
      - IDF curve-based design storm generation
      - Huff temporal rainfall distribution
      - Multiple rainfall durations
      
      b. Runoff Module
      - NRCS Curve Number (CN) method
      - Effective rainfall estimation
      - Synthetic Unit Hydrograph transformation
      
      c. Drainage & Inundation Module
      - Storage–elevation relationship
      - Gravity drainage through outlet structures
      - Pump-assisted discharge scenarios
      - Dynamic storage routing

<_Model Components_>

      File	                        Description
      IDF_coef.txt	                 IDF equation coefficients
      variable.txt	                 Watershed parameters
      volume_Flooding_A.txt      	Storage-volume relationship

<_How to Run_>

      python main.py

      Simulation settings are defined in:

      SimulationConfig(
          var="a",
          r=0.875,
          pump_max=40,
          max_duration=48
      )



<_Output_>
      
      Results are stored in:

      output/

      Generated files:

      max_storage.txt
      total_inflow.txt

      Matrix Structure
      
      Rows            	      Columns
      Rainfall Duration (hr)	Pump Capacity

<_Example Visualization_>

      import numpy as np
      import matplotlib.pyplot as plt

      storage = np.loadtxt("output/max_storage.txt")

      plt.imshow(storage, aspect="auto")
      plt.colorbar(label="Maximum Storage (m³)")
      plt.xlabel("Pump Capacity")
      plt.ylabel("Rainfall Duration (hr)")
      plt.show()

<_Applications_>

      - Agricultural watershed flood-risk assessment
      - Pump station design
      - Drainage system planning
      - Climate resilience evaluation
      - Scenario-based infrastructure assessment

<_Future Development_>

      - Probabilistic rainfall scenarios
      - Climate change-adjusted IDF curves
      - Multi-watershed simulation
      - Automatic pump optimization
      - GIS integration
      
<_Citation_>

      If you use this framework for research purposes, please cite the associated publication (if available).

<_Author_>
      
      Kwihoon Kim
      Ph.D. in Agricultural Engineering  

<_License_>
      
      Developed for research applications in Agricultural Watershed hydrology and drainage system design.

