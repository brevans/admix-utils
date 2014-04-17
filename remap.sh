#!/bin/bash
#reformat plink-friendly map to more informative from SC1.2_123 into proper columns
num=$( wc -l $1 | awk '{print $1}' )
paste <( awk '{print $2}' $1 | awk -F"_" '{print $1}' | awk -F"." '{print $2}' ) <( awk '{print $2}' $1 ) <( yes 0 | head -n $num ) <( awk '{print $2}' $1 | awk -F"_" '{print $2}' )
