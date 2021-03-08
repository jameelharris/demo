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
                html.Button(id='select_xaxis', n_clicks=0, children= 'deselect all x', style={'width':'99%'})
            ], style={'display':'inline-block', 'width':'7%'}),

            html.Div([
                html.Button(id='select_yaxis', n_clicks=0, children= 'deselect all y', style={'width':'99%'})
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
            ], style={'display':'inline-block', 'width':'12%', 'visibility':'hidden'}),

            html.Div([
                html.Div(id='product_name_container', style={'width':'99%'})
            ], style={'display':'inline-block'}),
     
        ]),

    ], style={'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial', 'position':'absolute', 'width':'1500px', 'height':'10px', 'top':'2px'}),

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

    ], style={'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial', 'padding-top': '4px', 'position':'absolute', 'width':'1500px', 'height':'10px', 'top':'25px'}),


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
                    id='dropdown_2', 
                    clearable=False,
                    style = {'width':'99%', 'visibility':'hidden'},
                    disabled=True,  
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

    ], style={'font-weight':'bold', 'font-size':'12px', 'font-family':'Arial', 'padding-top': '2px', 'position':'absolute', 'width':'1500px', 'height':'10px', 'top':'65px'}), 
    
    html.Div([
        html.Span(id='legend_container', style={'display':'none'}),
        html.Span(id='test_ui', style={'display':'none'}),
        dcc.Graph(
            id='graph',
            config={'displayModeBar': False, 'showTips': False},
            style={'display':'none'}
            #figure=fig
        ), 

        dcc.Store(id='trace_names'),
        dcc.Store(id='blank_test'),
        dcc.Store(id='test_answers'),
        dcc.Store(id='test_scenario'),
        dcc.Store(id='test_prompt')

        #html.Span('test', id='tooltip-target'),
        #dbc.Tooltip('hover text', target='tooltip-target')
    ], style={'position':'absolute', 'width':'1500px', 'height':'650px', 'top':'104px'})
])


@app.callback(
    Output('test_ui', 'children'),
    Output('test_ui', 'style'),
    Input('blank_test', 'data'), 
    Input('test_answers', 'data'), 
    Input('test_scenario', 'data'))
def display_test_ui(blank_test, test_answers, test_scenario):
    if (blank_test and test_answers and test_scenario) is not None and len(blank_test.keys()) != 0:
        print('from validate test scope - blank test = ', blank_test)
        print('from validate test scope - test answers = ', test_answers)
        print('from validate test scope - test scenario = ', test_scenario)
        
        return [
            html.Div([
                html.Button(id='pure', n_clicks=0, children= 'pure', style={'display':'block', 'width': '25%'}),
                html.Button(id='high', n_clicks=0, children= 'high', style={'display':'block', 'width': '25%'}),
                html.Button(id='medium', n_clicks=0, children= 'medium', style={'display':'block', 'width': '25%'}),
                html.Button(id='low', n_clicks=0, children= 'low', style={'display':'block', 'width': '25%'}),
                html.Button(id='fold', n_clicks=0, children= 'fold', style={'display':'block', 'width': '25%'})
            ])
        ], {'display':'block', 'position':'absolute', 'width':'250px', 'right':'300px', 'background':'black'}


    else:
        print('from validate test scope - prevent update')
        raise PreventUpdate

@app.callback(
    Output('dropdown_1', 'style'),
    Output('dropdown_2', 'style'),
    Input('app_mode', 'value'),
    Input('submit-button-state', 'children'))
def change_dropdown_visbility(app_mode, submit_text):

    if app_mode == 'nuclear':
        return {'visibility':'hidden', 'width': '99%'}, {'visibility':'hidden', 'width': '99%'}
    if app_mode == 'sniper':
        return {'visibility':'visible','width': '99%'}, {'visibility':'hidden', 'width': '99%'}
    if app_mode == 'test' and submit_text == 'Set x and y':
        return {'visibility':'visible', 'width': '99%'}, {'visibility':'hidden', 'width': '99%'}
    if app_mode == 'test' and submit_text == 'Set column':
        return {'visibility':'visible', 'width': '99%'}, {'visibility':'visible', 'width': '99%'}

@app.callback(
    Output('submit-button-state', 'children'),
    Output('dropdown_2', 'options'),
    Output('dropdown_2', 'value'),
    Input('app_mode', 'value'),
    Input('submit-button-state', 'n_clicks'),
    Input('usecases', 'value'),
    Input('dropdown_1', 'value'),
    Input('trace_names', 'data'),
    Input('yaxis_variables', 'value'),
    State('submit-button-state', 'children'))
def change_button_title(app_mode, submit_button_clicks, selected_usecase, selected_x_value, data, yaxis_variables, button_text):
    ctx = dash.callback_context
    component_id = ctx.triggered[0]['prop_id'].split('.')[0]


    if app_mode == 'test':
        if button_text == 'Set x and y' and component_id not in ('dropdown_1', 'yaxis_variables', 'usecases') and len(data) > 0:
            #print('passed change button title test')
            return 'Set column', [{'label': trace_var, 'value': trace_var} for trace_var in data], data[0]
        else:
            return 'Set x and y', [], ''
    else:
        return 'Update Target', [], ''

    
@app.callback(
    Output('dropdown_1', 'disabled'),
    Output('dropdown_2', 'disabled'),
    Input('app_mode', 'value'))
def set_dropdown_enablement(app_mode):
    #print('app_mode = ', app_mode)
    if app_mode == 'sniper':
        return False, True
    if app_mode == 'test':
        return False, False
    if app_mode == 'nuclear':
        return True, True


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
    Output('legend_container', 'style'),
    Input('show_legend', 'n_clicks'), 
    State('legend_container', 'style'))
