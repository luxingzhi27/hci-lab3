# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Incorporate data
salariesByMajor = pd.read_csv(
    './dataset/college-salaries/degrees-that-pay-back.csv', encoding='MacRoman')
salariesByCollegeType = pd.read_csv(
    './dataset/college-salaries/salaries-by-college-type.csv', encoding='MacRoman')
salariesByRegion = pd.read_csv(
    './dataset/college-salaries/salaries-by-region.csv', encoding='MacRoman')


def getTable(csvFile):
    return dash_table.DataTable(data=csvFile.to_dict('records'), page_size=6, style_table={'overflowX': 'auto'})


csvFiles = [salariesByMajor, salariesByCollegeType, salariesByRegion]
tables = [[getTable(salariesByMajor)], [getTable(salariesByCollegeType)], [
    getTable(salariesByRegion)]]

# Clean up the columns with "$" symbol
columnsToClean = ['Starting Median Salary',
                  'Mid-Career Median Salary',
                  'Mid-Career 10th Percentile Salary',
                  'Mid-Career 25th Percentile Salary',
                  'Mid-Career 75th Percentile Salary',
                  'Mid-Career 90th Percentile Salary']


# Clean up the columns with "$" symbol
for col in columnsToClean:
    salariesByMajor[col] = salariesByMajor[col].str.replace(
        '$', '')
    salariesByMajor[col] = salariesByMajor[col].str.replace(
        ',', '').astype(float)
    salariesByCollegeType[col] = salariesByCollegeType[col].str.replace(
        '$', '')
    salariesByCollegeType[col] = salariesByCollegeType[col].str.replace(
        ',', '').astype(float)
    salariesByRegion[col] = salariesByRegion[col].str.replace(
        '$', '')
    salariesByRegion[col] = salariesByRegion[col].str.replace(
        ',', '').astype(float)


# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = dbc.Container([
    dbc.Row([
        html.Div('College Salaries Data Analysis',
                 className="text-primary text-center fs-3")
    ]),
    dbc.Row([
        html.Div([], style={'height': '20px'})
    ]),
    dbc.Row([
        dcc.Dropdown(
            id="dropdown-csv-files",
            options=[
                {"label": "salaries-by-major",
                    "value": "salaries-by-major"},
                {"label": "salaries-by-college-type",
                    "value": "salaries-by-college-type"},
                {"label": "salaries-by-region", "value": "salaries-by-region"}
            ],
            value="salaries-by-major",
        ),
    ]),
    dbc.Row([html.Div([], style={'height': '20px'})]),
    dbc.Row(id='table-row', children=tables[0]),
    dbc.Row([html.Div([], style={'height': '20px'})]),
    dbc.Row([
        dbc.RadioItems(options=[{"label": x, "value": x}
                                for x in ['Starting Median Salary', 'Mid-Career Median Salary',
                                          'Mid-Career 10th Percentile Salary',
                                          'Mid-Career 25th Percentile Salary',
                                          'Mid-Career 75th Percentile Salary',
                                          'Mid-Career 90th Percentile Salary',]],
                       value='Starting Median Salary',
                       inline=True,
                       id='radio-buttons-final'),
    ], justify='center'),
    dbc.Row([html.Div([], style={'height': '20px'})]),
    dbc.Row([dcc.Graph(figure={}, id='graph')],
            style={'height': '700px'},
            justify='center',
            id='graphs-row'),
], fluid=True)


# Add controls to build the interaction


@callback(
    Output(component_id='graph',
           component_property='figure'),
    Input(component_id='radio-buttons-final', component_property='value'),
    Input(component_id='dropdown-csv-files', component_property='value')
)
def update_graph(col_chosen, selected_csv_file):
    if selected_csv_file == 'salaries-by-major':
        fig = px.histogram(salariesByMajor, x='Undergraduate Major',
                           y=col_chosen, histfunc='avg')
    elif selected_csv_file == "salaries-by-college-type":
        fig = px.scatter(salariesByCollegeType, x='Starting Median Salary',
                         y=col_chosen, color='School Type')
    elif selected_csv_file == "salaries-by-region":
        fig = px.box(salariesByRegion, color="Region", y=col_chosen)
    return fig


@app.callback(
    Output(component_id='table-row', component_property='children'),
    Input(component_id='dropdown-csv-files', component_property='value'),
)
def choose_csv_file(selected_csv_file):
    if selected_csv_file == 'salaries-by-major':
        return tables[0]
    if selected_csv_file == 'salaries-by-college-type':
        return tables[1]
    if selected_csv_file == 'salaries-by-region':
        return tables[2]


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
