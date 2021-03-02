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
appmodelog = ['',]
selectxlog = [True,]
imagedisplayed = [False,]

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
app.layout = html.Div([

    html.Div([        

        html.Div([

            html.Div([
                dcc.RadioItems(
                    id='app_mode', 
                    options=[
                        {'label': 'nuclear option', 'value': 'nuclear'},
                        {'label': 'sniper mode', 'value': 'sniper'},
                        {'label': 'target practice', 'value': 'test'}
                    ],
                    value='nuclear',
                    labelStyle={'display': 'inline-block'},
                 )
            ], style={'display':'inline-block', 'width':'24%'}),

            html.Div([
                html.Button(id='submit-button-state', n_clicks=0, children= 'Update Target', style={'width': '99%'}),
            ], style={'display':'inline-block', 'width':'7%'}),

            html.Div([
                html.Button(id='select_xaxis', n_clicks=0, children= 'x-axis', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'7%'}),

            html.Div([
                html.Button(id='select_yaxis', n_clicks=0, children= 'y-axis', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'7%'}),

            html.Div([
                html.Button(id='suited', n_clicks=0, children= 'suited', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'7%'}),

            html.Div([
                html.Button(id='offsuit', n_clicks=0, children= 'offsuit', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'7%'}),

            html.Div([
                html.Button(id='show_legend', n_clicks=0, children= 'legend', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'7%'}),

            html.Div([
                html.Button(id='spacer_0', n_clicks=0, style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'22%', 'visibility':'hidden'}),

            html.Div([
                html.Div(id='product_name_container', style={'width':'99%'})
            ], style={'display':'inline-block'}),
     
        ]),

    ], style={'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial'}),

    html.Div([

        html.Div([
            dcc.Dropdown(
                id='usecases',
                options=[{'label': usecase, 'value': usecase} for usecase in definitions.verticalfilter.keys()],
                value='RFI-polar',
                clearable=False,
                style={'width': '99%'}
            ),
        ], style={'display': 'inline-block', 'width':'20%', 'vertical-align': 'bottom'}),

        html.Div([
                html.Button(id='spacer_1', n_clicks=0, style={'width':'99%'})
        ], style={'display':'inline-block', 'width':'4%', 'visibility':'hidden'}),


        html.Div([
            
            html.Div([
                html.P('y-axis: '),
            ], style={'display':'inline-block'}),

            html.Div([
                dcc.Checklist(
                    id='yaxis_variables',
                    options=[{'label': handsubclass, 'value': handsubclass} for handsubclass in definitions.handVariants.keys()],
                    value=list(definitions.handVariants.keys()),
        
                ),
            ], style={'display': 'inline-block'})

        ], style={'display': 'inline-block'}),

    ], style={'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial', 'padding-top': '4px'}),


    html.Div([

         html.Div([
            html.Div([
                dcc.Dropdown(
                    id='dropdown_1', 
                    clearable=False,  
                    style={'width':'99%', 'visibility':'hidden'},
                    disabled=True
                ),
            ], style={'display':'inline-block', 'width':'49%'}),


            html.Div([
                dcc.Dropdown(
                    id='trace_var', 
                    clearable=False,
                    style = {'width':'99%', 'visibility':'hidden'},
                    disabled=True 
                )
            ], style={'display':'inline-block', 'width':'50%'})

        ], style={'width':'20%', 'display':'inline-block', 'vertical-align':'bottom'}),

        html.Div([
                html.Button(id='spacer_2', n_clicks=0, style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'4%', 'visibility':'hidden'}),

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
        
        ], style={'display':'inline-block'}),

    ], style={'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial', 'padding-top': '2px'}), 

    html.Span(id='legend_container'),

    dcc.Graph(
        id='graph',
        config={'displayModeBar': False, 'showTips': False},
        style={'visibility':'hidden'}
        #figure=fig
    ), 

    #html.Span('test', id='tooltip-target'),
    #dbc.Tooltip('hover text', target='tooltip-target')
])


@app.callback(
    Output('dropdown_1', 'style'),
    Output('trace_var', 'style'),
    Input('app_mode', 'value'))
def change_dropdown_visbility(app_mode):
    if app_mode == 'nuclear':
        return {'visibility':'hidden', 'width': '99%'}, {'visibility':'hidden', 'width': '99%'}
    if app_mode == 'sniper':
        return {'visibility':'visible','width': '99%'}, {'visibility':'hidden', 'width': '99%'}
    if app_mode == 'test':
        return {'visibility':'visible', 'width': '99%'}, {'visibility':'visible', 'width': '99%'}


@app.callback(
    Output('submit-button-state', 'children'),
    Input('app_mode', 'value'))
def change_button_title(app_mode):
    if app_mode == 'test':
        return 'Lock and Load' 
    else:
        return 'Update Target'


@app.callback(
    Output('dropdown_1', 'disabled'),
    Input('app_mode', 'value'))
def enable_sniper_dropdown(app_mode):
    print('app_mode = ', app_mode)
    if app_mode in ('sniper', 'test'):
        return False
    else:
        return True


@app.callback(
    Output('dropdown_1', 'options'),
    Output('dropdown_1', 'value'),
    Input('app_mode', 'value'),
    Input('usecases', 'value'), 
    State('dropdown_1', 'value'))
def set_xaxis_dropdown(app_mode, selected_usecase, selected_dropdown_value):
    variable_list = []

    if app_mode in ('nuclear', 'test'):
        for key in definitions.preFlopUseCases.keys():
            #print('substring =', key, ' string =', selected_usecase)
            
            if key in selected_usecase:
                #print('substring condition passed')
                variable_list = list(definitions.verticalfilter[selected_usecase].values())[-1]

        return [{'label': element, 'value': element} for element in variable_list], variable_list[0]

    if app_mode in ('nuclear', 'sniper'):
        # if the dropdown value is not the default value then maintain the state of the selected value
        if selected_dropdown_value in list(definitions.handMatrix.keys()) and selected_dropdown_value != list(definitions.handMatrix.keys())[0]:
            dropdown1_value = selected_dropdown_value
        else:
            dropdown1_value = list(definitions.handMatrix.keys())[0] 
        return [{'label': hand, 'value': hand} for hand in definitions.handMatrix.keys()], dropdown1_value

    

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
    Output('product_name_container', 'children'),
    Input('app_mode', 'value'))
def show_product_name(app_mode): 
    image_filename = 'product_name.PNG' # replace with your own image
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())

    return html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), height='14', style={'vertical-align':'bottom'})



@app.callback(
    Output('submit-button-state', 'disabled'),
    Input('yaxis_variables', 'value'),
    Input('xaxis_variables', 'value'))
def validate_update_chart_enabled_state(yaxis_variables, xaxis_variables):
    if len(yaxis_variables) == 0 or len(xaxis_variables) == 0:
        return True 
    else:
        return False


@app.callback(
    Output('select_xaxis', 'disabled'),
    Output('select_yaxis', 'disabled'),
    Output('suited', 'disabled'), 
    Output('offsuit', 'disabled'),
    Input('app_mode', 'value'))
def set_button_enabled_state_sniper(app_mode): 
    if app_mode == 'sniper':
        return False, True, True, True

    if app_mode == 'test':
        return True, False, False, False

    if app_mode == 'nuclear':
        return False, False, False, False

@app.callback(
    Output('xaxis_variables', 'options'),
    Input('usecases', 'value'), 
    Input('app_mode', 'value'))
def set_xaxis_checklist_options(selected_usecase, app_mode):
    
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
    if app_mode == 'nuclear' or app_mode == 'sniper': 
        if 'StackDepth' in last_element:  
            return [{'label': element.replace('BB', 'bb'), 'value': element} for element in variable_list]
        else:
            return [{'label': element, 'value': element} for element in variable_list]
    if app_mode == 'test':
        if 'StackDepth' in last_element:  
            return [{'label': element.replace('BB', 'bb'), 'value': element, 'disabled': True} for element in variable_list]
        else:
            return [{'label': element, 'value': element, 'disabled': True} for element in variable_list]


@app.callback(
    Output('xaxis_variables', 'value'), 
    Input('xaxis_variables', 'options'),
    Input('select_xaxis', 'n_clicks'), 
    Input('usecases', 'value'),
    Input('app_mode', 'value'),
    Input('dropdown_1', 'value'), 
    State('xaxis_variables', 'value'))
def set_xaxis_checklist_values(variable_dict, select_button_clicks, usecase, app_mode, selected_variable, xaxis_variables):
    #print('usecaselog = ', usecaselog)
    variable_list = []
    ctx = dash.callback_context
    component_id = ctx.triggered[0]['prop_id'].split('.')[0]
    #print('comp id = ', component_id)
    xaxis_deslected = selectxlog[0]
    previous_app_mode = appmodelog[-1]
    difference = len(xaxis_variables) - len(list(variable_dict))

    print(variable_dict)
    print('component_id = ', component_id)
    print('last use case = ',  usecaselog[-1], ' current use case = ', usecase)
    print('last app mode = ',  appmodelog[-1], ' current app mode = ', app_mode)
    print('xaxis deselected = ', xaxis_deslected)

    if app_mode == 'test': 
        variable_list.clear()
        variable_list.append(selected_variable)


    if app_mode in ('sniper', 'nuclear'): 

        if component_id == 'select_xaxis' and (previous_app_mode == app_mode) and selectxlog[0] == True:
            if difference == 0:
                print('first condition if')
                variable_list = []
                selectxlog[0] = False
            else: 
                print('first condition else')
                for variable in variable_dict:
                    #print('for testing...= ', variable)
                    variable_list.append(variable['value'])
                selectxlog[0] = True
        else: 
            if previous_app_mode == 'test':
                print('second condition if')
                variable_list = xaxis_variables
                selectxlog[0] = True
            else:
                print('second condition else')
                # if dropdown contains hands then maintain state of xaxis selections unless the use case changes
                if selected_variable in list(definitions.handMatrix.keys()) and usecase == usecaselog[-1]:
                    variable_list = xaxis_variables
                    selectxlog[0] = True
                else:
                    for variable in variable_dict:
                        #print('for testing...= ', variable)
                        variable_list.append(variable['value'])
                    selectxlog[0] = True


    appmodelog.append(app_mode)
    appmodelog.pop(0)
    usecaselog.append(usecase)
    usecaselog.pop(0)
    return variable_list


@app.callback(
    Output('yaxis_variables', 'options'),
    Input('app_mode', 'value'))
def set_yaxis_checklist_enabled_state(app_mode):
    if app_mode in ('nuclear', 'test'): 
        return [{'label':handsubclass, 'value':handsubclass, 'disabled': False} for handsubclass in definitions.handVariants.keys()]
    else:
        return [{'label':handsubclass, 'value':handsubclass, 'disabled': True} for handsubclass in definitions.handVariants.keys()]



@app.callback(
    Output('yaxis_variables', 'value'),
    Input('yaxis_variables', 'options'),
    Input('select_yaxis', 'n_clicks'),
    Input('suited', 'n_clicks'),
    Input('offsuit', 'n_clicks'), 
    Input('dropdown_1', 'value'),
    Input('app_mode', 'value'),
    State('yaxis_variables', 'value'))
def set_yaxis_checklist_values(variable_dict, select_yaxis, suited, offsuit, user_hand, app_mode, yaxis_variables):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    difference = len(yaxis_variables) - len(list(variable_dict))


    if app_mode == 'test': 
        yaxis_variables = list(definitions.handVariants.keys())


    if app_mode == 'sniper':    
        yaxis_variables.clear() 
        yaxis_variables.append(definitions.handMatrix[user_hand]['code'])

    if app_mode != 'sniper': 
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
    Output('graph', 'style'),
    Input('submit-button-state', 'n_clicks'),
    State('app_mode', 'value'),
    State('dropdown_1', 'value'),
    State('usecases', 'value'),
    State('yaxis_variables', 'value'),
    State('xaxis_variables', 'value'), prevent_initial_call=True)
def render_heatmap(update_chart, app_mode, user_hand, usecaseconfig, yaxis_variables, xaxis_variables): 
    suppress_callback_exceptions=True
    if len(yaxis_variables) == 0 or len(xaxis_variables) == 0:
        raise PreventUpdate

    if app_mode == 'sniper': 
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
        
        hero['handVariantMatrix'] = functions.getNewMatrix('handVariant', functions.getHandMatrix(hands, user_hand, app_mode))
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
