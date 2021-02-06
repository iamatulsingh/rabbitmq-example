#!/bin/bash

curl -X GET http://localhost:5000/ -H "Content-Type: application/json" \
	-d '{"r": "fastoneatul@gmail.com", "c": "Good night !!"}' | jq
