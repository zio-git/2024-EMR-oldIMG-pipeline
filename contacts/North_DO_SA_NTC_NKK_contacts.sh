#!/bin/bash --login
#cluster=1
cd "${WORKSPACE}"
echo "_________________________________________________________"
echo "Adding recipients list"
echo "_________________________________________________________"

sed -i '33d' core_shippingx.py
sed -i '32 arecipients = ["+265995246144", "+265998006237", "+265998276712", "+265992182669", "+265991450316", "+265888231289", "+265992268777", "+265882890008", "+265993030442", "+265996963312", "+265998555333", "+265996146325", "+265996131060"]' core_shippingx.py

sed -i '33d' api_shippingx.py
sed -i '32 arecipients = ["+265995246144", "+265998006237", "+265998276712", "+265992182669", "+265991450316", "+265888231289", "+265992268777", "+265992890008", "+265993030442", "+265996963312", "+265998555333", "+265996146325", "+265996131060"]' api_shippingx.py

# Editing email notification file
sed -i '9d' email_notification.py
sed -i '8 aemail_recipients = ["zmwakanema@pedaids.org", "oonions@pedaids.org", "willmbowe@gmail.com", "tlwara@pedaids.org", "domstig248@gmail.com", "mnaboti@pedaids.org", "jmakhuva@linmalawi.org", "pmasangano@linmalawi.org", "sam@pihmalawi.com", "egulule@pihmalawi.com", "mnkhoma@linmalawi.org", "gchibambo@linmalawi.org"]' email_notification.py

sed -i '10d' email_notification.py
sed -i '9 asubject = "Auto Deployment Status -Dowa -Salima -Ntchisi -Nkhotakota"' email_notification.py


#sed -i "40 acluster = get_xi_data('http://10.44.0.52:8000/sites/api/v1/get_single_cluster/$cluster')" core_shippingx.py
