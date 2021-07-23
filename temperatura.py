#%%

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib as mpl

temperature = ctrl.Antecedent(np.arange(0, 50, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 100, 1), 'humidity')

temperature_variation = ctrl.Consequent(np.arange(-15, 15, 1), 'temperature_variation')

temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 25])
temperature['normal'] = fuzz.trimf(temperature.universe, [0, 25, 50])
temperature['hot'] = fuzz.trimf(temperature.universe, [25, 50, 50])

humidity['low_wet'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['wet'] = fuzz.trimf(humidity.universe, [0, 50, 100])
humidity['high_wet'] = fuzz.trimf(humidity.universe, [50, 100, 100])

temperature_variation['low'] = fuzz.trimf(temperature_variation.universe, [-15, -15, 0])
temperature_variation['medium'] = fuzz.trimf(temperature_variation.universe, [-15, 0, 15])
temperature_variation['high'] = fuzz.trimf(temperature_variation.universe, [0, 15, 15])

temperature.view()
humidity.view()
temperature_variation.view()

rule1 = ctrl.Rule(humidity['high_wet'] | temperature['hot'], temperature_variation['high'])
rule2 = ctrl.Rule(humidity['wet'], temperature_variation['medium'] )
rule3 = ctrl.Rule(humidity['low_wet'] & temperature['cold'], temperature_variation['low'])

variation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
variation = ctrl.ControlSystemSimulation(variation_ctrl)

variation.input['temperature'] = float(input('Enter the temperature:  '))
variation.input['humidity'] = float(input('Enter the humidity:  '))

variation.compute()

print(f"\n\n The temperature variantion is {variation.output['temperature_variation']}% \n\n")
temperature_variation.view(sim=variation)

# %%
