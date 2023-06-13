import requests
import json
from .data_types.acars.position import AcarsPosition
from .data_types.acars.update import AcarsUpdate
from .data_types.pirep_data import PirepData
from .data_types.pilot_user import PilotUser

class ApiHandler:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_pilot_user(self) -> PilotUser:
        url = f"{self.base_url}/api/users/me"
        headers = {
            'X-API-Key': self.api_key,
            'Content-type': 'application/json'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            json_response = response.json()
            if response.status_code == 200:
                return PilotUser(json_response)
            else:
                error = json_response['error']
                formatted_error = self.format_error(error)
                raise Exception(formatted_error)
        except requests.exceptions.RequestException as e:
            raise Exception(str(e))

    def fetch_pireps(self, page: int = 0) -> PirepData:
        url = f"{self.base_url}/api/pireps?page={page}"
        headers = {
            'X-API-Key': self.api_key,
            'Content-type': 'application/json'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            json_response = response.json()
            if response.status_code == 200:
                return PirepData(json_response)
            else:
                error = json_response['error']
                formatted_error = self.format_error(error)
                raise Exception(formatted_error)
        except requests.exceptions.RequestException as e:
            raise Exception(str(e))

    def post_acars_position(self, pirepId: int, data: AcarsPosition) -> PirepData:
        url = f"{self.base_url}/api/pireps/{pirepId}/acars/position"
        headers = {
            'X-API-Key': self.api_key,
            'Content-type': 'application/json'
        }

        try:
            response = requests.post(url, data=json.dumps(data.__dict__),  headers=headers)
            response.raise_for_status()
            json_response = response.json()
            if response.status_code == 400:
                error = json_response['error']
                formatted_error = self.format_error(error)
                raise Exception(formatted_error)
        except requests.exceptions.RequestException as e:
            raise Exception(str(e))

    def post_acars_update(self, pirepId: int, data: AcarsUpdate) -> PirepData:
        url = f"{self.base_url}/api/pireps/{pirepId}/update"
        headers = {
            'X-API-Key': self.api_key,
            'Content-type': 'application/json'
        }

        try:
            response = requests.post(url, data=json.dumps(data.__dict__),  headers=headers)
            response.raise_for_status()
            json_response = response.json()
            if response.status_code == 400:
                error = json_response['error']
                formatted_error = self.format_error(error)
                raise Exception(formatted_error)
        except requests.exceptions.RequestException as e:
            raise Exception(str(e))

    @staticmethod
    def format_error(error: str) -> str:
        code = error['code']
        http_code = error['http_code']
        message = error['message']
        formatted_error = f"Error {code} ({http_code}): {message}"
        return formatted_error
