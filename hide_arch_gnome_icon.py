#!/bin/python
import configparser
import sys
import os

config = configparser.ConfigParser()
# Do not convert to lower case
config.optionxform = str

sys_path = '/usr/share/applications/'
user_path = os.path.expanduser('~/.local/share/applications/')

entries = [
    'lstopo.desktop',
    'qvidcap.desktop',
    'qv4l2.desktop',
    'bssh.desktop',
    'bvnc.desktop',
    'avahi-discover.desktop'
]

def hide_entry(entry: str):
    with open(sys_path + entry) as read_from:
        config.read_file(read_from)
        config.set('Desktop Entry', 'Hidden', 'true')
        with open(user_path + entry, 'w') as save_to:
            config.write(save_to, False)
            print("Hide: " + entry)

def toggle_entry(entry: str):
    config.read(entry)
    if config.has_option('Desktop Entry', 'Hidden'):
        if config['Desktop Entry']['Hidden'] == 'true':
            config.set('Desktop Entry', 'Hidden', 'false')
            print("Show: " + entry)
        else:
            config.set('Desktop Entry', 'Hidden', 'true')
            print("Hide: " + entry)

def default_hide():
    for entry in entries:
        if not os.path.isfile(sys_path + entry):
            continue
        hide_entry(entry)

if __name__ == '__main__':
    if 1 == len(sys.argv):
        default_hide()
    if 2 == len(sys.argv):
        entry = sys.argv[1]
        if os.path.isfile(sys_path + entry):
            if os.path.isfile(user_path + entry):
                toggle_entry(user_path + entry)
                with open(user_path + entry, 'w') as f:
                    config.write(f, False)
            else:
                hide_entry(entry)
        else:
            print("Do nothing.")
