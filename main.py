from Simulation import Simulation
from Population import Population
from Person import Person

# Create a simulation and population object.
sim = Simulation()
pop = Population(sim)

# Set the initial infection conditions of the population.
pop.initial_infection(sim)
pop.display_statistics(sim)
pop.graphics()
input("\nPress enter to begin the simulation.")

# Run the simulation.
for i in range(1, sim.sim_days):

    # For a single day, spread the infection,update the population, display statistics and graph.
    pop.spread_infection(sim)
    pop.update(sim)
    pop.display_statistics(sim)
    pop.graphics()

    # If it is not the last day of the simulation, pause the program.
    if i !=  sim.sim_days -1:
        input("\nPress enter to advance to the next day.")
