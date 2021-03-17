import definitions
import glob
import pathlib
import copy
from collections import defaultdict
from collections import OrderedDict
import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)  
import matplotlib.pyplot as plt
import seaborn as sns

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.figure_factory as ff

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc




def modifyMatrix(matrix): 
    for (key, value) in matrix.items():
        matrix = addChildToMatrix('class', key, matrix)
        matrix = removeChildFromMatrix('combos', key, matrix)
        print('program():', key,':', value)

def isBetSizeCriteriaMet(hero, useCase, betSize):
    #validates all betSizes are associated with a given use case, stack depth, position, and action
    if useCase in definitions.useCaseVizTypes['useCaseVariantDriven']:
        if useCase == definitions.betSizes[betSize]['parentUseCase']: 
            if hero['heroStackDepth'] in definitions.betSizes[betSize]['heroStackDepths']:
                if hero['heroPosition'] in definitions.betSizes[betSize]['heroPositions']:
                    if hero['heroAction'] in definitions.betSizes[betSize]['heroActions']:
                        if hero['heroUseCaseVariant'] in definitions.betSizes[betSize]['parentUseCaseVariants']:
                            return True
    else:
        if useCase == definitions.betSizes[betSize]['parentUseCase']: 
            if hero['heroStackDepth'] in definitions.betSizes[betSize]['heroStackDepths']:
                if hero['heroPosition'] in definitions.betSizes[betSize]['heroPositions']:
                    if hero['heroAction'] in definitions.betSizes[betSize]['heroActions']:
                        return True
    return False


def getBetSize(hero, useCase, sizeType):
    #validates if criteria is met to return a betsize; returns a specific bet size for the hero or the villain (counteredSize)
    for betSize in definitions.betSizes:
        if isBetSizeCriteriaMet(hero, useCase, betSize) is False:
            continue

        if sizeType == 'heroBetSize':
            if sizeType in definitions.betSizes[betSize]:
                print(f'getBetSize()-heroBetSize: {definitions.betSizes[betSize]["heroBetSize"]}')
                return definitions.betSizes[betSize]['heroBetSize'] 

        if sizeType == 'counteredSize':
            if sizeType in definitions.betSizes[betSize]:
                print(f'getBetSize()-counteredSize: {definitions.betSizes[betSize]["counteredSize"]}')
                return definitions.betSizes[betSize]["counteredSize"]


def getFiles(fileDirPattern):
    #grabs all files via recursion based on the directory pattern for a given use case
    #fileName includes its absolute path
    fileList = []
    for absoluteFileName in glob.iglob(fileDirPattern, recursive=True):
        fileList.append(absoluteFileName) 
        print(f'getFiles()-fileName: {absoluteFileName}')
    return fileList
    

def getHands(absoluteFileName):
    #extracts hands from a file and inserts them into a list; assumes ',' is always the delimeter
    handList = []
    with open(absoluteFileName, 'r') as reader:
        for line in reader:
            handList = line.split(definitions.delimiters['handListDelimiter'])
            print(f'getHands()-absoluteFileName: {absoluteFileName}')
            print(f'getHands()-handList: {handList}')
    return handList


def getFileAttribute(absoluteFileName, attribute):
    #extracts file name from the absolute file name
    if attribute == 'name':
        print(f'getFileAttribute()-{attribute}: {str(pathlib.Path(pathlib.Path(absoluteFileName).name).stem)}')
        return str(pathlib.Path(pathlib.Path(absoluteFileName).name).stem)

    #extracts file path from the absolute file name
    if attribute == 'path':
        print(f'getFileAttribute()-{attribute}: {str(pathlib.Path(absoluteFileName).parent)}')
        return str(pathlib.Path(absoluteFileName).parent)


def getHeroAttribute(fileAttribute, useCase, heroAttribute):    
    if heroAttribute == 'heroUseCaseVariant':
             if 'heroUseCaseVariants' not in definitions.preFlopUseCases[useCase]:
                return None


    for attribute in definitions.preFlopUseCases[useCase][heroAttribute + 's']:
        if heroAttribute == 'heroStackDepth':
            if attribute in fileAttribute:
                print(f'getHeroAttribute()-{heroAttribute}: {attribute}')
                return attribute

        if attribute == getFileNameComponent(fileAttribute, heroAttribute, useCase):
            print(f'getHeroAttribute()-{heroAttribute}: {attribute}')
            return attribute


def getFileNameComponent(fileName, fileNameComponent, useCase=None):
    #extracts the situational factors from the components of the file name
    fileNameComponents = fileName.split(definitions.delimiters['fileNameDelimiter'])
    if fileNameComponent == 'heroPosition':
        return fileNameComponents[definitions.components['heroPosition']]
    
    if fileNameComponent == 'heroUseCaseVariant':
        return fileNameComponents[definitions.components['heroUseCaseVariant']]

    if fileNameComponent == 'heroAction':
        if isUseCaseVariable(useCase):
            return fileNameComponents[definitions.components['heroAction']]
        else:
            return fileNameComponents[definitions.components['heroAction-alt']] 


