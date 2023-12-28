echo "please enter a file name: \c"
read fname
if [ -z "$fname" ]
then echo "please enter a filename"
elif test -f "$fname" -a -w "$fname"
then echo "Everything is fine"
else
echo "the file is not writable"
fi
