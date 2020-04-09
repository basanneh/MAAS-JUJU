#!/bin/bash
if [ $# -ge 1 ]; then
    while read studentAndEndDate; do
        student=$(echo $studentAndEndDate | cut -f1 -d'|' | tr -d [:space:])
        endDate=$(echo $studentAndEndDate | cut -f2 -d'|' | tr -d [:space:])
        #studentdir=/home/SharedStorage2/dsclass/$student    
        #studentdir=/home/SharedStorage2/$student
	#studentdir=/home/SharedStorage2/$student
	studentdir=/home/$student
        echo "adding user $student until $endDate on dir $studentdir"
        pass=$(perl -e 'print crypt($ARGV[0], "password")' $student)
        #useradd $student --create-home --expiredate $endDate  --shell /bin/bash --password $pass
        useradd $student -m --home-dir $studentdir --expiredate $endDate  --shell /bin/bash --password $pass
        chage  --expiredate $endDate  $student
    done < $1
else
    echo "usage: <this>  netidsource[file] "
fi
