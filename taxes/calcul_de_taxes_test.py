import unittest
from calcul_de_taxes import *

class TestCalculDeTaxes(unittest.TestCase):
  def test_cart(self):
    # Test if the cart input by user is of type list
    cart = get_products_from_user()
    self.assertIsInstance(cart, list)

    # Test if cart has at least one item
    item_count = len(cart)
    self.assertGreater(item_count, 0)

  def test_parse_cart_item(self):
    # Test if the cart is parsed correctly as expected

    self.assertDictEqual(parse_cart_item('1 livre à 12.49'), {
      'qty': 1,
      'desc': 'livre',
      'price': 12.49,
      'imported' : False,
      'vat_applies' : False
    })
    self.assertDictEqual(parse_cart_item('1 CD musical à 14.99'), {
      'qty': 1,
      'desc': 'CD musical',
      'price': 14.99,
      'imported' : False,
      'vat_applies' : True
    })
    self.assertDictEqual(parse_cart_item('1 barre de chocolat à 0.85'), {
      'qty': 1,
      'desc': 'barre de chocolat',
      'price': 0.85,
      'imported' : False,
      'vat_applies' : False
    })
    self.assertDictEqual(parse_cart_item('1 boîte de chocolats importée à 10.00'), {
      'qty': 1,
      'desc': 'boîte de chocolats importée',
      'price': 10.00,
      'imported' : True,
      'vat_applies' : False
    })
    self.assertDictEqual(parse_cart_item('1 flacon de parfum importé à 47.50'), {
      'qty': 1,
      'desc': 'flacon de parfum importé',
      'price': 47.50,
      'imported' : True,
      'vat_applies' : True
    })
    self.assertDictEqual(parse_cart_item('1 boîte de pilules contre la migraine à 9.75'), {
      'qty': 1,
      'desc': 'boîte de pilules contre la migraine',
      'price': 9.75,
      'imported' : False,
      'vat_applies' : False
    })

  def test_round_taxes(self):
    # Test if first param is rounded up to the second param
    # We assume the function is always passed a float or int
    self.assertAlmostEqual(round_taxes(15, 0.05), 15)
    self.assertAlmostEqual(round_taxes(14.98, 0.05), 15)
    self.assertAlmostEqual(round_taxes(15.07, 0.05), 15.1)
    self.assertAlmostEqual(round_taxes(10.43, 0.05), 10.45)
    self.assertAlmostEqual(round_taxes(3.52, 0.05), 3.55)

    self.assertAlmostEqual(round_taxes(3.52, 0.15), 3.6)
    self.assertAlmostEqual(round_taxes(4.18, 0.5), 4.5)