def isUseCaseVariable(useCase):
    #determines if a use case has child use cases
    if 'heroUseCaseVariants' in definitions.preFlopUseCases[useCase]:
        return True
    else:
        return False


def offsuit(handRank): 
    #returns valid offsuit specification for an otherwise unspecified hand
    return handRank + definitions.handProperties['offsuit']


def suited(handRank): 
    #returns valid suited specification for an otherwise unspecified hand
    return handRank + definitions.handProperties['suited']


def buildUnspecifiedHandMatrix(handRank, discount=1):
    #gets offsuit and suited specification for an unspecified hand; calculates its combo frequencies; assigns its codes
    handMatrix = {
        offsuit(handRank): {
            'code': definitions.handMatrix[offsuit(handRank)]['code'],
            'combos': format(discount * definitions.handMatrix[offsuit(handRank)]['combos'], definitions.formats['comboFormat'])
            },
        
        suited(handRank): {
            'code': definitions.handMatrix[suited(handRank)]['code'],
            'combos': format(discount * definitions.handMatrix[suited(handRank)]['combos'], definitions.formats['comboFormat'])
            }
        } 
    return handMatrix


def buildSpecifiedHandMatrix(handRank, discount=1):
    #gets a specification for a specified hand; calculates its combo frequency; assigns its code
    handMatrix = {
        handRank : {
            'code': definitions.handMatrix[handRank]['code'],
            'combos': format(discount * definitions.handMatrix[handRank]['combos'], definitions.formats['comboFormat'])
            }
        } 
    
    return handMatrix


def buildNewMatrix(newMatrixType, newMatrix, sourceMatrixKey, sourceMatrix):
    #totals combo frequency for each distinct class
    if newMatrixType == 'handClass':
        for (handClassKey, handClassValue) in definitions.handClasses.items():
            if sourceMatrixKey in handClassValue['variants']:
                newMatrix = {
                    handClassKey: {
                    'combos': format(float(newMatrix[handClassKey]['combos']) + float(sourceMatrix[sourceMatrixKey]['combos']), definitions.formats['comboFormat'])
                    }
                }

    #must add filtering logic here to set combos to zero where filter applies for a given hand class or code

    if newMatrixType == 'handVariant': 
        handstring = newMatrix[sourceMatrix[sourceMatrixKey]['code']]['hands']
        #print('inside buildNewMatrix() ', sourceMatrixKey, '-', sourceMatrix[sourceMatrixKey]['combos'])


        handfrequency = format(float(sourceMatrix[sourceMatrixKey]['combos']) / float(definitions.handMatrix[sourceMatrixKey]['combos']), definitions.formats['frequencyFormat'])
        #print('inside buildNewMatrix() ', sourceMatrixKey, '-', str(handfrequency))
        #print('\n')

        newMatrix = {
            sourceMatrix[sourceMatrixKey]['code']: { 
                'combos': format(float(newMatrix[sourceMatrix[sourceMatrixKey]['code']]['combos']) + float(sourceMatrix[sourceMatrixKey]['combos']), definitions.formats['comboFormat']),
                'hands': str(newMatrix[sourceMatrix[sourceMatrixKey]['code']]['hands']) + cleanstring('hand', handstring) + str(sourceMatrixKey) + cleanstring('handfrequency', handfrequency),
                'name': definitions.handVariants[sourceMatrix[sourceMatrixKey]['code']] + ' (' + sourceMatrix[sourceMatrixKey]['code'] + ')',
                'property': ''
                }
            }

        propertystring = cleanstring('property', str(newMatrix[sourceMatrix[sourceMatrixKey]['code']]['hands']), str(newMatrix[sourceMatrix[sourceMatrixKey]['code']]['name']))

        newMatrix[sourceMatrix[sourceMatrixKey]['code']]['property'] = propertystring
            

    return newMatrix

def cleanstring(stringtype, string, optionalstring=''):
    if stringtype == 'hand':   
        if string == '':
            return ''
        else: 
            return ', '

    if stringtype == 'handfrequency':
        if string == '1.00': 
            return ''
        else:
            return '-' + string

    if stringtype == 'property': 
        if string == '':
            return ''
        else:
            return '<i>' + optionalstring + '</i><br><b>' + string + '</b>'

def getNewMatrix(newMatrixType, sourceMatrix):
    #creates and returns dictionary comprised of hands grouped by class whose combos are totaled
    if newMatrixType == 'handClass':
        newMatrix = copy.deepcopy(definitions.handClasses)
   
    if newMatrixType == 'handVariant':
        newMatrix = copy.deepcopy(definitions.handVariants)
    
        print('from getNewMatrix() before keys overwritten', newMatrix)

    for newMatrixKey in newMatrix.keys():
        newMatrix[newMatrixKey] = {'combos': '0.0', 'hands': '', 'name': definitions.handVariants[newMatrixKey] + ' (' + newMatrixKey + ')', 'property': ''}

    print('from getNewMatrix() after keys overwritten ', newMatrix)

    for sourceMatrixKey in sourceMatrix.keys():
        #must pass filter to buildNewMatrix for horizontal filtering
        newMatrix.update(buildNewMatrix(newMatrixType, newMatrix, sourceMatrixKey, sourceMatrix))        
        
    return newMatrix


