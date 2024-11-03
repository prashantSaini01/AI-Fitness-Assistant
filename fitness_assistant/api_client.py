import requests
from .config import Config

class GroqAPIClient:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.base_url = Config.BASE_URL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def call_api(self, messages):
        """Make API call to Groq"""
        try:
            payload = {
                "model": Config.MODEL_NAME,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 1024
            }
            
            response = requests.post(
                self.base_url, 
                headers=self.headers, 
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {str(e)}"
