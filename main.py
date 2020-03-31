import random

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


class Person:
    """A class to model an individual person in a population."""

    def __init__(self):
        """Initialize the attributes."""

        self.is_infected = False # Person starts healthy, not infected.
        self.is_dead = False # Person starts alive.
        self.days_infected = 0 # Keeps track of days infected for individual person.


    def infect(self, simulation):
        """Infect a person based on simulation conditions."""

        """
        2020 Apr 01 Wed  00:35:33 - Arjun Adhikari
        Random number generated must be less than infection probability to infect.  
        """
        if random.randint(0,100) < simulation.infection_probability:
            self.is_infected = True

    def heal(self):
        """Heals a person from an infection."""
        
        self.is_infected = False
        self.days_infected = 0


    def die(self):

        """Kill a person."""

        self.is_dead = True

    def update(self, simulation):
        """Update an individual person if the person is not dead.
        Check id they are infected. 
        If they are, increase the days infected count, 
        then check if they should die or be healed."""

        # Check if the person is not dead before updating.
        if not self.is_dead:
            if self.is_infected += 1
            self.days_infected += 1

            # Check to see if the person will die.
            if random.randint(0,100) < simulation.mortality_rate:
                self.die()
            # Check if the infection is over, if it is, heal the person.
            elif self.days_infected ==  simulation.infection_duration:
                self.heal()
                