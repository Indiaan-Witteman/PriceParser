import datetime
import os
from dotenv import load_dotenv
import hashlib

from fastapi import HTTPException, Request
import jwt


# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
sercret_key = os.getenv("SECRET_KEY")

class price_parser_service:
    
    
    
    @classmethod
    def parse_price(cls, input_text : str = None):
        
        # here comes the logic. 
        
        return "test"
    
    