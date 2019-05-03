#!/bin/bash
echo "Connect to http://localhost:8091"
docker run -p 8091:80 --rm --name=tools-example-instance tools-example
