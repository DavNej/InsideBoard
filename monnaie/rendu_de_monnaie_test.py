import unittest
from rendu_de_monnaie import Change

class TestChange(unittest.TestCase):
  def test_init(self):
    # Test init function of the Change class
    change = Change()
    self.assertIs(change.bill10, None)
    self.assertIs(change.bill5, None)
    self.assertIs(change.coin2, None)
    self.assertIsInstance(change.TOTAL_AMOUNT, int)