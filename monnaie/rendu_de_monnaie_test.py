import unittest
from rendu_de_monnaie import Change

class TestChange(unittest.TestCase):
  def test_init(self):
    # Test init function of the Change class
    change = Change()
    self.assertIs(change.bill10, 0)
    self.assertIs(change.bill5, 0)
    self.assertIs(change.coin2, 0)

  def test_amout_to_change(self):
    # Test if input is of type int greater than 0
    change = Change()
    change.ask_amount_to_change()
    self.assertIsInstance(change.TOTAL_AMOUNT, int)
    self.assertGreaterEqual(change.TOTAL_AMOUNT, 0)

  def test_get_the_change(self):
    # Test some change cases
    # change = Change()
    pass
