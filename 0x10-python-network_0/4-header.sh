#!/bin/bash
#take in a url and has a header varible, sends a GET reuest and return the response
curl -sH "X-School-User-Id: 98" "$1"
