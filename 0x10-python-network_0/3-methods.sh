#!/bin/bash
# This will send a DELETE request
curl -sI $1 | grep Allow: | cut -d " " -f 2-
