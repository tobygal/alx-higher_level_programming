#!/bin/bash
#takes a url and sends it a GET request and display the body response
curl -sfL "$1" -X GET