def getFrequency(matrixType, matrix, horizontalfilter):
    baseMatrix = getBaseMatrix(matrixType)

    filterlist = []
    filterflag = False

    #print('horizontalfilter test #1 = ', horizontalfilter)


    # logic for when checklist is based on class
    '''
    if len(horizontalfilter) > 0:
        for classKey in horizontalfilter:
            for var in list(definitions.handClasses[classKey]['variants']):
                filterlist.append(var)
                filterflag = True
    '''

    # logic for when checklist is based on subclass
    if len(horizontalfilter) > 0:
        filterlist = horizontalfilter
        filterflag = True


    if filterflag == True:
        for key in matrix.keys(): 
            if key not in filterlist: 
                matrix[key]['combos'] = 0.0
                matrix[key]['hands'] = ''
                matrix[key]['name'] = ''
                matrix[key]['property'] = ''
            frequency = format(float(matrix[key]['combos']) / float(baseMatrix[key]['combos']), definitions.formats['frequencyFormat'])
            matrix.update(addFrequency(frequency, key, matrix))


    return matrix, filterlist


def getBaseMatrix(matrixType):
    if matrixType == 'handVariant':
        baseMatrix = getNewMatrix(matrixType, definitions.handMatrix)

    if matrixType == 'handClass':
        baseMatrix = getNewMatrix(matrixType, getNewMatrix('handVariant', definitions.handMatrix))
    return baseMatrix


def getTotalCombos(matrix):
    combos = 0.0
    for value in matrix.values():
        combos = combos + float(value['combos'])
    return combos


def addChildToMatrix(childKey, parentKey, matrix):
    if childKey == 'class':
        for (key, value) in definitions.handClasses.items():
            if parentKey in value['variants']: 
                matrix[parentKey][childKey] = key   

    return matrix

def removeChildFromMatrix(childKey, parentKey, matrix):
    del matrix[parentKey][childKey]
    return matrix


def addFrequency(frequency, key, matrix):
    matrix[key]['frequency'] = frequency
    return matrix
    
    
def getHandMatrix(hands, selected_hand, app_mode):
    #creates and returns dictionary comprised of discounted and undiscounted hands, whose frequencies are calculated and combos are assigned 
    handMatrix = {}
    

    if app_mode != 'sniper': 
        for hand in hands:
            if isHandDiscounted(hand):
                if(getDiscountedHandRank(hand) in definitions.handMatrix):
                    handMatrix.update(buildSpecifiedHandMatrix(getDiscountedHandRank(hand), getDiscount(hand)))
                else: 
                    handMatrix.update(buildUnspecifiedHandMatrix(getDiscountedHandRank(hand), getDiscount(hand)))

            if (isHandDiscounted(hand) is False):
                if(hand in definitions.handMatrix):
                    handMatrix.update(buildSpecifiedHandMatrix(hand))
                else: 
                    handMatrix.update(buildUnspecifiedHandMatrix(hand))

    if app_mode == 'sniper': 
        for hand in hands:
            
            # The hands extracted from the txt files do not specify suit when offsuit and suited are of equal frequency, so this IF accounts for that
            if definitions.delimiters['discountedHandDelimiter'] in hand and selected_hand[:-1] == hand.split(':',1)[0]:
                hand = selected_hand + definitions.delimiters['discountedHandDelimiter'] + hand.split(':',1)[1]
            
            # The hands extracted from the txt files do not specify suit when all 16 combos apply, so this IF accounts for that
            if selected_hand[:-1] == hand: 
                hand = selected_hand

            if selected_hand in hand: 
                if isHandDiscounted(hand):
                    if(getDiscountedHandRank(hand) in definitions.handMatrix):
                        handMatrix.update(buildSpecifiedHandMatrix(getDiscountedHandRank(hand), getDiscount(hand)))
                    else: 
                        handMatrix.update(buildUnspecifiedHandMatrix(getDiscountedHandRank(hand), getDiscount(hand)))

                if (isHandDiscounted(hand) is False):
                    if(hand in definitions.handMatrix):
                        handMatrix.update(buildSpecifiedHandMatrix(hand))
                    else: 
                        handMatrix.update(buildUnspecifiedHandMatrix(hand))

    return handMatrix


def isHandDiscounted(hand):
    #determines if a given hand is discounted
    if definitions.delimiters['discountedHandDelimiter'] in hand:
        return True
    else:
        return False


