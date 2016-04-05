import unittest
from gc_calc import gc

class GcTests(unittest.TestCase):
    def test_gc(self):
        self.assertEqual(gc('ACTG'), 0.5)

    def test_long(self):
        self.assertAlmostEqual(gc('ACTGCAGATCTGAAATTCAGTAAGGG'), 0.4230769)
    def test_empty(self):
        self.assertRaises(TypeError, gc, )

if __name__ == '__main__':
    unittest.main()
