#!/bin/bash --login
[ -d "HIS-Core-release" ] && echo "Core already cloned." || git clone https://github.com/HISMalawi/HIS-Core-release.git 
cd $WORKSPACE && chmod 777 HIS-Core-release
cd HIS-Core-release && git fetch --tags
git checkout v1.15.2 -f
