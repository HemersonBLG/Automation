"""
from random import randrange

date = str(randrange(1, 30)) + '/' + str(randrange(1, 12)) + '/' + str(randrange(1990, 2019))

print(date)

########################################################################################################################

import random
import time


def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%d/%m/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate


print("Random Date = ", getRandomDate("20/2/2019", "1/03/2019"))

########################################################################################################################

from random import randrange
faturamentoAnual = randrange(25000, 95000)
faturamentoMensal = faturamentoAnual/12
print(f'{faturamentoAnual:.2f}')
print(f'{faturamentoMensal:.2f}')

"""