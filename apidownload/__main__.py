import json
from pathlib import Path
import requests
import shutil
import sys

SETTINGS_FILE = Path('settings.json')

def fetch_endpoint(url: str, file: str, indent: int = 2):
    print('Updating ', file, '... ', sep = '', end = '')
    request = requests.get(url)
    data = request.json()
    Path(file).write_text(json.dumps(data, indent = indent))
    print('Done')

def create_settings_file():
    shutil.copyfile(Path(__file__).parent / 'default_settings.json', SETTINGS_FILE)
    print('Created', SETTINGS_FILE.absolute())

def main():
    if SETTINGS_FILE.exists():
        settings = json.loads(SETTINGS_FILE.read_text())
        for endpoint in settings:
            if isinstance(endpoint, dict):
                fetch_endpoint(**endpoint)
            else:
                print('Invalid endpoint type:', endpoint, file=sys.stderr)
    else:
        create_settings_file()

if __name__ == '__main__':
    main()
