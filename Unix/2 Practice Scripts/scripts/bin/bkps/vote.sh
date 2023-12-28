#!/bin/bash
echo enter your age
read age
if [ $age -ge 18 ]; then
echo "you are elible to vote"
else
echo "sorry bro!"
fi
