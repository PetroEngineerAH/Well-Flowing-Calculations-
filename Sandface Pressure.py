#METHOD #1 SANDFACE PRESSURE CALCULATION
Oil_Rate = 500    #BOPD

Water_Rate = 2500   #BWPD 

Water_Cut = Water_Rate / (Oil_Rate + Water_Rate)     #%

print(f"Water_Cut: {Water_Cut:,.2f} % - Water Cut")

Reservoir_Pressure = 4100    #psi 

Pump_Intake_Pressure_PIP = 1900     #psi 

Oil_Gradient = 0.395     #psi/ft

Water_Gradient = 0.43333   #psi/ft 

Mixture_Gradient = (Oil_Gradient*(1-Water_Cut)) + (Water_Gradient*Water_Cut)

print(f"Mixture_Gradient: {Mixture_Gradient:,.3f} psi/ft - Mixture Fluid Gradient")

Mid_Point_Perf = 10950    #FTTVD 

Sensor_Depth = 13600     #FTTVD 

Mid_Point_Perf_Sensor = Sensor_Depth - Mid_Point_Perf

Hydrostatic_Pressure = Mixture_Gradient * Mid_Point_Perf_Sensor

print(f"Hydrostatic_Pressure: {Hydrostatic_Pressure:,.2f} psi - Hydrostatic Pressure")

Sandface_Dynamic_Pressure = Hydrostatic_Pressure + Pump_Intake_Pressure_PIP

print(f"Sandface_Dynamic_Pressure: {Sandface_Dynamic_Pressure:,.2f} psi   - Sandface Dynamic Pressure")

Productivity_Index = (Oil_Rate+Water_Rate)/(Reservoir_Pressure-Sandface_Dynamic_Pressure)             #bbl/d/psi 

print(f"Productivity_Index: {Productivity_Index:,.2f} bbl/d/psi - Productivity Index")

#METHOD #2 PIP CALCULATION 

API = 30

Density_Mixture = (141.5/(API+131.5))*(1-Water_Cut)+1*Water_Cut

print(f"Density_Mixture: {Density_Mixture:,.5f} lb/ft3 - Density Mixture")

Pump_Intake_Pressure_PIP_Calculated = Sandface_Dynamic_Pressure - ((Sensor_Depth-Mid_Point_Perf)*Density_Mixture*0.4333)

print(f"Pump Intake Pressure Calculated: {Pump_Intake_Pressure_PIP_Calculated:,.2f} psi - PIP Calculated")

#METHOD 3 WELL FLOWING CALCULATIONS UNDERBALANCED PERFORATIONS 

Fluid_Level_Perforating = 500        #Fluid Level at time of perforation 

Calculated_Pressure_Perforations = (Mid_Point_Perf-Fluid_Level_Perforating)*Mixture_Gradient

print(f"Calculated Pressure at Perforations: {Calculated_Pressure_Perforations:,.2f} psi - Calculated Pressure at Perforations")

Change_in_Pressure_Underbalanced = Reservoir_Pressure - Calculated_Pressure_Perforations

Drawdown = (Reservoir_Pressure - Calculated_Pressure_Perforations) / (Reservoir_Pressure)

print(f"Change in Pressure Underbalanced: {Change_in_Pressure_Underbalanced:,.2f} psi - Change in Pressure Underbalanced")

#WELL FLOW ALL THE WAY TO SURFACE? 

Calculated_WellFlow_Pressure = Calculated_Pressure_Perforations + (Fluid_Level_Perforating*Oil_Gradient)    #psi

print(f"Calculated_WellFlow_Pressure: {Calculated_WellFlow_Pressure:,.2f} psi - Calculated Well Flowing Pressure")

if Reservoir_Pressure-Calculated_WellFlow_Pressure > 0: 
    print("Well will flow to surface")
else: 
    print("Well will not flow to surface")


    



