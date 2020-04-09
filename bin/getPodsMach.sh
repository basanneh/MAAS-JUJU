#!/bin/bash
# get machines names and id that can deploy VM
# ./getPodsMacchines name and id
PROFILE=admin
mypods=($(maas $PROFILE pods read   | grep "name" | grep -v "default" | grep -v "maas" | cut -d ":" -f 2 | cut -d "," -f 1))
for pod in "${mypods[@]}"
do
    maas $PROFILE pods read | jq '.[] | select (.name=='${pod}') | .name, .id' \
        | awk  'BEGIN{ RS = "" ; FS = "\n" }{print $1 " : "  $2}' \
               >> podsIds.txt
done

