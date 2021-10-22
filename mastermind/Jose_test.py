
import random
def _prepare(self):
          # """sets up the number to be guessed and places it in the list _numbers"""
          numbers = []
          for i in range(4):
                    numbers.append(random.randint(1,20))
          return numbers
master_list = _prepare(5)
print(master_list)