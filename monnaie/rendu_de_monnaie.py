from sys import argv
import logging

#Create and configure the logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
  filename='./rendu_de_monnaie.log',
  level = logging.DEBUG,
  format = LOG_FORMAT,
  filemode = 'w')  
logger = logging.getLogger()

#Test logger
logger.info('Program started')

class Change():
  def __init__(self, coin2=0, bill5=0, bill10=0):
      self.coin2 = coin2
      self.bill5 = bill5
      self.bill10 = bill10
    

  def __str__(self):
    return """
    {0} pièces de 2 euros
    {1} billet(s) de 5 euros
    {2} billet(s) de 10 euros
    """.format(self.coin2, self.bill5, self.bill10)


  def ask_amount_to_change(self):
    try:
      self.TOTAL_AMOUNT = abs(int(argv[1]))
    except IndexError as err:
      logger.warning(err)
      logger.warning('No arg was entered at program launch - {}'.format(err))
      self.get_an_int()
    except ValueError as err:
      logger.warning('Amount entered was not an int - {}'.format(err))
      self.get_an_int()
    self.spare = self.TOTAL_AMOUNT


  def get_an_int(self):
    self.TOTAL_AMOUNT = None
    while not isinstance(self.TOTAL_AMOUNT, int):
      print('Veuillez entrer une somme (en chiffre entier)')
      try:
        self.TOTAL_AMOUNT = abs(int(input()))
      except ValueError as err:
        logger.warning('Amount entered was not an int - {}'.format(err))
        self.get_an_int()
  

  def get_the_change(self):
    if (self.spare == 0):
      # opt_chg = Change(coin2=self.coin2, bill5=self.bill5, bill10=self.bill10)
      # print(opt_chg)
      return
    
    elif (self.spare == 1 and self.TOTAL_AMOUNT > 1):
      print('Désolé mais la machine ne peut rendre l\'appoint, vous perdez 1€')
      # opt_chg = Change(coin2=self.coin2 + 1, bill5=self.bill5, bill10=self.bill10)
      # print(opt_chg)
      return
    
    elif (self.spare == 1):
      print('Impossible de rendre la monnaie')
      return None

    else:
      # 10 bills
      if ( self.spare >= 10 ):
        self.spare = self.TOTAL_AMOUNT % 10
        self.bill10 = int((self.TOTAL_AMOUNT - self.spare) / 10)
        self.get_the_change()
      
      # 5 bills
      elif ( self.spare in [5, 7, 9]):
        self.bill5 = 1
        self.spare -= 5
        self.get_the_change()

      # 2 coins
      else:
        self.coin2 = int((self.spare - (self.spare % 2)) / 2)
        self.spare = self.spare % 2
        self.get_the_change()
    

def optimal_change():
  change = Change()
  change.ask_amount_to_change()
  change.get_the_change()
  print(change)
  return change

if __name__ == '__main__':
  optimal_change()