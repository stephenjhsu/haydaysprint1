prefix=$1
cp -a srv/runme/$1/Raw.txt srv/runme/$1/Raw.txt-$(date +"%Y-%m-%dT%H%M%S%:z")
cp -a srv/runme/$1/proc.txt srv/runme/$1/proc.txt-$(date +"%Y-%m-%dT%H%M%S%:z")
rm srv/runme/$1/Raw.txt
rm srv/runme/$1/proc.txt
