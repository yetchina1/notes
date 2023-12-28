#!/bin/bash
echo "please enter a directory name"
read dir
while [ $dir ] 
do
if [ ! -d "$dir" ]
then
echo " this is not a directory, pleae enter a direcotry:"
read dir
continue
fi 
if [ `ls $dir | wc -l` -gt 10 ]
then
echo "This is a very big direcotry. exiting..."
break
fi
echo " this directory had less than 10 files"
echo "enter the a direcory name..to exit of this loop, you have to enter a directory whihc has more than 10 files."
read dir
done 
