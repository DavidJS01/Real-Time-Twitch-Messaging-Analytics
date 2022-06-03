# -*- coding: utf-8 -*-

from streamcheck import thread_placeholder_name
import argparse
import logging

def main():
    parser = argparse.ArgumentParser(description="Real Time Twitch Analytics!")
    parser.add_argument("add_stream", nargs = '*', metavar = "stream_name", type = str,
                        help = "Type Twitch stream names, seperated by a space.")

    args = parser.parse_args()
    print(f'attempting to access streams: {args.add_stream}')
    thread_placeholder_name(args.add_stream)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))

# streams = ['drututt', 'solarbacca', 'dunlol', 'aphromoo', 'veigarv2', 'cookielolxx', 'katevolved', 'sneakylol', 'doglightning']


# thread_placeholder_name(streams)


    



         
    


