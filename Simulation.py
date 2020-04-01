class Simulation:
    """A class to control the simulation and help facilitate in the spread of the disease."""

    def __init__(self):
        """Initialize attributes."""
        self.day_number = 1

        # Get simulation initial conditions from the user.
        print("To simulate the epidemic outbreak, we must know the population size.")
        self.population_size = int(input("--- Enter the population size : "))

        print("We must start by infecting a portion of population.")
        self.infection_percent = float(
            input("--- Enter the percentage of (0-100) of the population of initially infect : "))
        self.infection_percent /= 100

        print("We must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = float(input(
            "--- Enter the probability (0-100) that a person gets infected when exposed to the disease : "))

        print("We must know how long the infection will last when exposed.")
        self.infection_duration = int(
            input("--- Enter the duration in days of the infection : "))

        print("We must know the mortality rate of those infected.")
        self.mortality_rate = float(
            input("--- Enter the mortality rate (0-100) of the infection :"))

        print("We must know how long to run the simulation.")
        self.sim_days = int(
            input("--- Enter the number of days to simulate : "))

