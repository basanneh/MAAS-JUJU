#!/bin/bash

# to get information compact of the nodes in maas
# include VM and Metal boxes output
# {"hostname":"node1","system_id":"dfgnnd","status":4}

maas admin machines read | jq ".[] |  {hostname:.hostname, system_id: .system_id, status:.status}" --compact-output

