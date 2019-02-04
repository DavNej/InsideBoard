import logging
from math import ceil, floor

"""
Inputs are assumed to be entered correctly. Error cases are not handled but can be with try except statements.
"""

#Create and configure the logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
  filename='./calcul_de_taxes.log',
  level = logging.DEBUG,
  format = LOG_FORMAT,
  filemode = 'w')  
logger = logging.getLogger()

#Test logger
logger.info('Program started')

# Program Params
VAT = 10
IMPORT_TAX = 5
ROUND_TAXES_TO = 0.05
VAT_FREE_ITEMS = [
  'livre',
  'livres',
  'barre de chocolat',
  'barres de chocolat',
  'boîte de pilules contre la migraine',
  'boîtes de pilules contre la migraine',
  'boîte de chocolats', 'boîtes de chocolats']

logger.info('Constants are set')


def get_products_from_user():
  """
  Ask user for the content of his cart and return a list
  """
  print('\nEntrer le contenu du panier en validant chaque article par "Entrer".')
  print('---- Laisser le champ vide marque la fin du panier ----\n')

  end = False
  cart = []

  while end is False:
    item = input()
    if item == "":
      end = True
      logger.info('End of cart input by user')
      break

    # item = check_input(item)
    cart.append(item)
  
  item_count = len(cart)
  print(f'Le panier contient {item_count} articles')

  if item_count == 0:
    print("Merci d'entrer au moins un article")
    get_products_from_user()
  
  logger.info('Cart input done')
  return cart


def check_input(input):
  """
  A good thing would be to check if the input is what we truly expect
  """
  pass


def parse_cart_item(cart_item):
  """
  Parse standardized input cart_item into dict
  """
  cart_item = cart_item.strip().split()
  
  output = {
    'qty': int(cart_item[0]),
    'desc': '',
    'price': None,
    'imported' : False,
    'vat_applies' : True
  }

  cart_item = cart_item[1:]

  output['price'] = float(cart_item[-1])
  cart_item = cart_item[:-2]

  if 'import' in cart_item[-1]:
    output['imported'] = True
    imported = cart_item[-1]
  else:
    imported = ''


  output['desc'] = ' '.join(cart_item)

  if output['desc'].replace(imported, '').strip() in VAT_FREE_ITEMS:
    output['vat_applies'] = False

  return output


def round_taxes(val, roundup_to):
  """
  Return float rounded up to the value passed as parameter
  """
  return ceil(val/roundup_to) * roundup_to


def eval_VAT(product_price):
  """
  Return VAT value of a number as float
  """
  return round_taxes(product_price * VAT / 100, ROUND_TAXES_TO)


def eval_import_tax(product_price):
  """
  Return import tax value of a number as float
  """
  return round_taxes(product_price * IMPORT_TAX / 100, ROUND_TAXES_TO)


def eval_taxes(product_dict):
  """
  Return the total taxes value of a product
  """
  taxes = 0

  if product_dict['vat_applies']:
    taxes += eval_VAT(product_dict['price'])

  if product_dict['imported']:
    taxes += eval_import_tax(product_dict['price'])
    
  return taxes


def print_bill(cart):
  """
  Print each product on a new line with its full price.
  Print total taxes value and total price
  """

  taxes = 0
  total = 0

  print("""
---------------------
       FACTURE       
---------------------\n""")

  for item in cart:
    taxes += eval_taxes(item)
    full_price = floor(eval_taxes(item) * 100) / 100 + item['price']
    total += item['price']
    print(item['qty'], item['desc'], ':', '%.2f' % full_price)

  print('\nMontant des taxes :', '%.2f' % taxes)
  print('Total :', '%.2f' % total)

def main():
  cart = get_products_from_user()
  
  cart = [ parse_cart_item(item) for item in cart ]
  logger.info('Cart parsed successfully')

  print_bill(cart)

if __name__ == '__main__':
  main()
  