# URLSCAN API GUI for image scans

This is a application created with use of PySimpleGUI for conducting scans with use of URLSCAN API.

In order to run the proper scan it is needed to create the `config.txt` file with only API Key in the first line.

The path to the `config.txt` is needed to be added in:

    `if api_key is None:
        with open('config.txt') as config:`
            api_key = config.readline()`

This is the version 0.1 - more updates coming soon!