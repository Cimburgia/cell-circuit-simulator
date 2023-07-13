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
    - Diffusion of signal
    - Production of signal
    - Growth rate of ecoli
    - 
"""

