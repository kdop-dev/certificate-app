#!/bin/bash
docker build -t kdop/certificate-app:0.0.1 .
#docker push kdop/certificate-app:0.0.1
docker run --rm -p 5000:5000 --name=certificate-app kdop/certificate-app:0.0.1
