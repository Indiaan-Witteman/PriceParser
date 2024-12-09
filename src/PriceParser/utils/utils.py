# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:54:00 2024

@author: Gebruiker
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

open_ai_api_key = os.getenv("OPENAI_API_KEY")
