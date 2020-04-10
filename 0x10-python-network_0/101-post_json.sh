#!/bin/bash
# post to JSON
curl -sd "@$2" -H "Content-Type: application/json" -X POST "$1"
