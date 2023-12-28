
#!/bin/bash
ls shift.sh && cp andpipe.sh ~/tmp
diff shift.sh andpipe.sh || echo "file A and fileB are different"
