#!/bin/bash
# This will send a POST with data
curl -s -o /dev/null -w "%{http_code}" "$1"
