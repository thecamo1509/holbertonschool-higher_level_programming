#!/bin/bash
# This will send a POST with data
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST $1
