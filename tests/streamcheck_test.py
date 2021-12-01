from streamcheck import get_streamer_info, get_stream_status
import os 
import requests_mock

client_id = f'{os.environ["ClientID"]}'
secret = f'{os.environ["Secret"]}'
auth_url = 'https://id.twitch.tv/oauth2/token'
oauth = f'{os.environ["oauth"]}'

aut_params = {'client_id': client_id, 'client_secret': secret, 'grant_type': 'client_credentials'}

def test_api_request():
    with requests_mock.Mocker() as mock_request:
        mock_request.get()
    pass