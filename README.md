# URLSCAN API GUI for image scans

This is a application created with use of PySimpleGUI for conducting scans with use of URLSCAN API.

In order to run the proper scan it is needed to create the `config.txt` file with only API Key in the first line.

The path to the `config.txt` is needed to be added in:

    if api_key is None:
        with open('config.txt') as config:
            api_key = config.readline()

This is the version 0.1 - more updates coming soon!

## Setup

### configure virtualenv (recommended) 

`python3 -m venv venv`

`source venv/bin/activate`

### configure passivetotal API key (required)

`pip3 install -r requirements.txt`

`pt-config setup user@example.com` - This will create a file in
`~/.config/passivetotal` for Linux
or in `C:\Users\<Username>\.config\passivetotal` for Windows
with the credentials used by passivetotal


## Issues

### ModuleNotFoundError: No module named 'tkinter'

(debian-based systems) `apt install python3-tk`
