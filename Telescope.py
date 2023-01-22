import numpy as np


class Telescope:

    def __init__(self, antenna: list):

        """
        :param antenna: collection of coordinates of each antenna. Coordinates must be the same length.
        """
        if len(antenna) < 2:
            raise ValueError("must have at least two antennae")

        self.antenna = antenna

    def baseline_between(self, antenna1_index: int, antenna2_index: int):
        """
        :param antenna1_index: index of first antenna to be compared
        :param antenna2_index: index of second first antenna to be compared
        :return vector between two antennae
        """

        if antenna1_index == antenna2_index:
            raise ValueError("antenna should be different")
        if antenna1_index < 0 or antenna2_index < 0:
            raise ValueError("antenna index should be greater than or equal to zero")
        if antenna1_index >= len(self.antenna) or antenna2_index >= len(self.antenna):
            raise ValueError("index has to be less than the number of antenna")

        baseline_vector = self.antenna[antenna1_index].vector_to(self.antenna[antenna2_index])

        return baseline_vector

    def baseline_length(self, antenna1_index: int, antenna2_index: int):

        """
        :param antenna1_index: index of first antenna to be compared
        :param antenna2_index: index of second antenna to be compared
        :return: Euclidean distance between two antennae
        """

        if antenna1_index == antenna2_index:
            raise ValueError("antenna should be different")
        if antenna1_index < 0 or antenna2_index < 0:
            raise ValueError("antenna index should be greater than or equal to zero")
        if antenna1_index >= len(self.antenna) or antenna2_index >= len(self.antenna):
            raise ValueError("index has to be less than the number of antenna")

        baseline_length = self.antenna[antenna1_index].length(self.antenna[antenna2_index])

        return baseline_length

    def path_difference(self, antenna1_index: int, antenna2_index: int, theta: float, alpha: float):

        """
        finds the path difference between radio waves
        :param antenna1_index: index of first antenna to be compared
        :param antenna2_index: index of second antenna to be compared
        :param theta: angle between baseline vector and radio wave source
        :param alpha: angle between two antennae
        :return: absolute value of the path difference between two antennae
        """

        if not 0 <= theta < 2 * np.pi:
            raise ValueError("theta must lie in the interval [0,2pi)")
        if not 0 <= alpha < 2 * np.pi:
            raise ValueError("alpha must lie in the interval [0,2pi)")

        baseline = self.baseline_length(antenna1_index, antenna2_index)
        path_difference = baseline * np.cos(alpha) * np.cos(theta)

        return abs(path_difference)

    def phase_difference(self, antenna1_index: int, antenna2_index: int, wavelength: float, theta: float, alpha: float):

        """
        finds the phase difference between radio waves
        :param antenna1_index: index of first antenna to be compared
        :param antenna2_index: index of second antenna to be compared
        :param wavelength: wavelength of radio wave
        :param theta: angle between baseline vector and radio wave source
        :param alpha: angle between two antennae
        :return: phase difference modulo 2pi between two antennae 
        """

        if wavelength <= 0:
            raise ValueError("wavelength should be greater than zero")

        path_difference = self.path_difference(antenna1_index, antenna2_index, theta, alpha)

        phase_diff = 2 * np.pi * path_difference / wavelength
        phase_diff_mod = phase_diff % (2 * np.pi)

        return phase_diff_mod