def getDiscountedHandRank(hand):
    #returns hand rank of a discounted hand
    if definitions.delimiters['discountedHandDelimiter'] in hand:
        handElementsList = hand.split(definitions.delimiters['discountedHandDelimiter'])
        return handElementsList[0] 


def getDiscount(hand):
    #returns the discount of the discounted hand
    if definitions.delimiters['discountedHandDelimiter'] in hand:
        handElementsList = hand.split(definitions.delimiters['discountedHandDelimiter'])
        return float(handElementsList[definitions.components['discount']])

def reorderUseCases(useCaseInventory): 
    return OrderedDict(sorted(useCaseInventory.items(), key=lambda i: (i[1]['heroAction'], i[1]['heroPosition'])))

def convertToDataFrame(matrix): 
    return pd.DataFrame.from_dict(matrix).transpose().reset_index().rename(columns={'index':'variant'})

def reorderColumns(df):
    return df[['class', 'variant', 'frequency', 'property']] 


def setDataFrame(useCase, useCaseMetaData): 
    tempDF = convertToDataFrame(useCaseMetaData['handVariantMatrix'])
    tempDF = reorderColumns(tempDF)
    tempDF['heroBetSize'] = useCaseMetaData['heroBetSize']
    tempDF['heroBetSize'] = tempDF['heroBetSize'].fillna('na')
    if useCase in definitions.useCaseVizTypes['useCaseVariantDriven']:
        tempDF['counteredSize'] = useCaseMetaData['counteredSize']
        tempDF['counteredSize'] = tempDF['counteredSize'].fillna('na')
    tempDF['heroPosition'] = useCaseMetaData['heroPosition']
    tempDF['heroAction'] = useCaseMetaData['heroAction']
    tempDF['heroStackDepth'] = useCaseMetaData['heroStackDepth']
    tempDF['frequency'] = pd.to_numeric(tempDF['frequency'], errors='coerce')

    if useCase in definitions.useCaseVizTypes['useCaseVariantDriven']:
        tempDF['heroUseCaseVariant'] = useCaseMetaData['heroUseCaseVariant']

    #enforces order of the x and y axis categorical data
    tempDF['heroStackDepth'] = pd.Categorical(tempDF['heroStackDepth'], definitions.preFlopUseCases[useCase]['heroStackDepths'])
    tempDF['class'] = pd.Categorical(tempDF['class'], definitions.handClasses)
    tempDF['heroPosition'] = pd.Categorical(tempDF['heroPosition'], definitions.preFlopUseCases[useCase]['heroPositions'])
    tempDF['variant'] = pd.Categorical(tempDF['variant'], definitions.handVariants)
    if useCase in definitions.useCaseVizTypes['useCaseVariantDriven']:
        tempDF['heroUseCaseVariant'] = pd.Categorical(tempDF['heroUseCaseVariant'], definitions.preFlopUseCases[useCase]['heroUseCaseVariants'])
    return tempDF

def get_vertical_segments(filterdict, useCase): 
    factors = []
    for filterlist in filterdict.values(): 
        if len(filterlist) > 0:
            for values in filterlist:
                factors.append(values)
    factors = str(factors)
    factors = factors.replace('[', '')
    factors = factors.replace(']', '')

    return factors

def get_horizontal_segments(filterdict):
    classsegments = []
    variantsegments = []
    if len(filterdict['classes']) > 0: 
        for value in filterdict['classes']:
            temp = value + ' ' + str(definitions.handClasses[value]['variants'])
            classsegments.append(temp)
    classsegments = str(classsegments)
    classsegments = classsegments.replace('[', '')
    classsegments = classsegments.replace(']', '')
    classsegments = classsegments.replace('\"', '')
   

    if len(filterdict['variants']) > 0: 
        for values in filterdict['variants']: 
            variantsegments.append(values)
    variantsegments = str(variantsegments)
    variantsegments = variantsegments.replace('[', '')
    variantsegments = variantsegments.replace(']', '')
   

    return classsegments, variantsegments

def find_key_for(input_dict, input_dict_key, nesteddictkey):    
    if nesteddictkey == 'variants':
        for k, v in input_dict.items():
            if input_dict_key in v[nesteddictkey]:
                return k

    if nesteddictkey == 'code':
        hands = []
        for k, v in input_dict.items():
            if input_dict_key in v[nesteddictkey]:
                hands.append(k)
        return hands



def df_to_plotly(df, dfsecondary, xvalues):
    classlist = []
    for handVariantKey in definitions.handVariants.keys():
        classlist.append('<b>' + str(find_key_for(definitions.handClasses, handVariantKey, 'variants')) + '</b>')

    return {'z': df.values.tolist(),
            'x': xvalues,
            'y': [classlist, df.index.tolist()],
            'text': dfsecondary.values.tolist(),
            #'hovertemplate': 
            #    '<b>%{text}</b><extra></extra>'
            
                } 
        
