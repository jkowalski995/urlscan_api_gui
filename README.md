# DOMAIN SCAN 

This is an application created with use of PySimpleGUI for conducting scans with use of URLSCAN API and RiskIQ PassiveTotal API.

## Version history
| Version | Comment                                                                                |
|---------|----------------------------------------------------------------------------------------|
| 0.1     | Initial version; only URLSCAN API feature working                                      |
| 0.2     | Passive total API feature added; little GUI changes; added whois.py and image.py files |
| 0.2.1   | Added raw WhoIs                                                                        |
| 0.3     | Comming soon...                                                                        |

## Ideas
- [x] Adding whole raw WhoIs record
- [ ] Adding saving the basic WhoIs
- [ ] Adding confirmation about saving the WhoIs
- Adding the default directory for saving screenshots
- [ ] Adding the CLI version
- [ ] Reworking the GUI:
  - [ ] Creating the better and user-friendly UI
- [ ] Saving whole data to some template e.g. Excel file

## Setup

### configure virtualenv (recommended) 

`python3 -m venv venv`

`source venv/bin/activate`

### configure passivetotal API key (required)

`pip3 install -r requirements.txt`

`pt-config setup user@example.com`

This will create a file in

`~/.config/passivetotal` for Linux

or in 

`C:\Users\<Username>\.config\passivetotal` for Windows


with the credentials used by passivetotal.

### configure urlscan API key (required)

In order to run the proper scan it is needed to create the `config.txt` file with only API Key in the first line.

The path to the `config.txt` is needed to be added in:

    if api_key is None:
        with open('config.txt') as config:
            api_key = config.readline()

## Issues

### ModuleNotFoundError: No module named 'tkinter'

(debian-based systems) `apt install python3-tk`
