import random
from Person import Person

class Population():
    """A class to model whole population of Person objects."""

    def __init__(self, simulation):
        """Initialize the attributes."""

        self.population = []

        # Create the correct number of Person instances based on the simulation conditions.
        for _ in range(simulation.population_size):

            person = Person()
            self.population.append(person)

    def initial_infection(self, simulation):
        """Infect an initial portion of the population."""

        # The number of people to infect is found by taking the pop size * infection percentage.
        # We must rounf to 0 decimals and cast to an int so we can use infected count in a for loop.
        infected_count = int(
            round(simulation.infection_percent*simulation.population_size))

        # Infect the correct the number of people.
        for i in range(infected_count):
            self.population[i].is_infected = True
            self.population[i].days_infected = 1

        # Shuffle the population list so we can spread the infection out randomly.
        random.shuffle(self.population)

    def spread_infection(self, simulation):
        """Spread the infection to all adjacent people in the population list."""

        for i in range(len(self.population)):
            # If person is ALIVE, see if they should be infected.
            # Don't bother infecting a dead person, they are infected and dead.
            # Check to see if adjacent Persons are infected.
            if self.population[i].is_infected == False:
                # i is the first persson if in the list, can only check to the right.
                if i == 0:
                    if self.population[i+1].is_infected:
                        self.population[i].infect(simulation)

                # i is in the middle of the list, can check to the left [i-1] and right[i+1].
                elif i < len(self.population)-1:
                    if self.population[i-1].is_infected or self.population[i+1].is_infected:
                        self.population[i].infect(simulation)

                # i is the last person in the list, can only check to the left.
                elif i == len(self.population)-1:
                    if self.population[i-1].is_infected:
                        self.population[i].infect(simulation)

    def update(self, simulation):
        """Update the whole population by updating each individual person in the simulation."""

        simulation.day_number += 1

        # Call the update method for all person instances in the population.
        for person in self.population:
            person.update(simulation)

    def display_statistics(self, simulation):
        """Display the current statistics of a population."""

        # Initialize values.
        total_infected_count = 0
        total_death_count = 0

        # Loop through whole population.
        for person in self.population:

            # Person is infected.
            if person.is_infected:
                total_infected_count += 1

            # Person is dead.
            elif person.is_dead:
                total_death_count += 1

        # Calculate the percentage of population that is infected.
        infected_percent = round(
            100 * (total_infected_count/simulation.population_size), 4)
        death_percent = round(
            100 * (total_death_count/simulation.population_size), 4)

        print(f"\n Day # {simulation.day_number} ---")
        print("Percentage of Population Infected: " +
              str(infected_percent) + "%")
        print("Percentage of Population Dead: " + str(death_percent) + "%")
        print(
            f"Total People Infected : {total_infected_count} / {simulation.population_size}")
        print(
            f"Total Deaths : {total_death_count} / {simulation.population_size}")

    def graphics(self):
        """A graphical representation for a population. 0 is healthy, I infected and X head."""

        # A list to hold all X, I and O to represent the status of each person.
        status = []
        for person in self.population:
            # Person is dead.
            if person.is_dead:
                char = 'X'
            # Person is infected.
            elif person.is_infected:
                char = 'I'
            # Person is healthy.
            else:
                char = 'O'

            status.append(char)

        # Print out all status characters separated by -.
        for letter in status:
            print(letter, end='-')