def getlegenddata(): 
    ann_text = []
    z = []

    classposition = 1
    for handVariantKey in definitions.handVariants.keys():
        handclass = str(find_key_for(definitions.handClasses, handVariantKey, 'variants'))
        if classposition in (1, 4, 10, 16, 22):
            ann_text.append([handclass, handVariantKey])
        else:   
            ann_text.append(['', handVariantKey])

        if handclass == 'Pair':
            z.append([5, 5])

        if handclass == 'Ace':
            z.append([4, 4])

        if handclass == 'Connector':
            z.append([3, 3])
        
        if handclass == 'Gapper Sr.':
            z.append([2, 2])

        if handclass == 'Gapper Jr.':
            z.append([1, 1])

        classposition = classposition + 1
    ann_text = ann_text[::-1]
    z = z[::-1]

    #print(z)

    return z, ann_text
            

def visualizelegend():
    ##### adding legend figure
  

    z, annotation_text = getlegenddata()
    fig = ff.create_annotated_heatmap(z, annotation_text=annotation_text, zmin=0, zmax=20, colorscale='greys')

    for i in range(len(fig.layout.annotations)):
        fig.layout.annotations[i].font.size = 10

    fig.layout.width = 275
    return fig



def visualizedatadash(dfList, useCase, mostOuterVariable, xtickDict, usecaseconfig): 
    tracename_list = []
    subplottitle = ''
    subplottitlelist = []
    specialformattingusecases = ('blindvsblind', 'vsOpen')

    for key in xtickDict.keys():
        if useCase not in specialformattingusecases: 
            subplottitle = '<b>' + key + '</b>'
        else:
            subplottitle = key
        subplottitlelist.append(subplottitle)

    #print('from visualizedatatemp()...xtickDict keys: ', xtickDict.keys())

    fig = make_subplots(rows=1, cols=len(dfList), shared_yaxes='rows', subplot_titles=subplottitlelist)

    fontsize = 0
    layoutfontsize = 10
    if useCase in specialformattingusecases:
        subplottitlefontsize = 9.5
    else: 
        subplottitlefontsize = layoutfontsize

    for i in fig['layout']['annotations']:
        i['font'] = dict(size=subplottitlefontsize, color='black')

    i = 0
    for df in dfList:
        opacity = 0 
        for col_data in df['frequency'].iteritems():
            if col_data[1] > 0.0:
                opacity = 1 
        
        #print('from visualizedatadash() \n', df)
        
        ##### coloring the heatmap
        subplotcolor = ''
        for actionKey, colorValue in definitions.preFlopUseCases[useCase]['subplotcolors'].items():
            columnHeader = list(xtickDict.keys())[i]
            chElements = columnHeader.split(definitions.delimiters['columnHeaderDelimiter']) 
            for chElement in chElements:          
                if actionKey == chElement:
                    subplotcolor = colorValue

        ##### getting the action before pivoting df
        #group = df['heroAction'].values[0]


        ##### creating the heatmap
        dfsecondary = df  
        df = df.pivot('variant', mostOuterVariable, 'frequency')
        dfsecondary = dfsecondary.pivot('variant', mostOuterVariable, 'property')
        #print('from visualizedatatemp()...', dfsecondary)
    
        tracename = '<b>' + str(list(xtickDict.keys())[i]) + '</b>'
        fig.add_trace(go.Heatmap(df_to_plotly(df, dfsecondary, list(xtickDict.values())[i]), zmin=0, zmax=1, colorscale=subplotcolor, name=tracename, opacity=opacity), row=1, col = i + 1)        
        
        if opacity == 1:
            tracename = tracename.replace('<b>', '').replace('</b>', '')
            tracename_list.append(tracename)

    
        ##### iterating through each data frame
        i = i + 1

    ##### displaying the map 

    #factors = get_vertical_segments(definitions.verticalfilter[usecaseconfig], useCase)
    #classes, variants = get_horizontal_segments(definitions.horizontalfilter)
    title = definitions.preFlopUseCases[useCase]['viztitle']

    #fig.update_layout(hovermode='x', autosize=True, title_text=title, plot_bgcolor='white', font_color='black', font_size=10, yaxis={'title': ''}, xaxis={'title': ''})
    fig.update_layout(hoverlabel=modifyhoverlabel(), title_x=0.5, hovermode='x',autosize=False, height=650, width=1500, title_text= '<b>' + title + '</b>', plot_bgcolor='white', font_color='black', font_size=layoutfontsize, yaxis={'title': ''}, xaxis={'title': ''})
    fig.update_yaxes(autorange='reversed', automargin=True, showspikes=True, spikemode='toaxis', spikethickness=.5, spikedash='dot', spikecolor='black')
    fig.update_xaxes(tickangle=-45, showspikes=True, spikemode='toaxis', spikethickness=.5, spikedash='dot', spikecolor='black')
    fig.update_traces(yaxis='y1', showscale=False, hoverinfo='text + x', xgap=0, ygap=0, showlegend=True)
    #fig.update_traces(showscale=False, hoverinfo='text + x', xgap=0, ygap=0, showlegend=True) 
    
   
    #fig.show(config={'displayModeBar': False, 'showTips': False})
    
    return fig, {'visibility':'visible'}, tracename_list, {}, {}, {}, {}


