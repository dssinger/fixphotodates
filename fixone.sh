#!/bin/bash
echo $1 >>log.txt
csv="${1: -10}.csv"
exiftool "$1" -if '(not $datetimeoriginal or ($datetimeoriginal eq "0000:00:00 00:00:00")) and ($filetype eq "JPEG")' -csv="$csv" >>log.txt 2>&1
