#!/bin/bash
# sends a request to the provided url and displays the size of the response body in bytes
curl -Si "$1" | grep -i content-lengh | cut -d " " -f 2