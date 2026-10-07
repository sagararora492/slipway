import unittest

import slipway


class PackageTest(unittest.TestCase):
    def test_version(self):
        self.assertEqual(slipway.__version__, "0.0.0")


if __name__ == "__main__":
    unittest.main()
