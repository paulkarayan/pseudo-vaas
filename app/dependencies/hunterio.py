'''This module is to be used for calling the hunter.io api endpoints

'''
from app.dependencies import CONFIG_FILE
from configular import Configular
import requests
from typing import Dict


config = Configular(CONFIG_FILE)
api_key = config.get('HunterIO', 'api_key')
base_url = 'https://api.hunter.io/v2'


class HunterIOAPI():

    domain_search_url = f'{base_url}/domain-search?api_key={api_key}'
    email_finder_url = f'{base_url}/email-finder?api_key={api_key}'
    author_finder_url = f'{base_url}/author-finder?api_key={api_key}'
    email_verifier_url = f'{base_url}/email-verifier?api_key={api_key}'
    email_count_url = f'{base_url}/email-count?api_key={api_key} '

    def _dict_to_params(self, param_dict: Dict) -> Dict:
        param_list = [f'{k}={v}' for k, v in param_dict.items()]
        return f'{"&".join(param_list)}'

    def _get(self, url, url_params):
        url = f'{url}&{self._dict_to_params(url_params)}'
        try:
            
            return requests.get(url).json()
        except Exception as e:
            return {}        

    def domain_search(self, url_params: Dict):
        return self._get(HunterIOAPI.domain_search_url, url_params)

    def email_finder(self, url_params: Dict) -> Dict:
        return self._get(HunterIOAPI.email_finder_url, url_params)

    def author_finder(self, url_params: Dict) -> Dict:
        return self._get(HunterIOAPI.author_finder_url, url_params)

    def email_verifier(self, url_params: Dict) -> Dict:
        return self._get(HunterIOAPI.email_verifier_url, url_params)
        
    def email_count(self, url_params: Dict) -> Dict:
        return self._get(HunterIOAPI.email_count_url, url_params)


hunterio_api = HunterIOAPI()