def modifyhoverlabel():
    return { 
        'font_size': 16,
        'align': 'left', 
        'bgcolor': 'black'
        } 


def getdatavizcontent(vizParams, useCase, useCaseInventory):
    attrList = list(vizParams.keys())
    firstAttribute = attrList[0]
    attrList.pop(0)
    attributes = tuple(attrList)
    currFilter = vizParams[firstAttribute]

    inventory = buildbyattribute(firstAttribute, attributes, currFilter, vizParams, useCase)
    print('\n')
    print('from getdatavizcontent() - inventory... ', inventory)
    print('\n')


    tempVizParams = vizParams.copy()
    vizParamsList = []

    for key in tempVizParams.keys():
        tempVizParams[key] = None

    for item in inventory: 
        vizParamsList, tempVizParams = setItem(item, tempVizParams, vizParamsList)
        #print(tempVizParams)
        #print('\n')
    print('from getdatavizcontent() vizParamsList...', vizParamsList)
    print('\n')
    
    df = pd.DataFrame()
    dfList = []
    xtickList = []
    xtickDict = defaultdict(dict)
    i =  0
    breakPoint = len(vizParamsList)
    for vizParamNode in vizParamsList: 
        i = i + 1
        #print(vizParamNode)


        df, dfList, xtickList, xtickDict, mostInnerVariables, mostOuterVariable = compareItems(useCaseInventory, vizParamNode, useCase, df, dfList, xtickList, xtickDict)
        if i == breakPoint:
            dfList.append(df)

            i = 0
            breakPoint = len(mostInnerVariables) - 1
            lastaddedval = ''
            #print('getdataframes mostinnervaraibles...', mostInnerVariables)
            for var in mostInnerVariables:
               
                if i == breakPoint: 
                    #print('getdataframes if (lastaddedval)...', lastaddedval)
                    lastaddedval = lastaddedval + df[var].iloc[-1]
                else: 
                    #print('getdataframes else (lastaddedval)...', lastaddedval)
                    lastaddedval = lastaddedval + df[var].iloc[-1] + '-' 
                i = i + 1 
            #print('getdataframes (lastaddedval)...', lastaddedval)
            xtickDict.update({lastaddedval : xtickList})
    inventory = inventory.clear()
    print(xtickDict)
    print('\n')
    return dfList, xtickDict, mostOuterVariable

def compareItems(useCaseInventory, vizParamNode, useCase, df, dfList, xtickList, xtickDict):

    setDataFrameFlag = False 
    
    
    mostOuterVariable = list(vizParamNode.keys())[-1][:-1]
    mostInnerVariables = []

    i = 0
    breakPoint = len(list(vizParamNode.keys())) - 1
    for param in vizParamNode.keys(): 
        if i == breakPoint: 
            continue
        else: 
            #print('param ', param)
            mostInnerVariables.append(param[:-1])
        i = i + 1
        

    for useCaseMetaData in useCaseInventory.values(): #refactor this to use keys instead
        
        for value in vizParamNode.values(): #refactor this to use keys instead
            if value in useCaseMetaData.values():
                setDataFrameFlag = True    
                #print('if...', setDataFrameFlag) 
            else: 
                setDataFrameFlag = False 
                #print('else...', setDataFrameFlag)
                break

                  
        if setDataFrameFlag == True: 
            i = 0
            breakPoint = len(list(vizParamNode.keys())) - 1
            groupByAttrs = []
            for key in vizParamNode.keys():
                i = i + 1 
                key = key[:-1] 
                groupByAttrs.append(key)
                if i == breakPoint:
                    break

            #print(groupByAttrs)
            
            if len(df) == 0:
                #print('df length = 0')
                df = df.append(setDataFrame(useCase, useCaseMetaData))
                #print('df...', df)

                label = useCaseMetaData[mostOuterVariable] + ' (' + str(useCaseMetaData['heroBetSize']) + ' ' +  str(useCaseMetaData['counteredSize']) + ')' + ',   ' + useCaseMetaData['overallFrequency']
                label = label.replace(' (None None)', '')
                label = label.replace(' (None)', '')
                label = label.replace('None', '')
                label = label.replace(' ()', '')
                label = label.replace('( ', '(')
                label = label.replace('()', '')
                label = label.replace(' )', ')')
                xtickList.append(label)
                
                return df, dfList, xtickList, xtickDict, mostInnerVariables, mostOuterVariable
            else: 
                #print('df length is > than 0')
                appendDFListFlag = False
                for attr in groupByAttrs: 
                    lastaddedValue = df[attr].iloc[-1]
                    if lastaddedValue == useCaseMetaData[attr]:
                        appendDFListFlag = True 
                    else: 
                        appendDFListFlag = False 
                        break
                
                #print('appendDFListFlag...', appendDFListFlag)
                if appendDFListFlag == True:
                    df = df.append(setDataFrame(useCase, useCaseMetaData))
                    label = useCaseMetaData[mostOuterVariable] + ' (' + str(useCaseMetaData['heroBetSize']) + ' ' + str(useCaseMetaData['counteredSize']) + ')' + ',   ' + useCaseMetaData['overallFrequency']
                    label = label.replace(' (None None)', '')
                    label = label.replace(' (None)', '')
                    label = label.replace('None', '')
                    label = label.replace(' ()', '')
                    label = label.replace('( ', '(')
                    label = label.replace('()', '')
                    label = label.replace(' )', ')')
                    xtickList.append(label)
                    return df, dfList, xtickList, xtickDict, mostInnerVariables, mostOuterVariable
                else:
                    i = 0
                    breakPoint = len(mostInnerVariables) - 1
                    lastaddedval = ''
                    for var in mostInnerVariables:
                        if i == breakPoint: 
                            lastaddedval = lastaddedval + df[var].iloc[-1]
                            #print('if...', lastaddedval)
                        else: 
                            lastaddedval = lastaddedval + df[var].iloc[-1] + '-' 
                            #print('else...', lastaddedval)
                        i = i + 1 

                    #print('lastaddedValue...', lastaddedval)

                    xtickDict.update({lastaddedval : xtickList})
                    xtickList = []
                    label = useCaseMetaData[mostOuterVariable] + ' (' + str(useCaseMetaData['heroBetSize']) + ' ' +  str(useCaseMetaData['counteredSize']) + ')' + ',   ' + useCaseMetaData['overallFrequency']
                    label = label.replace(' (None None)', '')
                    label = label.replace(' (None)', '')
                    label = label.replace('None', '')
                    label = label.replace(' ()', '')
                    label = label.replace('( ', '(')
                    label = label.replace('()', '')
                    label = label.replace(' )', ')')
                    xtickList.append(label)
                    #print('xtickList...', xtickList)
                    dfList.append(df)
                    df = pd.DataFrame()
                    df = df.append(setDataFrame(useCase, useCaseMetaData))
                    
                    return df, dfList, xtickList, xtickDict, mostInnerVariables, mostOuterVariable
    #print('generic return...')
    
    #return objects in same state if no conditions are true
    return df, dfList, xtickList, xtickDict, mostInnerVariables, mostOuterVariable

    

