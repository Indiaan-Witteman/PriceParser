# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:04:39 2024

@author: Gebruiker
"""
import dash
from dash import Input, Output, State, dcc, html
from PriceParser.services.price_parser_service.price_parser_service import ProductParserService

# Simulating the parse_service function
def parse_service(text):
    # Replace this with the actual implementation of your function
    text = ProductParserService.parse_email_data(email_text= text)
    return f"PriceParser: {text}"

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
                    "Price Parser Demo, by LeoHanhart",
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
                    placeholder='Type your message here...', 
                    style={
                        'width': '100%', 
                        'height': '100px', 
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
        # Chat output area
        html.Div(
            id='output-text', 
            style={
                'margin-top': '20px',
                'width': '100%', 
                'height': '200px', 
                'overflow-y': 'auto', 
                'font-size': '16px', 
                'border': '1px solid #ccc', 
                'border-radius': '5px', 
                'padding': '10px', 
                'background-color': '#f9f9f9'
            }
        )
    ]
)

# Callback to handle input and output
@app.callback(
    Output('output-text', 'children'),
    Input('send-button', 'n_clicks'),
    State('input-text', 'value'),
    State('output-text', 'children'),
    prevent_initial_call=True
)
def update_chat(n_clicks, user_input, chat_history):
    if not user_input:
        return chat_history

    # Append the user input and bot response to chat history
    bot_response = parse_service(user_input)
    if not chat_history:
        chat_history = ""
    updated_chat = f"{chat_history}\n\nYou: {user_input}\n{bot_response}"
    return updated_chat

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
