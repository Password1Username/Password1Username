#!/bin/bash
nx=$1
ny=$2
inname=$3
outname=$4
x=$(($nx*64))
y=$(($ny*40))
convert $inname -resize $(echo $x)x$(echo $y)\! $outname
