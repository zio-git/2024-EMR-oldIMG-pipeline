#!/bin/bash --login
cluster=3
cd "${WORKSPACE}"
sed -i "34d" api_shippingx.py
sed -i "33 acluster = get_xi_data('http://10.44.0.52:8000/sites/api/v1/get_single_cluster/$cluster')" api_shippingx.py
sed -i "34d" core_shippingx.py
sed -i "33 acluster = get_xi_data('http://10.44.0.52:8000/sites/api/v1/get_single_cluster/$cluster')" core_shippingx.py

# clear files
truncate -s 0 updated_sites.txt
truncate -s 0 unreachable_sites.txt
truncate -s 0 failed_sites.txt
