import numpy as np 
import pandas as pd 

import headerService

fileName = 'TAB_test_mogenis_2_2019-08-14-160715176 5.tsv'
fileFolder = '/Users/connor/Documents/Projecten/Pointing/sprint141/'
filePath = fileFolder + fileName

print('--- load data ' + fileName + ' ---')

header = headerService.readOpenClinHeaderData(filePath)

headerService.printHeaderData(header)