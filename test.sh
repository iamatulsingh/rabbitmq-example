#!/bin/bash

curl -X GET http://localhost:5000/ -H "Content-Type: application/json" \
	-d '{"r": "email@domain.com", "c": "your message"}' | jq
