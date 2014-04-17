#!/bin/bash
cwd=$(pwd)
for i in $(seq -f"%02g" $1)
do
    echo "cd $cwd; /home/be59/bin/admixture --cv=10 $2 $i -j8 > ${2/.ped/}_k$i.log 2>&1;"
done
