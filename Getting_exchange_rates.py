import requests
import json   

class ConnectionWithTheBank:
    def __init__(self) -> None:
        self.url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
        self.response = requests.get(self.url)
        self.data = self.response.json()

    def passage(self, list_json):
        for item in list_json:
            if item.get('cc') == 'USD':
                number = item.get('rate')
                return round(number, 2)
        return None
    
    def read(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    def write(self, data, file_name='currency.json'):
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    
    def launch(self):
        self.write(self.data, 'currency.json')
        save = self.read('currency.json')
        number = self.passage(save) 
        
        return number
    
class Start_Communication:
    def communication_call(self):
        connection = ConnectionWithTheBank()
        current_rate = connection.launch()
        
        return current_rate