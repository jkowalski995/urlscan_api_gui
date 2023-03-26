import PySimpleGUI as sg
import PIL.Image
import io
import base64
import requests
import json
import time
from io import BytesIO


def api_call(url=None, api_key=None):
    """
    Will connect with urlscan.io API and retrieve an image (bytes) of provided url.
    :param url: (string) a string url of scanned website with or without https://www.
    :return: (bytes) image view in bytes object
    """
    if api_key is None:
        with open('config.txt') as config:
            api_key = config.readline()

    headers = {'API-Key': str(api_key) , 'Content-Type': 'application/json'}
    data = {"url": url, "visibility": "private"}
    response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))
    print(response)
    uuid = response.json()['uuid']

    time.sleep(15)

    response = requests.get('https://urlscan.io/screenshots/' + uuid + '.png', headers=headers, data=json.dumps(data))
    print(response)
    img_bytes = response.content

    return img_bytes


def convert_to_bytes(file_or_bytes, resize=None):
    """
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    """
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height / cur_height, new_width / cur_width)
        img = img.resize((int(cur_width * scale), int(cur_height * scale)), PIL.Image.LANCZOS)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()


def show_image(data=None):
    """
    Show an image in full size in system image viewer.
    :param data: (bytes) image from urlscan.io API as a bytes object
    :return: None, it calls an im.show() and show an image
    """
    im = PIL.Image.open(BytesIO(data))
    im.show()


def save_image(url=None, path=None, data=None):
    """
    Will convert image from bytes object to image and save it as a PNG.
    :param url: (string) a string url of scanned website with or without https://www.
    :param path: (string) a string path to the place where the image should be saved
    :param data: (bytes) image from urlscan.io API as a bytes object
    :return: None, it saved an image
    """
    # Load image from BytesIO
    image_to_save = PIL.Image.open(BytesIO(data))

    image_to_save.save(path + url + '.png')


layout = [[sg.Text('URL:')],
          [sg.InputText('e.g. https://domain.to.scan.url', key='-URL-'),
           sg.Button('Scan', key='-SCAN-', bind_return_key=True), sg.Button('Show oryginal image size', key='-SHOW-')],
          [sg.Button('Save original image', key='-SAVE-'),
           sg.InputText('C:\\', key='-PATH-')], [sg.Exit()],
          [sg.Image(size=(800, 600), key='-IMAGE-')],
          ]

window = sg.Window('URLSCAN API CONNECT', layout)

while True:
    event, values = window.read()
    print(event, values)  # for debugging
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-SCAN-':
        url = values['-URL-']
        try:
            data = api_call(url)
        except KeyError:
            sg.popup(f'The website {url} \nis currently not available. \nCheck if provided URL is correct and do not '
                     f'violate urlscan.io regulations.\n Also, check if API Key is provided and is correct.',
                     title='Error!')
            continue
        im = convert_to_bytes(data, resize=(800, 600))
        window['-IMAGE-'].update(data=im)
    if event == '-SHOW-':
        try:
            show_image(data)
        except NameError:
            sg.popup('There is no image to show. \nPlease do the scan first or scan a available website!',
                     title='Error!')
            continue
    if event == '-SAVE-':
        try:
            save_image(url=url, path=values['-PATH-'], data=data)
        except (FileNotFoundError, NameError):
            sg.popup(f'The path is broken. \nCheck if provided PATH is correct.\nOr do the scan before saving '
                     f'the original image!', title='Error!')
            continue
window.close()
