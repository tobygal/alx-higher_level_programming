#!/bin/bash
#a bash script that accepts a url and returns the size of body
curl -sI "$1" | grep Content-Length | cut -d " " -f2
