"""
	- Start with simple model that assumes everything is going to work perfectly
	- Try to add in variance:
		○ Maybe we expect this to vary via a normal distribution or Poisson
		○ Understand how assumptions impact our outcome
			§ Run model n times (~10k) and then look at outcome
		○ Take things that make a big impact and also our unknown and try to narrow down with experimental data
	- For parameters that influence others:
		○ Treat the relationship between them as an unknown parameter as well
			§ E.g., maybe the growth rate has a linear relationship to the amount of nutrient or exponential. Add these as unknowns and test
	- Always test and try to understand impact of unknowns

    Current model parameters:
    - Diffusion of signal through hydrogel
		- Varied
    - Production of signal
		- Varied
    - Concentration of cells per volumne of hydrogel
		- Fixed at print time
    
"""


def signal_diffusion_rate(signal, [hydrogel_properties]):
	'''Takes a given signaling molecule and returns the rate at which it will
	move (diffuse) through the hydrogel

	Inputs:
		- Signaling molecule
		- Properties of hydrogel (might be defined by user dynamically)
	'''
    pass

def signal_production(cell, signal, [parameters]):
	"""given a specific cell and its properties, model the rate at which the
	colony will produce a given signal. This will depend on a number of other parameters"""
	pass
