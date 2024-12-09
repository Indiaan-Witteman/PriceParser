# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:00:53 2024

@author: Gebruiker
"""

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from PriceParse.services.demo import parser_demo

class DemoRouter:
    router = APIRouter(
        prefix="/demo",
        tags=["demo"],
        responses={404: {"description": "Not found"}},
    )

    @router.get("/", response_class=HTMLResponse)
    async def get_demo():
        """
        Serve the demo Gradio/Plotly app.

        Returns:
            HTMLResponse: The HTML page containing the demo app.
        """
        return parser_demo()
