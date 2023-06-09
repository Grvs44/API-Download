"""
Download the JSON contents of an API endpoint
"""
import json
import shutil
import sys
from pathlib import Path

import requests

SETTINGS_FILE = Path('apidownload.json')


def fetch_endpoint(url: str, file: str, indent: int = 2):
    """
    Download the JSON data at url and save it in file
    """
    print('Updating ', file, '... ', sep='', end='')
    request = requests.get(url, timeout=20)
    data = request.json()
    Path(file).write_text(json.dumps(data, indent=indent))
    print('Done')


def create_settings_file():
    """
    Copy the example settings.json file into this directory
    """
    shutil.copyfile(
        Path(__file__).parent / 'apidownload.json',
        SETTINGS_FILE
    )
    print('Created', SETTINGS_FILE.absolute())


def main():
    """
    Entry-point to program
    """
    if SETTINGS_FILE.exists():
        settings = json.loads(SETTINGS_FILE.read_text())
        for endpoint in settings:
            if not isinstance(endpoint, dict):
                fetch_endpoint(**endpoint)
            else:
                print('Invalid endpoint type:', endpoint, file=sys.stderr)
    else:
        create_settings_file()


if __name__ == '__main__':
    main()
