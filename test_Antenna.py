import unittest
from IRIS import Antenna


class TestAntenna(unittest.TestCase):

    def test_GIVEN_coordiantes_dont_have_the_same_dimension_WHEN_computin_baseline_vector_THEN_raises_ValueError(self):
        a1 = Antenna([1, 2])
        a2 = Antenna([1, 2, 3])
        with self.assertRaises(ValueError):
            a1.vector_to(a2)

    def test_GIVEN_the_vector_between_antenna1_and_antenna2_is_calculated_WHEN_computing_the_baseline_vector_THEN_calculates_correctly(self):
        a1 = Antenna([1, 2, 4])
        a2 = Antenna([5, 6, 7])
        vector = a1.vector_to(a2)
        self.assertEqual(vector, [4, 4, 3])


    def test_GIVEN_length_of_coordiantes_is_less_than_2_WHEN_store_coordinates_THEN_raise_value_error(self):
        with self.assertRaises(ValueError):
            Antenna([1])

    def test_GIVEN_length_of_coordiantes_is_greater_than_3_WHEN_store_coordinates_THEN_raise_value_error(self):
        with self.assertRaises(ValueError):
            Antenna([1, 2, 3, 4])

    def test_GIVEN_length_of_coordiantes_of_antenna_1_does_not_match_the_length_of_coordinates_of_antenna_2_WHEN_computing_baseline_vector_THEN_lengths_must_be_equal(self):
        self.assertNotEqual(len(Antenna([1, 2, 3]).coordinates), len(Antenna([1, 2]).coordinates))




