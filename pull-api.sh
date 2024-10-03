#!/bin/bash --login
[ -d "BHT-EMR-API" ] && echo "API already cloned." || git clone https://github.com/HISMalawi/BHT-EMR-API.git
cd "$WORKSPACE" && chmod 777 BHT-EMR-API
cd BHT-EMR-API && git fetch --tags
git checkout v5.3.0-beta -f