def setItem(item, tempVizParams, vizParamsList): 
    for key in tempVizParams.keys(): 
        if list(item.keys())[0] == key and tempVizParams[key] == None:
            tempVizParams[key] = item[key]

        #if key match betweens the temp node and the item, then if the node already has a value, check to see if it's the last key in the node
        if list(item.keys())[0] == key and tempVizParams[key] != None and list(item.keys())[0] == list(tempVizParams.keys())[-1]: 
            tempVizParamsCopy = tempVizParams.copy()
            tempVizParamsCopy.update({key : item[key]})
            vizParamsList.append(tempVizParamsCopy)
            return vizParamsList, tempVizParamsCopy

        #if key match betweens the temp node and the item, then if the node already has a value, check to see if it's NOT the last key in the node
        if list(item.keys())[0] == key and tempVizParams[key] != None and list(item.keys())[0] != list(tempVizParams.keys())[-1]: 
            tempVizParamsCopy = tempVizParams.copy()
            tempVizParamsCopy.update({key : item[key]})
            return vizParamsList, tempVizParamsCopy

    if None in tempVizParams.values():
        return vizParamsList, tempVizParams


def buildbyattribute(currAttribute, attributes, currFilter, vizParams, useCase, inventory=[]):

    # here is the code block that filters vertically - deprecate code since this functionality is replaced with logic that
    # mutes the vertical strip rather than removes it
    if len(currFilter) > 0: 
        items = currFilter
        print('items...', items)
    else: 
        items = definitions.preFlopUseCases[useCase][currAttribute]

    if len(attributes) > 0: 
        attrList = list(attributes)
        nextAttribute = attrList[0]
        attrList.pop(0)
        attributes = tuple(attrList)
        currFilter = vizParams[nextAttribute]

        for item in items:
            inventory.append({currAttribute : item})
            print('inner ', currAttribute + ' : ' + item)
            buildbyattribute(nextAttribute, attributes, currFilter, vizParams, useCase, inventory=inventory)
        
    else: 
        
        for item in items:
            inventory.append({currAttribute : item})
            print('outer ', currAttribute + ' : ' + item)
            
    return inventory


