import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Load the data
def load_data():
    try:
        df = pd.read_csv('data/owid-covid-data.csv')
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Create the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("COVID-19 Global Data Tracker", className="text-center my-4"),
            html.P("Track COVID-19 statistics across different countries", className="text-center")
        ])
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H3("Select Country", className="mt-4"),
            dcc.Dropdown(
                id='country-dropdown',
                options=[],  # Will be populated with data
                value='World',
                className="mb-4"
            )
        ], width=6)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='cases-graph')
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='deaths-graph')
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='vaccination-graph')
        ], width=12)
    ])
], fluid=True)

# Callback to update country dropdown
@app.callback(
    Output('country-dropdown', 'options'),
    Input('country-dropdown', 'value')
)
def update_country_dropdown(_):
    df = load_data()
    if df is not None:
        countries = sorted(df['location'].unique())
        return [{'label': country, 'value': country} for country in countries]
    return []

# Callback to update cases graph
@app.callback(
    Output('cases-graph', 'figure'),
    Input('country-dropdown', 'value')
)
def update_cases_graph(selected_country):
    df = load_data()
    if df is not None:
        country_data = df[df['location'] == selected_country]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=country_data['date'],
            y=country_data['total_cases'],
            mode='lines',
            name='Total Cases'
        ))
        fig.add_trace(go.Scatter(
            x=country_data['date'],
            y=country_data['new_cases'],
            mode='lines',
            name='New Cases'
        ))
        
        fig.update_layout(
            title=f'COVID-19 Cases in {selected_country}',
            xaxis_title='Date',
            yaxis_title='Number of Cases',
            template='plotly_white'
        )
        return fig
    return {}

# Callback to update deaths graph
@app.callback(
    Output('deaths-graph', 'figure'),
    Input('country-dropdown', 'value')
)
def update_deaths_graph(selected_country):
    df = load_data()
    if df is not None:
        country_data = df[df['location'] == selected_country]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=country_data['date'],
            y=country_data['total_deaths'],
            mode='lines',
            name='Total Deaths'
        ))
        fig.add_trace(go.Scatter(
            x=country_data['date'],
            y=country_data['new_deaths'],
            mode='lines',
            name='New Deaths'
        ))
        
        fig.update_layout(
            title=f'COVID-19 Deaths in {selected_country}',
            xaxis_title='Date',
            yaxis_title='Number of Deaths',
            template='plotly_white'
        )
        return fig
    return {}

# Callback to update vaccination graph
@app.callback(
    Output('vaccination-graph', 'figure'),
    Input('country-dropdown', 'value')
)
def update_vaccination_graph(selected_country):
    df = load_data()
    if df is not None:
        country_data = df[df['location'] == selected_country]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=country_data['date'],
            y=country_data['people_vaccinated_per_hundred'],
            mode='lines',
            name='Vaccination Rate'
        ))
        
        fig.update_layout(
            title=f'COVID-19 Vaccination Rate in {selected_country}',
            xaxis_title='Date',
            yaxis_title='Vaccination Rate (per 100 people)',
            template='plotly_white'
        )
        return fig
    return {}

if __name__ == '__main__':
    app.run_server(debug=True) 