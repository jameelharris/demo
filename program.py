import definitions
import functions
import copy
import pandas as pd
import matplotlib.pyplot as plt
from itertools import groupby
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


useCase = 'sqz'
config = ''

files = functions.getFiles(definitions.preFlopUseCases[useCase]['fileDirPattern'])
print('\n')

useCaseInventory = {}   

for absoluteFileName in files:

    hands = functions.getHands(absoluteFileName)
    print('\n')
    filePath = functions.getFileAttribute(absoluteFileName, 'path')
    fileName = functions.getFileAttribute(absoluteFileName, 'name')
    
    hero = {
        'heroStackDepth': functions.getHeroAttribute(filePath, useCase, 'heroStackDepth'),
        'heroPosition': functions.getHeroAttribute(fileName, useCase, 'heroPosition'),
        'heroAction': functions.getHeroAttribute(fileName, useCase, 'heroAction'),
        'heroUseCaseVariant': functions.getHeroAttribute(fileName, useCase, 'heroUseCaseVariant'),
        }

    hero['heroBetSize'] = functions.getBetSize(hero, useCase, 'heroBetSize')
    
    if hero['heroBetSize'] == None and hero['heroAction'] == 'open':
        hero['heroBetSize'] = definitions.preFlopUseCases[useCase]['defaultOpenSize']
    
    hero['counteredSize'] = functions.getBetSize(hero, useCase, 'counteredSize')
    
    print('\n')

    
    hero['handVariantMatrix'] = functions.getNewMatrix('handVariant', functions.getHandMatrix(hands))
    for (key, value) in hero['handVariantMatrix'].items():
        print('program() - after getNewNatrix() executed:', key,':', value)

    print('\n')

    #must pass filter to getNewMatrix for horizontal filtering
    hero['handVariantMatrix'], filterlist = functions.getFrequency('handVariant', hero['handVariantMatrix'], definitions.horizontalfilter)
    for (key, value) in hero['handVariantMatrix'].items():
        print('program() - after getFrequency() executed:', key,':', value)

    print('\n')

    hero['overallFrequency'] = format(float(functions.getTotalCombos(hero['handVariantMatrix'])) / float(functions.getTotalCombos(functions.getBaseMatrix('handVariant'))), definitions.formats['frequencyFormat'])
    print('program()-overall frequency:', hero['overallFrequency'])

    print('\n')

    functions.modifyMatrix(hero['handVariantMatrix'])

    print('\n')
    
    useCaseInventory.update({ absoluteFileName : hero })

#useCaseInventory.update(functions.mutecolumns(useCaseInventory))

for (key, value) in useCaseInventory.items():
    print('program():', key,':', value)
    print('\n')



'''
orderedUseCaseInventory = functions.reorderUseCases(useCaseInventory)


print('\n THE ORDERED USE CASE INVENTORY \n')

for (key, value) in orderedUseCaseInventory.items():
    print('program():', key,':', value)
    print('\n')
'''
if config == '':
    usecaseconfig = useCase 
else: 
    usecaseconfig = useCase + '-' + config
dfList, xtickDict, mostOuterVariable = functions.getdatavizcontent(definitions.verticalfilter[usecaseconfig], useCase, useCaseInventory) 

for df in dfList:
    #df['frequency'] = np.where(df['class'] != 'The Ringer', 0.0, df['frequency'])
    print(df)
    print('\n')

functions.visualizedata(dfList, useCase, mostOuterVariable, xtickDict, filterlist, config)



    