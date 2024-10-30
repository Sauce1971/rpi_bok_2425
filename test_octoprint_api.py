import requests
import time
from datetime import datetime


def connect():
    import network
    ssid = 'DATO IOT'
    password = 'Admin:123'
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        time.sleep(1)
        
#connect()

headers= {'X-Api-Key':'C008FA50B3574215BC2D6704636F537A'}
printer_url = 'http://10.13.37.26/api/'
job_url = printer_url + 'job'

#print(job_url)
r = requests.get(job_url, headers=headers)
#print(r.status_code)
data = r.json()
#print(data)
# Konverterer til 2 desimaler
completion = "{:.2f}".format(data['progress']['completion'])
from datetime import datetime
# Konverterer fra en unix timestamp til python datetime
file_date = datetime.fromtimestamp(data['job']['file']['date'])

print('Completion:          ', completion, '%')
print('File date:           ', file_date)

print('Estimated Print time:', data['job']['estimatedPrintTime'])
print('File:                ', data['job']['file']['name'])
print('Status:              ', data['state'])

# Oppgave
"""
1. Plukk opp de andre data fra data variablen'
Dokumentasjon: https://docs.octoprint.org/en/master/api/job.html#retrieve-information-about-the-current-job
Direkte lenke mot printer: http://10.13.37.26/api/job?apikey=C008FA50B3574215BC2D6704636F537A
"""

# Sjekk på om jobben eventuelt er ferdig
"""
previous_state = ''
while True:    
    if previous_state == 'Printing' and data['state'] != 'Printing':
        previous_state = data['state']
        print('Job finished')
        # Gjør noe når jobben er ferdig
    time.sleep(10)
"""        
    


