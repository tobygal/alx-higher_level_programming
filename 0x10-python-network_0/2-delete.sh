#!/bin/bash
#accept a url, send a DELETE request and display body of reponse
curl -s "$1" -X DELETE
