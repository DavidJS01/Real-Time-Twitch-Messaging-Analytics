import requests
import socket
import threading
import logging
import os


client_id = f'{os.environ["ClientID"]}'
secret = f'{os.environ["Secret"]}'
auth_url = 'https://id.twitch.tv/oauth2/token'
oauth = f'{os.environ["oauth"]}'

aut_params = {'client_id': client_id, 'client_secret': secret, 'grant_type': 'client_credentials'}

def get_streams_api_data(parameters, head):
    r = requests.get(f'https://api.twitch.tv/helix/streams?{parameters}', headers=head).json()['data']
    print(r)
    return r

def get_streamer_info(streamer_name):
    AutCall = requests.post(url=auth_url, params=aut_params) 
    access_token = AutCall.json()['access_token']

    headers = {
        'Client-ID': client_id,
        'Authorization': "Bearer " + access_token
        }
    return get_streams_api_data(f'user_login={streamer_name}',headers)
    

def get_stream_status(data):
    stream_status = False
    if data[0]['type'] == 'live':
        stream_status = True
    return stream_status

def thread_placeholder_name(stream_list): # does this need to be changed?
    for stream in stream_list:
        try:
            data = get_streamer_info(stream)
            is_online = get_stream_status(data)
            if(is_online):
                thread = threading.Thread(target=read_chat, args=(data,))
                thread.start()
            else:
                print(f'streamer {data[0]["user_login"]} is offline')
        except IndexError as e:
                if(str(e) == 'list index out of range'):
                    logging.info(f"The stream for {stream} is offline")

def parse_chat(resp):
    resp = resp.rstrip().split('\r\n')
    for line in resp:
        if "PRIVMSG" in line:
            messager = line.split(':')[1].split('!')[0]
            msg = line.split(':', maxsplit=2)[2]
            line = messager + ": " + msg
            line = line.encode('utf-8')
            

def read_chat(data):
    oauth = os.environ['oauth']
    nick = 'placeholder'
    sock = socket.socket()
    sock.connect(('irc.chat.twitch.tv',6667))
    sock.send(f"PASS {oauth}\n".encode('utf-8'))
    sock.send(f"NICK {nick}\n".encode('utf-8'))
    sock.send(f"JOIN #{data[0]['user_login']}\n".encode('utf-8'))
    

    while True:
        resp = sock.recv(2048).decode('utf-8')
        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))
        elif len(resp) > 0:
            parse_chat(resp)
                

