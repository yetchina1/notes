
#!/bin/bash
if ls $1  > /dev/null
then
:
else "echo $1 does not exist"
exit
fi
