import requests
import json
import platform
import subprocess
import os
import time
from dotenv import load_dotenv
load_dotenv()

def get_xi_data(url):
    response = requests.get(url)
    data = json.loads(response.text)
    data = data[0]['fields']
    return data



def alert(url, params):
    """send SMS alert"""
    try:
        headers = {
            'Content-type': 'application/json; charset=utf-8',
            'Authorization': 'Token fe722faaa8f09438c79e70b2564729d9d1026027'
        }
        r = requests.post(url, json=params, headers=headers)
        print("SMS sent successfully")
    except Exception as e:
        print("Failed to send SMS with exception:", e)
        return False
    return True


recipients = ["+265995246144", "+265998006237", "+265998276712", "+265992182669", "+265991450316", "+265888231289"]
cluster = get_xi_data('http://10.44.0.52:8000/sites/api/v1/get_single_cluster/3')

for site_id in cluster['site']:
    site = get_xi_data('http://10.44.0.52:8000/sites/api/v1/get_single_site/' + str(site_id))

    # Functionality for ping retries
    count = 0
    max_attempts = 3
    success = False
    #REMOTE_PATH="/var/www/APK-FILE"

    while count < max_attempts:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        if subprocess.call(['ping', param, '1', site['ip_address']]) == 0:
            success = True
            break
        else:
            count += 1
            time.sleep(1)  # Wait for 1 second before retrying

    if success:
         # check if APK Exist
        check_apk_file = f"ssh {site['username']}@{site['ip_address']} 'if [ -f :/var/www/EMR-APK ]; then echo 'File exists, deleting it...'; rm :/var/www/EMR-APK; else echo 'APK File not found'; fi'"
        os.system(check_apk_file)

        # Ship API script to remote site
        push_core_script = f"rsync -r EMR-APK {site['username']}@{site['ip_address']}:/var/www && echo 'APK File transfer complete...'"
        os.system(push_core_script)

        # Write site to file
        updated_site = f"{site['name']}----------CORE-APK\n"
        with open("updated_sites.txt", "a") as f:
            f.write(updated_site)
    else:
        # Write site to failed file
        notupdated_site = f"{site['name']}----------CORE-APK\n"
        with open("failed_sites.txt", "a") as f:
            f.write(notupdated_site)
        
        # Send alert
        #for recipient in recipients:
         #   params = {
          #      "to": recipient,
           #     "message": f"Failed to update site {site['name']} after {max_attempts} attempts."
            #}
            #alert('http://your-sms-api-endpoint', params)

    print(f"Processing site {site['name']} completed.")

