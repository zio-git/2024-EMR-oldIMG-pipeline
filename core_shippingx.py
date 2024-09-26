import requests
import json
import platform
import subprocess
import os
import subprocess as sp
from fabric import Connection
from dotenv import load_dotenv
import time
load_dotenv()
 
def get_xi_data(url):
    response = requests.get(url)
    data = json.loads(response.text)
    data = data[0]['fields']
    return data

def alert(url, params):
    """send sms alert"""
    try:
        headers = {
                'Content-type': 'application/json; charset=utf-8', 
                'Authorization': 'Token fe722faaa8f09438c79e70b2564729d9d1026027'
                }
        r = requests.post(url, json=params, headers=headers)
        print("SMS sent successfully")
        
    except Exception as e:
        print("Failed to send SMS with exception: ", e)
        return False
    return True

recipients = ["+265995246144", "+265998006237", "+265998276712", "+265992182669", "+265991450316", "+265888231289"]
cluster = get_xi_data('http://10.44.0.52:8000/sites/api/v1/get_single_cluster/3')

for site_id in cluster['site']:
    site = get_xi_data('http://10.44.0.52:8000/sites/api/v1/get_single_site/' + str(site_id))

    # functionality for ping re-tries
    count = 0
    max_attempts = 3
    success = False

    while count < max_attempts:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        if subprocess.call(['ping', param, '1', site['ip_address']]) == 0:
            success = True
            break
        else:
            count += 1
            time.sleep(1)  # Wait for 1 second before retrying

    if success:                                               
            # ship api script to remote site
            push_core_script = "rsync " + "-r core_setup.sh " + site['username'] + "@" + site['ip_address'] + ":/var/www/HIS-Core"
            os.system(push_core_script)
            
            # run setup script
            run_core_script = "ssh " + site['username'] + "@" + site['ip_address'] + " 'cd /var/www/HIS-Core && ./core_setup.sh'"
            os.system(run_core_script)
            
            result = Connection("" + site['username'] + "@" + site['ip_address'] + "").run('cd /var/www/HIS-Core && git describe', hide=True)
            msg = "{0.stdout}"
            version = msg.format(result).strip()   

            core_version = sp.getoutput('cd HIS-Core-release && git describe')
            #print (core_version)

            if core_version == version:
                # write site to file
                updated_site= "" +site['name'] + "----------CORE\n"
                with open("updated_sites.txt", "a") as f:
                    for word in updated_site:
                        f.writelines(word)
                                            
            else:
                # write site to file
                notupdated_site= "" +site['name'] + "----------CORE\n"
                with open("failed_sites.txt", "a") as f:
                    for word in notupdated_site:
                        f.writelines(word)

    else:
        failled_site= "" +site['name'] + "----------CORE\n"
        with open("unreachable_sites.txt", "a") as f:
            for word in failled_site:
                f.writelines(word)

    print(f"Processing site {site['name']} completed.")

