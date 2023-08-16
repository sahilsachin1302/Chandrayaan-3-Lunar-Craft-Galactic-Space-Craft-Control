import unittest
from galactic_spacecraft import GalacticSpaceCraft

class TestGalacticSpaceCraft(unittest.TestCase):
    def test_basic_movement(self):
        spacecraft = GalacticSpaceCraft(0, 0, 0)

        spacecraft.execute_commands(['f', 'f', 'b', 'l', 'r', 'r', 'b'])
        final_position, final_direction = spacecraft.get_position_and_direction()

        self.assertEqual(final_position, (0, 1, 0))
        self.assertEqual(final_direction, 'N')

    def test_turning(self):
        spacecraft = GalacticSpaceCraft(0, 0, 0)

        spacecraft.execute_commands(['r', 'r', 'r', 'l', 'l'])
        final_position, final_direction = spacecraft.get_position_and_direction()

        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, 'N')

    def test_up_down_movement(self):
        spacecraft = GalacticSpaceCraft(0, 0, 0)

        spacecraft.execute_commands(['u', 'u', 'd', 'd'])
        final_position, final_direction = spacecraft.get_position_and_direction()

        self.assertEqual(final_position, (0, 0, 0))
        self.assertEqual(final_direction, 'N')

    def test_complex_movement(self):
        spacecraft = GalacticSpaceCraft(0, 0, 0)

        spacecraft.execute_commands(['f', 'r', 'u', 'b', 'l'])
        final_position, final_direction = spacecraft.get_position_and_direction()

        self.assertEqual(final_position, (0, 1, -1))
        self.assertEqual(final_direction, 'N')


if __name__ == '__main__':
    unittest.main()
