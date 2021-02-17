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
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)
app.layout = html.Div([

    html.Div([
        html.Button(id='submit-button-state', n_clicks=0, children= 'Update Chart'),
    ], style={'width': '8%', 'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial', 'display':'inline-block', 'vertical-align': 'top'}),


    html.Div([
        html.Div([
            dcc.Dropdown(
                id='usecases',
                options=[{'label': usecase, 'value': usecase} for usecase in definitions.verticalfilter.keys()],
                value='RFI-polar',
                clearable=False 
            ),
            
        ], style={'width': '80%'}),

    ], style={'width': '16%', 'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial', 'display':'inline-block', 'vertical-align': 'top'}),


    html.Div([

        html.Div([
            html.Div([
                html.P('Classes: ')
            ], style={'display': 'inline-block'}),

            html.Span(id='class_error_message', style={'color' : 'red'}),

            html.Div([
                dcc.Checklist(
                    id='handsubclasses',
                    options=[{'label': handsubclass, 'value': handsubclass} for handsubclass in definitions.handVariants.keys()],
                    value=list(definitions.handVariants.keys()),
                ),
            ], style={'display': 'inline-block'}),
        ]),

        html.Div([
            html.Div([
                html.P(id='variable_name')
            ], style={'display': 'inline-block'}),

            html.Span(id='variable_error_message', style={'color' : 'red'}),

            html.Div([
                dcc.Checklist(
                    id='xaxis_variables',
                    value=[]
                ),
            ], style={'display': 'inline-block'}),
        ]),

    ], style={'width': '76%', 'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial', 'display':'inline-block','vertical-align': 'top'}), 



    dcc.Graph(
        id='graph',
        config={'displayModeBar': False, 'showTips': False},
        #figure=fig
    ), 

    #html.Span('test', id='tooltip-target'),
    #dbc.Tooltip('hover text', target='tooltip-target')
])

@app.callback(
    Output('class_error_message', 'children'),
    Input('handsubclasses', 'value'))   
def send_error_message(handsubclasses):
    if len(handsubclasses) == 0: 
        return ' ...Select at least one Hand Class... '
    else: 
        return ''
    

@app.callback(
    Output('variable_error_message', 'children'),
    Input('xaxis_variables', 'value'),
    Input('variable_name', 'children'))   
def send_error_message(xaxis_variables, variable_name):
    if len(xaxis_variables) == 0: 
        return ' ...Select at least one of the' + variable_name + ' ... '
    else: 
        return ''

@app.callback(
    Output('submit-button-state', 'disabled'),
    Input('handsubclasses', 'value'),
    Input('xaxis_variables', 'value'))
def set_button_enabled_state(handsubclasses, xaxis_variables):
    if len(handsubclasses) == 0 or len(xaxis_variables) == 0:
        return True 
    else:
        return False

@app.callback(
    Output('xaxis_variables', 'options'),
    Output('variable_name', 'children'),
    Input('usecases', 'value'))
def set_variable_options(selected_usecase):
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
    Output('xaxis_variables', 'value'), 
    Input('xaxis_variables', 'options'))
def set_variable_value(variable_dict):
    variable_list = []
    for variable in variable_dict:
        #print('for testing...= ', variable)
        variable_list.append(variable['value'])
    return variable_list

@app.callback(
    Output('graph', 'figure'),
    Input('submit-button-state', 'n_clicks'),
    State('usecases', 'value'),
    State('handsubclasses', 'value'),
    State('xaxis_variables', 'value'), prevent_initial_call=True)
def render_heatmap(n_clicks, usecaseconfig, handsubclasses, xaxis_variables): 
    if len(handsubclasses) == 0 or len(xaxis_variables) == 0:
        raise PreventUpdate
   
    #print('xaxis_variables = ', xaxis_variables)
    useCase = ''

    ##### derive abstract use case from specific use case
    for key in definitions.preFlopUseCases.keys():
        if key in usecaseconfig:
            useCase = key 

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
        hero['handVariantMatrix'], filterlist = functions.getFrequency('handVariant', hero['handVariantMatrix'], handsubclasses)
        for (key, value) in hero['handVariantMatrix'].items():
            print('program() - after getFrequency() executed:', key,':', value)

        print('\n')

        hero['overallFrequency'] = format(float(functions.getTotalCombos(hero['handVariantMatrix'])) / float(functions.getTotalCombos(functions.getBaseMatrix('handVariant'))), definitions.formats['frequencyFormat'])
        print('program()-overall frequency:', hero['overallFrequency'])

        print('\n')

        functions.modifyMatrix(hero['handVariantMatrix'])

        print('\n')
        
        useCaseInventory.update({ absoluteFileName : hero })

    useCaseInventory.update(functions.mutecolumns(useCaseInventory, xaxis_variables, usecaseconfig))

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


    #functions.visualizelegend()


        
    return functions.visualizedatadash(dfList, useCase, mostOuterVariable, xtickDict, usecaseconfig)


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
