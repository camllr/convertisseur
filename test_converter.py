import unittest
from converter import convert_distance, convert_temperature, convert_weight, convert_volume

class TestConverter(unittest.TestCase):

    def test_convert_distance_km_to_m(self):
        result = convert_distance(1, "km", "m")
        self.assertEqual(result, 1000)

    def test_convert_distance_m_to_km(self):
        result = convert_distance(1500, "m", "km")
        self.assertEqual(result, 1.5)

    def test_convert_temperature_c_to_f(self):
        result = convert_temperature(0, "C", "F")
        self.assertAlmostEqual(result, 32.0, places=2)

    def test_convert_weight_kg_to_g(self):
        result = convert_weight(2, "kg", "g")
        self.assertEqual(result, 2000)

    def test_convert_volume_l_to_ml(self):
        result = convert_volume(1, "l", "ml")
        self.assertEqual(result, 1000)

if __name__ == '__main__':
    unittest.main()