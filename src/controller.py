import os
import requests
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file
api_endpoint = 'https://api.bscscan.com/api'


class GetBalance():
    def __init__(self) -> None:
        self.api_key = os.environ.get('BSC_SCAN_API_KEY')
        if not self.api_key:
            raise ValueError("BSC_SCAN_API_KEY environment variable not set")

        self.wallet_address = os.environ.get('WALLET_ADDRESS')
        if not self.wallet_address:
            raise ValueError("WALLET_ADDRESS environment variable not set")

        # BscScan API request parameters
        self.params = {
            'module': 'account',
            'action': 'balance',
            'address': self.wallet_address,
            'apikey': self.api_key,
        }


    def get_balance(self):
        
        # Make BscScan API request
        response = requests.get(api_endpoint, params=self.params)
        data = response.json()

        # Check if the request was successful
        if data['status'] == '1':
            balance = int(data['result']) / 1e18  # Convert balance from wei to BNB
            return balance
        else:
            raise ValueError(f"Error: {data['message']}")
