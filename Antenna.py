import math


class Antenna:

    def __init__(self, coordinates: list):
        """
        stores a list of cartesian coordinates in self
        :param coordinates: list containing lists of cartesian coordinates in either 2- or 3-dimensional space
        """

        if len(coordinates) not in (2, 3):
            raise ValueError("coordinates must be either two or three dimensions")

        self.coordinates = coordinates

    def vector_to(self, antenna: "Antenna"):
        """
        computes the baseline vector between two antenna
        :param antenna: object containing antenna positional coordinates
        """

        if len(self.coordinates) != len(antenna.coordinates):
            raise ValueError("coordinates must be the same dimension")

        baseline_vector = [antenna.coordinates[i] - self.coordinates[i] for i in range(len(self.coordinates))]

        return baseline_vector

    def length(self, antenna: "Antenna"):
        """computes the Euclidean distance between two antennae
        :param antenna: object containing antenna positional coordinates"""

        return math.dist(antenna.coordinates, self.coordinates)
