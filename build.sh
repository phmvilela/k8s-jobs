#!/bin/bash

kubectl delete deploy/job-trigger
sleep 10
docker build -f job-trigger/Dockerfile -t job-trigger:stable job-trigger
kubectl create -f job-trigger/job-trigger-depl.yaml
