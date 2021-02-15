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

app = dash.Dash(__name__)
app.layout = html.Div([

    html.Div([

        dcc.Dropdown(
            id='usecase',
            options=[{'label': usecase, 'value': usecase} for usecase in definitions.verticalfilter.keys()],
            value='RFI-linear', 

        ),

        html.Br(),

    ], style={'width': '15%', 'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial'}),


    html.Div([
        html.Div([
            html.P('Hand Classes: ')
        ], style={'display': 'inline-block'}),

        html.Div([
            dcc.Checklist(
                id='class',
                options=[{'label': handclass, 'value': handclass} for handclass in definitions.handClasses.keys()],
                value=list(definitions.handClasses.keys()),
            ),
        ], style={'display': 'inline-block'}),

    ], style={'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial'}),

    html.Div([
        html.Div([
            html.P(id='variable')
        ], style={'display': 'inline-block'}),

        html.Div([
            dcc.Checklist(
                id='vertical_filter',
                value=[]
            ),
        ], style={'display': 'inline-block'}),

    ], style={'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial'}), 

    dcc.Graph(
        id='graph',
        config={'displayModeBar': False, 'showTips': False},
        #figure=fig
    ), 

    html.Span('test', id='tooltip-target'),
    dbc.Tooltip('hover text', target='tooltip-target')
])


@app.callback(
    Output('vertical_filter', 'options'),
    Output('variable', 'children'),
    Input('usecase', 'value'))
def setverticalfilter(selected_usecase):
    variable_list = []
    print('selected_usecase= ', selected_usecase)
    last_element = list(definitions.verticalfilter[selected_usecase].keys())[-1] 

    for key in definitions.preFlopUseCases.keys():
        #print('substring =', key, ' string =', selected_usecase)
        
        if key in selected_usecase:
            print('substring condition passed')
            variable_list = list(definitions.verticalfilter[selected_usecase].values())[-1]

    #print('variable_list= ', variable_list)    
    #print('last_element = ', last_element)
    if 'StackDepth' in last_element:  
        return [{'label': element.replace('BB', 'bb'), 'value': element} for element in variable_list], definitions.variableUINames[last_element] + ': '
    else:
        return [{'label': element, 'value': element} for element in variable_list], definitions.variableUINames[last_element] + ': '


@app.callback(
    Output('vertical_filter', 'value'), 
    Input('vertical_filter', 'options'))
def set_variable_value(variable_dict):
    variable_list = []
    for variable in variable_dict:
        print('for testing...= ', variable)
        variable_list.append(variable['value'])
    return variable_list


@app.callback(
    Output('graph', 'figure'), 
    [Input('class', 'value')])
def updateheatmap(filteredlist): 

    useCase = 'BBdefends'
    config = ''

    if config == '':
        usecaseconfig = useCase 
    else: 
        usecaseconfig = useCase + '-' + config

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
    
    dfList, xtickDict, mostOuterVariable = functions.getdatavizcontent(definitions.verticalfilter[usecaseconfig], useCase, useCaseInventory) 

    for df in dfList:
        #df['frequency'] = np.where(df['class'] != 'The Ringer', 0.0, df['frequency'])
        print(df)
        print('\n')

    #functions.visualizedata(dfList, useCase, mostOuterVariable, xtickDict, filterlist, config)
    #functions.visualizedatatemp(dfList, useCase, mostOuterVariable, xtickDict, config)
        # visualizedatatemp does not use 'filterlist' (only visualize data)
    #functions.visualizelegend()


        
    return functions.visualizedatadash(dfList, useCase, mostOuterVariable, xtickDict, filteredlist, usecaseconfig)

if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
