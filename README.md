# CIF VALIDATOR

This is a tool comprising of REST API to validate CIF files using PyCodCIF

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

7. Visit http://127.0.0.1:8015. The port may vary depending on the machine. This may be confirmed from the output of the previous step.


## Using REST API

Send a file with POST request and parameter name as ```cif``` to http://127.0.0.1:8015/compute/validate.
