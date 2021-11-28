# -*- coding: utf-8 -*-
from streamcheck import get_streamer_info, get_stream_status, read_chat
import socket
import os

data = get_streamer_info('vgbootcamp')
print(data)
is_live = get_stream_status(data)

if(is_live == True):
    read_chat(data)

    



         
    


