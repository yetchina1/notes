if diff dollortest dollortest2 > /dev/null
then echo files are same
rm -f dollortest2
else
echo files are not same
diff dollortest dollortest2
fi
