import random


class Person:
    """A class to model an individual person in a population."""

    def __init__(self):
        """Initialize the attributes."""

        self.is_infected = False  # Person starts healthy, not infected.
        self.is_dead = False  # Person starts alive.
        # Keeps track of days infected for individual person.
        self.days_infected = 0

    def infect(self, simulation):
        """Infect a person based on simulation conditions."""

        """
        2020 Apr 01 Wed  00:35:33 - Arjun Adhikari
        Random number generated must be less than infection probability to infect.
        """
        if random.randint(0, 100) < simulation.infection_probability:
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
        Check if they are infected.
        If they are, increase the days infected count,
        then check if they should die or be healed."""

        # Check if the person is not dead before updating.
        if not self.is_dead:
            # Check if the person is infected.
            if self.is_infected:
                self.days_infected += 1

                # Check to see if the person will die.
                if random.randint(0, 100) < simulation.mortality_rate:
                    self.die()
                # Check if the infection is over, if it is, heal the person.
                elif self.days_infected == simulation.infection_duration:
                    self.heal()
