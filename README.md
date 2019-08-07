# CIF VALIDATOR

This is a tool comprising of REST API to validate CIF files using PyCodCIF.

## Deploy on Docker

1. Install [Docker](https://docs.docker.com/install/).

2. Fork the repository.

3. Clone the forked repository.

```console
git clone https://github.com/<user-name>/cif-validator.git
cd cif-validator
```

4. Build Docker image for ```tools-barebone```.

```console
cd tools-barebone
./build-docker.sh
```

5. Build Docker image for ```cif-validator```.

```console
cd ../cif-validator
./build-docker.sh
```

6. Run.

```console
./run-docker.sh
```

7. Visit http://127.0.0.1:8091 to check if the server started. The port may vary depending on the machine. This may be confirmed from the output of the previous step. The page might show `500 Internal Server Error`. Thats because the API uses a different URL (Look at the following steps).

## Testing
For testing, make sure that the server is running first.

1. Go to ```cif-validator/testing``` and install the required dependencies.
```console
pip install -r requirements.txt
```
2. To test the API, Run
```console
pytest
```
If both the tests pass, you are good to go :)
<br> Else, check the if all the requirements were installed correctly.

## Using the TOOL

##### Method 1
Send a `cif` file using POST request and parameter name as `cif` to http://127.0.0.1:8091/compute/validate/.

##### Method 2
Use the web page http://127.0.0.1:8091/compute/ to upload your own `cif` file or pick an example from the ones provided.

Both these methods return a ```JSON``` object containing the key **status**, which may hold the values *valid* or *error* , and the key **message** which may *describe the error in case there is*```.