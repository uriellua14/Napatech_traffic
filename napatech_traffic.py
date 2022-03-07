import os.path
from re import I
import time
import subprocess

'''
Description: Runs stress in napatech Smart NIC usings, will run random pachage sizes at the SFP speed. 
            Uses Monitoring to check for package erros and profiling to log temperature 
Requirements: 

    - Napatech test suite
    - Loop back with fiber 
    - (coming) DSS Tools Setup_Thermals_ADC (scripts to save logs are there)
'''
# 1 = 1hour for time
traffic_time=1
traffic_time_seconds= traffic_time * 3600
#need to be variables because of conflict with ""
keep = 'gnome-terminal --tab -e \"/bin/bash -c \'/root/napatech_traffic.py; exec /bin/bash -i\'\"'
command = '/opt/napatech3/bin/ntload.sh'
command1 = '/opt/napatech3/bin/ntservice'
command2 = '/opt/napatech3/bin/ntpcap_capture -i napa1'
command3 = '/opt/napatech3/bin/ntpcap_capture -i napa0'
command4 = '/opt/napatech3/bin/pktgen -p 0 -n 0 -s 64:10000 -r 0 -t empty'
command5 = '/opt/napatech3/bin/pktgen -p 1 -n 0 -s 64:10000 -r 0 -t empty'
command6 = '/opt/napatech3/bin/monitoring'
command_kill = '/opt/napatech3/bin/ntstop.sh'
#maybe add later 
#testdata_1 = '/root/scripts/napa_mon.sh'
#testdata_2 = '/root/scripts/napa_monitor.sh'



if __name__ == '__main__':
#check for folder for folder to save napa_mon.sh data (not working)
#    if not os.path.isdir('/root/testdata/'): 
#        os.system("mkdir /root/testdata")
#    if not os.path.isdir('/root/testdata_old'):
#        os.system("mkdir /root/testdata_old")
#start ntservice
    subprocess.call(['gnome-terminal', '-e',str(keep)])
    subprocess.call(['gnome-terminal', '--', command])
    subprocess.call(['gnome-terminal', '--', command1])
#wait for nt service to start
    time.sleep(15)
#start traffic
    subprocess.call(['gnome-terminal', '-e',str(command2)])
    time.sleep(1)
    subprocess.call(['gnome-terminal', '-e',str(command3)])
    time.sleep(1)
    subprocess.call(['gnome-terminal', '-e',str(command4)])
    time.sleep(1)
    subprocess.call(['gnome-terminal', '-e',str(command5)])
    time.sleep(1)
    subprocess.call(['gnome-terminal', '-e',str(command6)])

    print("Starting Ramdom Package traffic...(1h)")
#for 1 hour
    
    os.system('/opt/napatech3/bin/monitoring')
#option to kill it after ab hour?
#    time.sleep(traffic_time_seconds)

#    subprocess.call(['gnome-terminal', '--', command_kill])
#    print("Traffic completed")
