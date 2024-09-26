#!/bin/bash --login
echo "pulling and Checkout API tag"
echo "--------------------------------------------"
git fetch --tags jenkins@10.44.0.51:/var/lib/jenkins/workspace/2024-POC-Pipeline-Old-IMG/BHT-EMR-API -f
git checkout v5.0.4 -f
git describe > HEAD
echo "____________________________________________"
echo "ruby setup"
echo "____________________________________________"
rvm use ruby-3.2.0
echo "____________________________________________"
echo "Installing Local Gems"
echo "____________________________________________"
bundle install --local
echo "--------------------------------------------"
#rm -rf /var/www/BHT-EMR-API/db/migrate/20221112075527_create_lims_acknowledgement_statuses.rb
echo "running bin_update art"
echo "____________________________________________"
./bin/update_art_metadata.sh development
echo "____________________________________________"
