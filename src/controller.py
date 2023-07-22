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

        #self.wallet_address = os.environ.get('WALLET_ADDRESS')
        #if not self.wallet_address:
        #    raise ValueError("WALLET_ADDRESS environment variable not set")

        # BscScan API request parameters
        self.wallet_addresses = [os.environ.get('WALLET_ADDRESS_1'), os.environ.get('WALLET_ADDRESS_2'), os.environ.get('WALLET_ADDRESS_3')]

    def get_balance(self):
        balances = {}
        for address in self.wallet_addresses:
            # BscScan API request parameters
            self.params = {
                'module': 'account',
                'action': 'balance',
                'address': address,
                'apikey': self.api_key,
            }
            print(self.params)
        
        # Make BscScan API request
            response = requests.get(api_endpoint, params=self.params)
            data = response.json()
            print(data)

        # Check if the request was successful
        #if data['status'] == '1':
        #    self.balance = int(data['result']) / 1e18  # Convert balance from wei to BNB
        #    return self.balance
        #else:
        #    raise ValueError(f"Error: {data['message']}")

            if data['status'] == '1':
                balance = int(data['result']) / 1e18  # Convert balance from wei to BNB
                balances[address] = balance
                print(balances)
            else:
                balances[address] = None

        return balances