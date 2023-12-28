#!/bin/bash
#display all the arguments each one at a time by shifting the arguments using "shift" commnad.
#while($#) evaluates to true, continue the loop and shift.
#If no arguments passed, dispaly a message to pass at least one commnad and then exit
if [ "$#" == "0" ] ;
 then 
 echo Pass at least one argument
 exit 1
fi

while (($#)) ;
 do
  echo you gave me $1
  shift
 done
 