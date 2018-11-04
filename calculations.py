import random
import numpy as np


class RandPop:
    def Pop(self):
        x = random.randrange(0, 100, 1)

        if x < 5:
            return True
        else:
            return False