def mutecolumns(useCaseInventory, vertical_filter, usecaseconfig):
    #print('mutecolumns test #1 ', list(definitions.verticalfilter[usecaseconfig].values())[-1])
    #print('\n')
    #print('mutecolumns test #2 ', tuple(vertical_filter))

    s = set(list(definitions.verticalfilter[usecaseconfig].values())[-1]).symmetric_difference(vertical_filter)
    #print ('mute columns test #3 = ', s)
    if len(s) > 0:
        #print('mute columns test #4 passed')
        for (useCaseKey, useCaseNestedDicts) in useCaseInventory.items():
            for (useCaseNestedDictKey, useCaseNestedDictValue) in useCaseNestedDicts.items():
                for var in s: 
                    if var == useCaseNestedDictValue:
                        #print('mutecolumns condition passed')
                        for value in useCaseNestedDicts['handVariantMatrix'].values():
                            value['frequency'] = '0.00' 
                            value['hands'] = ''
                            value['property'] = ''
                        useCaseNestedDicts['overallFrequency'] = '0.00'
    return useCaseInventory

def get_test_answers(useCaseInventory, selected_column, selected_x_value, yaxis_variables, usecaseconfig, trace_data_state):
    #print('from get test answers - selected column = ', selected_column)
    #print('from get test answers - selected x value = ', selected_x_value)
    #print('from get test answers - y axis variables = ', yaxis_variables)
    #print('from get test answers - usecaseconfig = ', usecaseconfig)
    
    var_dict = {}

    var_string = selected_column + '-' + str(selected_x_value[0])
    if '40-50BB' in var_string:
        var_string = var_string.replace('40-50BB', '40$50BB')
        #print('var string 50 = ', var_string)
    if '60-100BB' in var_string:
        var_string = var_string.replace('60-100BB', '60$100BB')
        #print('var string 60 = ', var_string)

    var_list = var_string.split(definitions.delimiters['columnHeaderDelimiter'])
    #print('var list = ', var_list)

    var_list = [var.replace('$', '-') for var in var_list]


    #print('from get test answers - var list = ', var_list)


    for key in definitions.verticalfilter[usecaseconfig].keys(): 
        var_dict.update({key[:-1] : var_list[0]})
        var_list.pop(0)
    #print('from get test answers - var dict = ', var_dict)
    
    correct_action = ''
    correctUseCaseDict = {}
    red_flag = False
    for useCase_dict in useCaseInventory.values(): 
        for var_key, var_value in var_dict.items():
            print('useCase_dict[var_key] =', useCase_dict[var_key], 'and var_value = ', var_value)
            if useCase_dict[var_key] != var_value:
                red_flag = True 
                break
            else: 
                red_flag = False
                if var_key == 'heroAction':
                    correct_action = useCase_dict[var_key]
                continue
        if red_flag is False:
            print('red_flag is False')
            #print('correctUseCaseDict = ', correctUseCaseDict)
            correctUseCaseDict = useCase_dict.copy()
            break 

    print('correct action = ', correct_action)

    handVariantMatrix = correctUseCaseDict['handVariantMatrix'].copy()
    for hand_class in correctUseCaseDict['handVariantMatrix'].keys(): 
        if hand_class not in yaxis_variables: 
            del handVariantMatrix[hand_class]


    answerVariantMatrix = {}
    for hand_class, hand_class_dict in handVariantMatrix.items():
        answerVariantMatrix.update({hand_class : {'hands':  hand_class_dict['hands'].split(definitions.delimiters['handListDelimiter'])}})

    answerVariantMatrixCleaned = {}
    for hand_class, hand_class_dict in answerVariantMatrix.items():
        ls = [hand.replace(' ', '') for hand in hand_class_dict['hands']] 
        hand_frequency = 0.00 

        for hand in ls: 
            if '-' in hand: 
                extracted_freq = format(float(hand.split('-',1)[1]), definitions.formats['frequencyFormat'])
                extracted_freq = float(extracted_freq)
                hand_frequency = hand_frequency + extracted_freq
            elif hand_class_dict['hands'] == ['']: 
                continue
            else:
                hand_frequency = hand_frequency + 1.00

        num_of_hands = len(find_key_for(definitions.handMatrix, hand_class, 'code'))
        num_of_hands = format(float(num_of_hands), definitions.formats['frequencyFormat'])
        num_of_hands = float(num_of_hands)
        frequency = format(hand_frequency/ num_of_hands, definitions.formats['frequencyFormat'])
        frequency = float(frequency)
        answerVariantMatrixCleaned.update({hand_class : {'hands': ls, 'frequency': frequency, 'frequency_ui': check(frequency)}})

    print('from get test answers - test answers = ', answerVariantMatrixCleaned)

    sorted_yaxis_variables = []
    for key in definitions.handVariants.keys():
        if key in yaxis_variables: 
            sorted_yaxis_variables.append(key)

    return {}, {'display':'none'}, trace_data_state, sorted_yaxis_variables, answerVariantMatrixCleaned, var_string, correct_action

def check(value):
    value = float(value)
    if value == 0.00:
        return 'na'
    if 0.01 <= value <= 0.30:
        return 'low'  
    if 0.31 <= value <= 0.60:
        return 'medium'
    if 0.61 <= value <= 0.99:
        return 'high'
    if value == 1.00:
        return 'pure'

def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
              return i
    return -1