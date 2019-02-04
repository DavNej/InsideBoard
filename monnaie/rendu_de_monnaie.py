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
  def __init__(self):
    self.coin2 = None
    self.bill5 = None
    self.bill10 = None

    try:
      self.TOTAL_AMOUNT = int(argv[1])
    
    except IndexError as err:
      logger.warn(err)
      logger.warn('No amount was entered')
      self.getAnInt()

    except ValueError as err:
      logger.warn(f'Amount entered was not an int - {err}')
      self.getAnInt()

  def getAnInt(self):
    self.TOTAL_AMOUNT = None
    while not isinstance(self.TOTAL_AMOUNT, int):
      print('Veuillez entrer une somme (en chiffre)')
      try:
        self.TOTAL_AMOUNT = int(input())
      except ValueError as err:
        logger.warn(f'Amount entered was not an int - {err}')
        self.getAnInt()



def main():
  change = Change()

if __name__ == '__main__':
  main()