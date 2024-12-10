# -*- coding: utf-8 -*-
"""
Created on Tue Dec 9 16:56:34 2024

@author: Gebruiker
"""

from openai import OpenAI
import json
from PriceParser.utils.utils import open_ai_api_key as api_key  # Use your custom import for the API key

class ProductParserService:
    """
    A service for parsing product information from unstructured email-like text using OpenAI's GPT model.

    Methods:
        parse_email_data(email_text): Parses the email text and extracts structured product data for multiple items.
    """
    @classmethod
    def parse_service(cls,text):
        
        # Replace this with the actual implementation of your function
        text = ProductParserService.parse_email_data(email_text= text)
        return f"PriceParser: {text}", text



    @classmethod
    def parse_email_data(cls, email_text: str) -> list:
        """
        Parses an email-like text for product data and returns structured JSON for multiple products.

        Parameters:
            email_text (str): The unstructured email text containing product data.

        Returns:
            list: A list of dictionaries, each representing a product with structured data.
        """
        if not api_key:
            raise ValueError("API key is not set.")

        if not email_text.strip():
            raise ValueError("Email text cannot be empty.")

        # Prompt for the OpenAI model
        prompt = (
            "You are given an email-like text containing information about multiple products. "
            "Parse the text and extract structured data for each product as an array of JSON objects. "
            "Each object should contain the following fields: supplier, product, price. "
            "If any field is missing, set its value to null. \n\n"
            f"Email Text: {email_text}\n\n"
            "Return JSON format: [{\"supplier\": \"string\", \"product\": \"string\", \"price\": float}]"
        )

        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)

        try:
            # Request completion using the OpenAI API
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Specify the chat model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for parsing email data."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0  # Set temperature for deterministic output
            )
        except Exception as e:
            # Catch all exceptions raised by OpenAI
            raise RuntimeError(f"OpenAI API error: {e}")

        # Extract the JSON response from the text
        completion_text = response.choices[0].message.content.strip()


        try:
            # Remove code block markers if present and parse the JSON content
            if completion_text.startswith("```json"):
                completion_text = completion_text[7:]
            if completion_text.endswith("```"):
                completion_text = completion_text[:-3]

            parsed_data = json.loads(completion_text.strip())
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse the response as JSON: {e}")

        return parsed_data


# Example usage
if __name__ == "__main__":
    # Input email text with multiple products
    email_text = (
        "Hi,\n\n"
        "We have updated the prices for the following products:\n\n"
        "- Wheels: 10 euros each\n"
        "- Axles: 15 euros each\n"
        "- Gears: 8 euros each\n\n"
        "Please let us know if you need further details.\n\n"
        "Best regards,\n"
        "The A-Supplier"
    )

    # Parse the email data
    try:
        result = ProductParserService.parse_service(email_text)
        print("Parsed Product Data:")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}")
