import requests
import csv, json
import configparser


### SET Parameters ###
inifile = configparser.SafeConfigParser()
inifile.read('./config.ini')
username = inifile.get('settings', 'username')
password = inifile.get('settings', 'password')
controller_ip = inifile.get('settings', 'controller_ip')
config_path = inifile.get('settings', 'config_path')
base_url = "https://" + controller_ip + ":4343/v1/configuration/"


### Import AP Data from CSV ###
ap_list = []
with open('ap_data.csv', 'r') as f:
    for row in csv.DictReader(f):
        ap_list.append(row)


### SET UIDARUBA ###
url = "https://"+controller_ip+":4343/v1/api/login"
payload = "username="+username+"&password="+password
s = requests.session()
response = s.request("POST", url, data=payload, verify=False)
UIDARUBA=response.json()['_global_result']['UIDARUBA']


### READ Bootinfo ###
def prov_ap_read_bootinfo(ap_param):
    url = base_url + "object/prov_ap_read_bootinfo" 
    querystring = {"config_path":config_path,"UIDARUBA":UIDARUBA}
    body = "{\"wired-mac\":\"" + ap_param['wired-mac'] + "\"}"
    headers = {"Content-Type":"application/json"}
    response = s.request("POST", url, headers=headers, data=body, params=querystring, verify=False)
    return response.json()


### AP Provisioning ###
def ap_prov(ap_param):
    url = base_url + "object/ap_prov" 
    querystring = {"config_path":config_path,"UIDARUBA":UIDARUBA}
    body = "{ \
        \"ap_name\" : { \"ap-name\" : \"" + ap_param['ap_name'] + "\" }, \
        \"ap_group\" : { \"ap-group\" : \"" + ap_param['ap_group'] + "\" }, \
        \"ipaddr\" : { \"ipaddr\" : \"" + ap_param['ipaddr'] + "\" }, \
        \"netmask\" : { \"netmask\" : \"" + ap_param['netmask'] + "\" }, \
        \"gatewayip\" : { \"gateway\" : \"" + ap_param['gatewayip'] + "\"} \
        }"
    headers = {"Content-Type":"application/json"}
    response = s.request("POST", url, headers=headers, data=body, params=querystring, verify=False)
    return response.json()


### AP Reprovisioning ###
def ap_reprovision(ap_param):
    url = base_url + "object/ap_reprovision" 
    querystring = {"config_path":config_path,"UIDARUBA":UIDARUBA}
    body = "{\"wired-mac\":\"" + ap_param['wired-mac'] + "\"}"
    headers = {"Content-Type":"application/json"}
    response = s.request("POST", url, headers=headers, data=body, params=querystring, verify=False)
    return response.json()


### Run ###
for ap_param in ap_list:
    print(prov_ap_read_bootinfo(ap_param))
    print(ap_prov(ap_param))
    print(ap_reprovision(ap_param))



