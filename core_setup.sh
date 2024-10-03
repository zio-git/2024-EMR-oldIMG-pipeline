#!/bin/bash --login
echo "pulling and Checkout Core tag"
echo "--------------------------------------------"
git fetch --tags jenkins@10.44.0.51:/var/lib/jenkins/workspace/2024-POC-Pipeline-Old-IMG/HIS-Core-release -f
git checkout v2024.Q3.R4 -f
#git describe > HEAD
echo "____________________________________________"
