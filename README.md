# API Download
Download the data from an API endpoint to a file

## Install
```cmd
pip install apidownload
```

## Run
```cmd
apidownload
```
or
```cmd
python -m apidownload
````
* The first time `apidownload` is run in a directory, an `apidownload.json` file is created.
  * This contains the endpoint URLs and the file paths to store the data in.
  * Optionally, the `indent` property may be provided to override the default indentation level of 2 spaces.
* If the `apidownload.json` file exists in this directory, the endpoints are downloaded to the specified files.
