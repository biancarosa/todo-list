#!/bin/bash

API_URL=http://localhost:5005
for i in $(seq 1 100000); do
    data=$(echo "'{"description" : " a"}'")
    curl --request POST \
    --url $API_URL/tasks/ \
    --header 'Authorization: Basic Og==' \
    --header 'Content-Type: application/json' \
    --data '{"description":"task '$i'"}'
done;