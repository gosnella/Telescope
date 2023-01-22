import math
import unittest
from IRIS import Antenna, Telescope


class TestTelescope(unittest.TestCase):

    def setUp(self):
        self.antenna1 = Antenna([1, 2, 3])
        self.antenna2 = Antenna([1, 2, 4])
        self.antennae_list = [self.antenna1, self.antenna2]
        self.t = Telescope(self.antennae_list)

    def test_GIVEN_antenna1_index_is_equal_to_antenna2_index_WHEN_computing_baseline_vector_THEN_raises_ValueError(self):
        with self.assertRaises(ValueError):
            self.t.baseline_between(1, 1)

    def test_GIVEN_antenna1_index_is_less_than_0_WHEN_computing_baseline_vector_THEN_raises_ValueError(self):
        with self.assertRaises(ValueError):
            self.t.baseline_between(-1, 2)

    def test_GIVEN_antenna2_index_is_less_than_0_WHEN_computing_baseline_vector_THEN_raises_ValueError(self):
        with self.assertRaises(ValueError):
            self.t.baseline_between(1, -2)
    def test_GIVEN_antenna1_index_is_greater_than_the_number_of_antenna_WHEN_computing_baseline_vector_THEN_raises_ValueError(self):
        with self.assertRaises(ValueError):
            self.t.baseline_between(3, 2)
    def test_GIVEN_antenna2_index_is_greater_than_the_number_of_antenna_WHEN_computing_baseline_vector_THEN_raises_ValueError(self):
        with self.assertRaises(ValueError):
            self.t.baseline_between(1, 3)

    def test_GIVEN_baseline_length_is_one_and_theta_is_pi_WHEN_calculate_the_path_difference_between_two_antenna_THEN_path_difference_is_negative_one(
            self):
        value = self.t.path_difference(0, 1, math.pi, math.pi)
        self.assertEqual(value, 1)

    def test_GIVEN_positive_baseline_and_positive_wavelength_and_perpendicular_angle_WHEN_compute_phase_difference_THEN_phase_difference_is_zero(
            self):
        value = self.t.phase_difference(0, 1, 1, math.pi/2, math.pi/2)
        self.assertAlmostEqual(value, 0, 10)

    def test_GIVEN_baseline_length_is_1_wavelength_is_1_and_direction_to_source_is_parallel_to_baseline_WHEN_compute_phase_difference_THEN_phase_difference_is_zero(
            self):
        value = self.t.phase_difference(0, 1, 1, math.pi, math.pi)
        self.assertAlmostEqual(value, 0, 10)

    def test_GIVEN_alpha_is_zero_WHEN_compute_phase_difference_for_any_pair_fo_antennae_THEN_phase_difference_is_path_difference(self):
        phase_diff = self.t.phase_difference(0, 1, 1, 0, 0)
        path_diff = self.t.path_difference(0, 1, 0, 0)
        self.assertAlmostEqual(path_diff, 1)
        self.assertAlmostEqual(phase_diff, 0)

    def test_GIVEN_wavelength_is_negative_WHEN_calculate_phase_difference_for_any_two_antennae_THEN_raises_error(self):
        with self.assertRaises(ValueError):
            self.t.phase_difference(0, 1, -1, -1, math.pi/2)

    def test_GIVEN_alpha_is_pi_over_2_WHEN_compute_phase_difference_for_any_pair_fo_antennae_THEN_phase_difference_is_0(self):
        value = self.t.phase_difference(0, 1, 1, 1, math.pi / 2)
        self.assertAlmostEqual(value, 0)
    def test_GIVEN_alpha_is_0_and_theta_is_1_and_wavelength_is_1_and_baseline_length_is_1_WHEN_compute_phase_difference_between_two_antennae_THEN_phase_difference_is_0(self):
        value = self.t.phase_difference(0, 1, 1, 0, 0)
        self.assertAlmostEqual(value, 0)

    def test_GIVEN_alpha_is_0_and_theta_is_pi_over_2_and_wavelength_is_1_and_baseline_length_is_1_WHEN_compute_phase_difference_between_two_antennae_THEN_phase_difference_is_0(
            self):
        value = self.t.phase_difference(0, 1, 1, math.pi/2, 0)
        self.assertAlmostEqual(value, 0)

    def test_GIVEN_alpha_is_pi_over_2_and_theta_is_0_and_wavelength_is_1_and_baseline_length_is_1_WHEN_compute_phase_difference_between_two_antennae_THEN_phase_difference_is_0(
            self):
        value = self.t.phase_difference(0, 1, 1, 0, math.pi/2)
        self.assertAlmostEqual(value, 0)


    def test_GIVEN_alpha_is_non_zero_and_theta_is_non_zero_WHEN_compute_phase_difference_between_two_antennae_THEN_phase_difference_is_positive(
            self):
        value = self.t.phase_difference(0, 1, 1, 0, math.pi/2)
        self.assertGreater(value, 0)

    def test_GIVEN_path_difference_is_greater_than_wavelength_WHEN_compute_phase_difference_between_two_antennae_THEN_phase_difference_is_positive(
            self):
        value = self.t.phase_difference(0, 1, 1, 0, math.pi/2)
        self.assertGreater(value, 0)

    def test_GIVEN_alpha_is_pi_and_theta_is_a_real_number_WHEN_compute_phase_difference_between_two_antennae_THEN_phase_difference_is_in_range_0_to_2pi(
            self):
        value = self.t.phase_difference(0, 1, 1, math.pi, 1)
        self.assertTrue(0 <= value < 2 * math.pi)

    def test_GIVEN_theta_is_less_than_0_WHEN_compute_phase_difference_THEN_raises_ValueError(self):
        with self.assertRaises(ValueError):
            self.t.phase_difference(0, 1, 1, -1, 1)

    def test_GIVEN_theta_is_greater_than_2piWHEN_compute_phase_difference_THEN_raises_ValueError(self):
        with self.assertRaises(ValueError):
            self.t.phase_difference(0, 1, 1, 3*math.pi, 1)

    def test_GIVEN_alpha_is_less_than_0_WHEN_compute_phase_difference_THEN_raises_ValueError(self):
        with self.assertRaises(ValueError):
            self.t.phase_difference(0, 1, 1, 1, -1)

    def test_GIVEN_alpha_is_greater_than_2pi_WHEN_compute_phase_difference_THEN_raises_ValueError(self):
        with self.assertRaises(ValueError):
            self.t.phase_difference(0, 1, 1, 1, 3*math.pi)

    def test_GIVEN_radio_wave_is_parallel_to_both_antennae_and_wavelength_is_less_than_baseline_length_WHEN_compute_phase_difference_THEN_within_the_range(self):
        value = self.t.phase_difference(0, 1, 0.5, 0, 0)
        self.assertAlmostEqual(value, 0)


if __name__ == '__main__':

    unittest.main()
