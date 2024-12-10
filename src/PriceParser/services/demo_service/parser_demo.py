# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:04:39 2024

@author: Gebruiker
"""
import dash
from dash import Input, Output, State, dcc, html, dash_table
from PriceParser.services.price_parser_service.price_parser_service import ProductParserService

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    style={'width': '60%', 'margin': 'auto', 'padding': '20px', 'font-family': 'Arial, sans-serif'},
    children=[
        # Header with logo and title
        html.Div(
            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px'},
            children=[
                html.Img(
                    src='https://cdn.prod.website-files.com/66050c5fc246f4f153986ac9/66066513f2d884346dec88d9_automation-group.svg',
                    style={'height': '50px', 'margin-right': '15px'}
                ),
                html.H1(
                    "Price Parser",
                    style={'font-size': '24px', 'margin': '0'}
                )
            ]
        ),
        # Text input area
        html.Div(
            style={'margin-bottom': '10px'},
            children=[
                dcc.Textarea(
                    id='input-text',
                    value="""Onderwerp: Nieuwe prijzen voor onze topproducten!

Hoi daar,

Ik hoop dat alles goed met je gaat! We hebben even naar onze prijzen gekeken en we hebben goed nieuws voor je: we hebben ze aangepast! Hier zijn de nieuwe prijzen voor een paar van onze paradepaardjes:

- Wielen: nu slechts €10 per stuk  
- Assen: voor maar €15 per stuk  
- Tandwielen: een koopje van €8 per stuk  

Laat me weten als je meer info nodig hebt, of als ik ergens mee kan helpen. Altijd leuk om van je te horen!

Vrolijke groeten,  
De A-Leverancier  
""",
                    placeholder='Type your message here...',
                    style={
                        'width': '100%',
                        'height': '200px',
                        'font-size': '16px',
                        'border': '1px solid #ccc',
                        'border-radius': '5px',
                        'padding': '10px'
                    }
                )
            ]
        ),
        # Send button
        html.Button(
            'Send',
            id='send-button',
            style={
                'width': '100%',
                'padding': '10px',
                'font-size': '18px',
                'background-color': '#007BFF',
                'color': 'white',
                'border': 'none',
                'border-radius': '5px',
                'cursor': 'pointer'
            }
        ),
        # Chat output area with loading spinner
        dcc.Loading(
            id='loading',
            type='circle',
            style={'margin-top': '20px'},
            children=[
                html.Div(
                    id='output-text',
                    style={
                        'width': '100%',
                        'height': '200px',
                        'overflow-y': 'auto',
                        'font-size': '16px',
                        'border': '1px solid #ccc',
                        'border-radius': '5px',
                        'padding': '10px',
                        'background-color': '#f9f9f9',
                        'white-space': 'pre-wrap'  # Preserve line breaks
                    }
                )
            ]
        ),
        # DataFrame display
        html.Div(
            id='output-table',
            style={'margin-top': '20px'}
        )
    ]
)

# Callback to handle input and output
@app.callback(
    [Output('output-text', 'children'),
     Output('output-table', 'children')],
    Input('send-button', 'n_clicks'),
    State('input-text', 'value'),
    State('output-text', 'children'),
    prevent_initial_call=True
)
def update_chat_and_table(n_clicks, user_input, chat_history):
    if not user_input:
        return chat_history, dash.no_update

    # Simulated bot response and parsed list
    bot_response, list_items = ProductParserService.parse_service(user_input)

    # Update chat history
    if not chat_history:
        chat_history = ""
    updated_chat = f"{chat_history}\n\nYou: {user_input}\nBot: {bot_response}"

    # Check if list_items is a valid list of dictionaries
    if isinstance(list_items, list) and all(isinstance(item, dict) for item in list_items):
        # Create a DataTable from the response
        table = dash_table.DataTable(
            columns=[{'name': col, 'id': col} for col in list_items[0].keys()],
            data=list_items,
            style_table={'width': '100%'},
            style_cell={'textAlign': 'left', 'padding': '5px', 'fontSize': '16px'},
            style_header={
                'backgroundColor': '#f1f1f1',
                'fontWeight': 'bold',
                'border': '1px solid #ccc'
            },
            style_data={
                'border': '1px solid #ccc'
            }
        )
    else:
        # If list_items is not a valid list of dictionaries, return a simple message
        table = html.Div("No table data to display.", style={'color': 'gray', 'fontSize': '16px'})

    return updated_chat, table


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
