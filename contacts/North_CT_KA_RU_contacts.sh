#!/bin/bash --login
#cluster=1
cd "${WORKSPACE}"
echo "_________________________________________________________"
echo "Adding recipients list"
echo "_________________________________________________________"

sed -i '33d' core_shippingx.py
sed -i '32 arecipients = ["+265995246144", "+265998006237", "+265998276712", "+265992182669", "+265991450316", "+265888231289", "+265888000187", "+265992268777", "+265993030442", "+265997762346", "+265996551261"]' core_shippingx.py

sed -i '33d' api_shippingx.py
sed -i '32 arecipients = ["+265995246144", "+265998006237", "+265998276712", "+265992182669", "+265991450316", "+265888231289", "+265888000187", "+265992268777", "+265993030442", "+265997762346", "+265996551261"]' api_shippingx.py

# Editing email notification file
sed -i '9d' email_notification.py
sed -i '8 aemail_recipients = ["zmwakanema@pedaids.org", "oonions@pedaids.org", "willmbowe@gmail.com", "tlwara@pedaids.org", "domstig248@gmail.com", "mnaboti@pedaids.org", "egulule@pihmalawi.com", "ewetzel@tingathe.org", "ishmaelmthuzi@gmail.com", "kmunyimbili@linmalawi.org", "kbanda@linmalawi.org"]' email_notification.py

sed -i '10d' email_notification.py
sed -i '9 asubject = "Auto Deployment Status - Chitipa -Karonga -Rumphi"' email_notification.py



#sed -i "40 acluster = get_xi_data('http://10.44.0.52:8000/sites/api/v1/get_single_cluster/$cluster')" core_shippingx.py
