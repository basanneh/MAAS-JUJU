#!/bin/bash
# ping the VM in the private network
# give the lower and upper range of the subnet
# pingsubnet 172.16.2 90 95
usage="$(basename "$0") [-h] [s l u] -- program ping range subnet

where:
     s = subnet three nums ex 172.16.2
     l = lower num of the range in the subnet ex 90 
     u = upper num of the range in the subnet ex 95"

pingSubnet(){
    for i in $(seq $l $u); do
        ip=${s}.${i}
        echo "ping ${ip}"
        ping -c 1 ${ip} &> /dev/null && echo success || echo fail
    done
}

if [ $# == 0 ] ; then
    echo "$usage"
    exit 1;
fi
s=$1
l=$2
u=$3
while getopts "h" option; do
	  case "$option" in
		  "h") echo "$usage"
			 exit
			 ;;
	  esac
done

pingSubnet
