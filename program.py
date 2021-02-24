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

import base64


usecaselog = ['',]
imagedisplayed = [False,]

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
app.layout = html.Div([

    html.Div([        
        
        html.Div([
            dcc.Dropdown(
                id='usecases',
                options=[{'label': usecase, 'value': usecase} for usecase in definitions.verticalfilter.keys()],
                value='RFI-polar',
                clearable=False 
            ),
        ], style={'width':'95%'}),
        
        html.Br(),

        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='user_hand', 
                    clearable=False,  
                    style={'width':'100%'},
                    disabled=True
                ),
            ], style={'display':'inline-block', 'width':'28%'}),

            html.Div([
                dcc.Dropdown(
                    id='xaxis_var', 
                    clearable=False,
                    style = {'width':'100%'},
                    disabled=True 
                ), 
            ], style={'display':'inline-block', 'width':'36%'}),

            html.Div([
                dcc.Dropdown(
                    id='trace_var', 
                    clearable=False,
                    style = {'width':'100%'},
                    disabled=True 
                )
            ], style={'display':'inline-block', 'width':'36%'})

        ], style={'width':'95%'})

    ], style={'width': '16%', 'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial', 'display':'inline-block', 'vertical-align': 'top'}),

    html.Div([
        html.Div([
            html.Button(id='submit-button-state', n_clicks=0, children= 'Update Chart', style={'width': '90%'}),
        ]),


    ], style={'width': '8%', 'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial', 'display':'inline-block', 'vertical-align': 'top'}),


    html.Div([

        html.Div([

            html.Div([
                html.Button(id='select_xaxis', n_clicks=0, children= 'x-axis', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'12.5%'}),

            html.Div([
                html.Button(id='select_yaxis', n_clicks=0, children= 'y-axis', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'12.5%'}),

            html.Div([
                html.Button(id='suited', n_clicks=0, children= 'suited', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'12.5%'}),

            html.Div([
                html.Button(id='offsuit', n_clicks=0, children= 'offsuit', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'12.5%'}),

            html.Div([
                html.Button(id='sniper_mode', n_clicks=0, children= 'sniper mode', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'12.5%'}),

            html.Div([
                html.Button(id='test_mode', n_clicks=0, children= 'test mode', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'12.5%'}),
     
            html.Div([
                html.Button(id='show_legend', n_clicks=0, children= 'legend', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'12.5%'}),

        ], style={'width':'100%'}),

        html.Div([
            html.Div([
                html.P('y-axis: ')
            ], style={'display': 'inline-block'}),

            html.Div([
                dcc.Checklist(
                    id='yaxis_variables',
                    options=[{'label': handsubclass, 'value': handsubclass} for handsubclass in definitions.handVariants.keys()],
                    value=list(definitions.handVariants.keys()),
                ),
            ], style={'display': 'inline-block'}),
        ]),

        html.Div([
            html.Div([
                html.P('x-axis: ')
            ], style={'display': 'inline-block'}),

            html.Div([
                dcc.Checklist(
                    id='xaxis_variables',
                    value=[]
                ),
            ], style={'display': 'inline-block'}),
        ]),

    ], style={'width': '76%', 'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial', 'display':'inline-block','vertical-align': 'top'}), 

    html.Span(id='legend_container'),

    dcc.Graph(
        id='graph',
        config={'displayModeBar': False, 'showTips': False},
        #figure=fig
    ), 

    #html.Span('test', id='tooltip-target'),
    #dbc.Tooltip('hover text', target='tooltip-target')
])

@app.callback(
    Output('user_hand', 'disabled'),
    Input('sniper_mode', 'n_clicks'),
    State('user_hand', 'disabled'))
def allow_hand_input(sniper_button, disabled):
    ctx = dash.callback_context
    component_id = ctx.triggered[0]['prop_id'].split('.')[0]
    #print('sniper button clicks = ', sniper_button)
    #print('component_id = ', component_id)
    if disabled == True and sniper_button > 0:
        return False
    else:
        return True

@app.callback(
    Output('user_hand', 'options'),
    Output('user_hand', 'value'), 
    Input('user_hand', 'disabled'))
def set_hand_dropdown(user_hand_disabled):
    if user_hand_disabled == False: 
        return [{'label': hand, 'value': hand} for hand in definitions.handMatrix.keys()], list(definitions.handMatrix.keys())[0]
    else:
        return [{'label': hand, 'value': hand} for hand in definitions.handMatrix.keys()], ''
    

@app.callback(
    Output('legend_container', 'children'),
    Input('show_legend', 'n_clicks'))
def show_legend(legend):
    image_filename = 'legend.PNG' # replace with your own image
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    
    if imagedisplayed[0] == False and legend > 0:
        imagedisplayed[0] = True
        return html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), height=650, style={'display':'block', 'margin-left':'auto', 'margin-right':'auto', 'width':'75%'})
    else:
        imagedisplayed[0] = False
        return ''

@app.callback(
    Output('submit-button-state', 'disabled'),
    Input('yaxis_variables', 'value'),
    Input('xaxis_variables', 'value'))
def set_button_enabled_state_axis(yaxis_variables, xaxis_variables):
    if len(yaxis_variables) == 0 or len(xaxis_variables) == 0:
        return True 
    else:
        return False


@app.callback(
    Output('select_xaxis', 'disabled'),
    Output('select_yaxis', 'disabled'),
    Output('suited', 'disabled'), 
    Output('offsuit', 'disabled'),
    Output('test_mode', 'disabled'), 
    Output('sniper_mode', 'disabled'),
    Input('user_hand', 'disabled'), 
    Input('xaxis_var', 'disabled'))
def set_button_enabled_state_sniper(user_hand_disabled, xaxis_var_disabled): 
    if user_hand_disabled == False:
        return False, True, True, True, True, False

    if xaxis_var_disabled == False:
        return True, True, True, True, False, True

    if user_hand_disabled == True and xaxis_var_disabled == True:
        return False, False, False, False, False, False

@app.callback(
    Output('xaxis_variables', 'options'),
    Input('usecases', 'value'))
def set_variable_checklist(selected_usecase):
    variable_list = []
    #print('selected_usecase= ', selected_usecase)
    last_element = list(definitions.verticalfilter[selected_usecase].keys())[-1] 

    for key in definitions.preFlopUseCases.keys():
        #print('substring =', key, ' string =', selected_usecase)
        
        if key in selected_usecase:
            #print('substring condition passed')
            variable_list = list(definitions.verticalfilter[selected_usecase].values())[-1]

    #print('variable_list= ', variable_list)    
    #print('last_element = ', last_element)
    if 'StackDepth' in last_element:  
        return [{'label': element.replace('BB', 'bb'), 'value': element} for element in variable_list]
    else:
        return [{'label': element, 'value': element} for element in variable_list]

@app.callback(
    Output('xaxis_var', 'disabled'),
    Input('test_mode', 'n_clicks'),
    State('xaxis_var', 'disabled'))
def set_test_mode_status(test_mode_button, test_mode_disabled):
    if test_mode_disabled == True and test_mode_button == 0:
        return True
    
    if test_mode_disabled == True and test_mode_button > 0: 
        return False 
    else:
        return True

@app.callback(
    Output('xaxis_var', 'options'),
    Output('xaxis_var', 'value'),
    Input('xaxis_var', 'disabled'),
    Input('usecases', 'value'))
def set_variable_dropdown(test_mode_disabled, selected_usecase):
    variable_list = []
    
    if test_mode_disabled == False:
        for key in definitions.preFlopUseCases.keys():
            #print('substring =', key, ' string =', selected_usecase)
            
            if key in selected_usecase:
                #print('substring condition passed')
                variable_list = list(definitions.verticalfilter[selected_usecase].values())[-1]

        return [{'label': element, 'value': element} for element in variable_list], variable_list[0]
    else:
        return [{'label': element, 'value': element} for element in variable_list], ''


@app.callback(
    Output('xaxis_variables', 'value'), 
    Input('xaxis_variables', 'options'),
    Input('select_xaxis', 'n_clicks'), 
    Input('usecases', 'value'),
    Input('xaxis_var', 'disabled'), 
    State('xaxis_variables', 'value'))
def set_variable_value(variable_dict, select, usecase, xaxis_var_disabled, xaxis_variables):
    #print('usecaselog = ', usecaselog)
    variable_list = []
    ctx = dash.callback_context
    component_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if xaxis_var_disabled == False: 
        variable_list.append(xaxis_variables[0])

    if xaxis_var_disabled == True: 
        difference = len(xaxis_variables) - len(list(variable_dict))

        '''
        print(variable_dict)
        print('component_id = ', component_id)
        print('select = ', select)
        print('difference = ', difference)
        print('last use case = ',  usecaselog[-1], ' current use case = ', usecase)
        '''

        if usecaselog[-1] == usecase and difference == 0:
            variable_list = []
        
        if usecaselog[-1] == usecase and difference != 0 or component_id == 'xaxis_variables' or usecaselog[-1] != usecase: 
            for variable in variable_dict:
                #print('for testing...= ', variable)
                variable_list.append(variable['value'])

        usecaselog.append(usecase)
        usecaselog.pop(0)
    return variable_list


@app.callback(
    Output('yaxis_variables', 'options'),
    Input('user_hand', 'disabled'),
    Input('xaxis_var', 'disabled'),
    State('yaxis_variables', 'options'), 
    State('user_hand', 'value'))
def set_checklist_enabled_state(user_hand_disabled, xaxis_var_disabled, options, user_hand):

    if user_hand_disabled == True and xaxis_var_disabled == True: 
        return [{'label':handsubclass, 'value':handsubclass, 'disabled': False} for handsubclass in definitions.handVariants.keys()]
    else:
        return [{'label':handsubclass, 'value':handsubclass, 'disabled': True} for handsubclass in definitions.handVariants.keys()]



@app.callback(
    Output('yaxis_variables', 'value'),
    Input('yaxis_variables', 'options'),
    Input('select_yaxis', 'n_clicks'),
    Input('suited', 'n_clicks'),
    Input('offsuit', 'n_clicks'), 
    Input('user_hand', 'value'),
    Input('user_hand', 'disabled'),
    Input('xaxis_var', 'disabled'),
    State('yaxis_variables', 'value'))
def set_checklist_values(variable_dict, select_yaxis, suited, offsuit, user_hand, user_hand_disabled, xaxis_var_disabled, yaxis_variables):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    difference = len(yaxis_variables) - len(list(variable_dict))

    #print('user hand disabled = ', user_hand_disabled)

    if xaxis_var_disabled == False: 
        yaxis_variables = list(definitions.handVariants.keys())


    if user_hand_disabled == False:    
        yaxis_variables.clear() 
        yaxis_variables.append(definitions.handMatrix[user_hand]['code'])

    if user_hand_disabled == True: 
        if button_id == 'select_yaxis':
            if difference == 0: 
                yaxis_variables = []
            else:
                yaxis_variables = list(definitions.handVariants.keys())

        if button_id == 'suited':
            yaxis_variables = []
            for key in definitions.handVariants.keys():
                if key[-1] == 's':
                    yaxis_variables.append(key)
        
        if button_id == 'offsuit':
            yaxis_variables = []
            for key in definitions.handVariants.keys():
                if key[-1] == 'o':
                    yaxis_variables.append(key)

    return yaxis_variables


@app.callback(
    Output('graph', 'figure'),
    Input('submit-button-state', 'n_clicks'),
    State('user_hand', 'disabled'),
    State('user_hand', 'value'),
    State('usecases', 'value'),
    State('yaxis_variables', 'value'),
    State('xaxis_variables', 'value'), prevent_initial_call=True)
def render_heatmap(update_chart, user_hand_disabled, user_hand, usecaseconfig, yaxis_variables, xaxis_variables): 
    #suppress_callback_exceptions=True
    if len(yaxis_variables) == 0 or len(xaxis_variables) == 0:
        raise PreventUpdate
    
    if user_hand_disabled == False: 
        print('user hand = ', user_hand)
    else: 
        print('user hand disabled is True') 
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

        #print('program-test user hand = ', user_hand)
        #print('program-test user hand[-1] = ', user_hand[-1])
        #print('program-test hands = ', hands)
        
        hero['handVariantMatrix'] = functions.getNewMatrix('handVariant', functions.getHandMatrix(hands, user_hand, user_hand_disabled))
        for (key, value) in hero['handVariantMatrix'].items():
            print('program() - after getNewNatrix() executed:', key,':', value)

        print('\n')

        #must pass filter to getNewMatrix for horizontal filtering
        hero['handVariantMatrix'], filterlist = functions.getFrequency('handVariant', hero['handVariantMatrix'], yaxis_variables)
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