def show_legend(legend_button, legend_style):
    image_filename = 'legend.PNG' # replace with your own image
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    #print('legend style = ', legend_style)
    if legend_style['display'] == 'none' and legend_button > 0:
        return html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), height=650, style={'display':'block', 'margin-left':'auto', 'margin-right':'auto', 'width':'75%'}), {'display':'block'}
    else:
        return '', {'display':'none'}
                    
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
    Output('select_xaxis', 'children'),
    Input('xaxis_variables', 'value'), 
    State('xaxis_variables', 'options'))
def change_select_xaxis_button_text(xaxis_variables, variable_dict):
    difference = len(xaxis_variables) - len(list(variable_dict))
    #print('change select == ', difference)
    #print('change select == xaxisvariables', xaxis_variables),
    #print('change select == variabledict', variable_dict)
    if difference == 0:
        return 'deselect all x'
    else:
        return 'select all x'

@app.callback(
    Output('select_yaxis', 'children'),
    Input('yaxis_variables', 'value'), 
    State('yaxis_variables', 'options'))
def change_select_yaxis_button_text(yaxis_variables, variable_dict):
    difference = len(yaxis_variables) - len(list(variable_dict))
    if difference == 0:
        return 'deselect all y'
    else:
        return 'select all y'


@app.callback(
    Output('xaxis_variables', 'value'), 
    Input('xaxis_variables', 'options'),
    Input('select_xaxis', 'n_clicks'), 
    Input('usecases', 'value'),
    Input('app_mode', 'value'),
    Input('dropdown_1', 'value'), 
    State('xaxis_variables', 'value'))
def set_xaxis_checklist_values(variable_dict, select_button_clicks, usecase, app_mode, selected_variable, xaxis_variables):
    variable_list = []
    ctx = dash.callback_context
    component_id = ctx.triggered[0]['prop_id'].split('.')[0]
    #print('set axis checklist values - component id = ', component_id)
    #print('set axis checklist values - app mode = ', app_mode)
    #print('set axis...variable dict = ', variable_dict)

    difference = len(xaxis_variables) - len(list(variable_dict))
    #print('difference == ', difference)

    if component_id in ('select_xaxis',):
        if difference == 0:
            variable_list = [] 
        else:
            for variable in variable_dict:
                variable_list.append(variable['value'])
        return variable_list

    if app_mode in ('nuclear',):
        #print('app mode in nuclear')
        if component_id in ('app_mode'): 
            variable_list = xaxis_variables
        else:
            for variable in variable_dict:
                variable_list.append(variable['value'])
        
    
    if app_mode in ('sniper',): 
        #print('app mode in sniper')
        if component_id not in ('usecases',):
            variable_list = xaxis_variables
        else:
            for variable in variable_dict:
                variable_list.append(variable['value'])
            

    if app_mode in ('test',): 
        #print('app mode in test')
        variable_list.append(selected_variable)
    
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
def set_yaxis_checklist_values(variable_dict, select_yaxis, suited, offsuit, dropdown_1_value, app_mode, yaxis_variables):
    selected_hand = ''
    if app_mode == 'sniper':
        selected_hand = dropdown_1_value
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    difference = len(yaxis_variables) - len(list(variable_dict))

    #print('button_id = ', button_id)

    if app_mode == 'test':
        pass


    if app_mode == 'sniper':    
        yaxis_variables.clear() 
        yaxis_variables.append(definitions.handMatrix[selected_hand]['code'])

    if app_mode != 'sniper': 
        if button_id == 'select_yaxis':
            if difference == 0: 
                yaxis_variables.clear()
            else:
                yaxis_variables = list(definitions.handVariants.keys())

        if button_id == 'suited':
            yaxis_variables.clear()
            for key in definitions.handVariants.keys():
                if key[-1] == 's':
                    yaxis_variables.append(key)

        if button_id == 'offsuit':
            yaxis_variables.clear()
            for key in definitions.handVariants.keys():
                if key[-1] == 'o':
                    yaxis_variables.append(key)
    
    
    return yaxis_variables


@app.callback(
    Output('graph', 'figure'),
    Output('graph', 'style'),
    Output('trace_names', 'data'),
    Output('blank_test', 'data'),
    Output('test_answers', 'data'),
    Output('test_scenario', 'data'),
    Input('submit-button-state', 'n_clicks'),
    State('dropdown_2', 'value'), 
    State('app_mode', 'value'),
    State('submit-button-state', 'children'),
    State('dropdown_1', 'value'),
    State('usecases', 'value'),
    State('yaxis_variables', 'value'),
    State('xaxis_variables', 'value'), prevent_initial_call=True)
def render_heatmap(update_chart, selected_column, app_mode, button_text, dropdown_1_value, usecaseconfig, yaxis_variables, xaxis_variables): 
    selected_hand = ''
    #suppress_callback_exceptions=True
    if len(yaxis_variables) == 0 or len(xaxis_variables) == 0:
        raise PreventUpdate

    if app_mode == 'sniper': 
        selected_hand = dropdown_1_value
        #print('user hand = ', selected_hand)

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

        #print('program-test user hand = ', selected_hand)
        #print('program-test user hand[-1] = ', selected_hand[-1])
        #print('program-test hands = ', hands)
        
        hero['handVariantMatrix'] = functions.getNewMatrix('handVariant', functions.getHandMatrix(hands, selected_hand, app_mode))
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

    
    if app_mode in ('test',) and button_text == 'Set column':
        return functions.get_test_answers(useCaseInventory, selected_column, xaxis_variables, yaxis_variables, usecaseconfig)

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
