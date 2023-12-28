#!/bin/bash
for fname in *
do
if [ -x $fname ]
then
cp $fname bkps
fi
done

