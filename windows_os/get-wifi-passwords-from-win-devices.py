#!/usr/bin/env python
# coding: utf-8

####################################################################################################################
#The script gets all WiFi SSIDs and the passwords stored from a Windows device                                     #
#Important: The Terminal was written in pt-BR, so make sure to adapt the regular expressions used in this script   #
####################################################################################################################
#Libs:
#Importing subprocess lib, allow us to run system commands
import subprocess
#Importing re module, allow us to use regular expressions
import re


#save into a variable string the content output from the system command line 'netsh wlan show profiles'
terminal_output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout

#print(terminal_output.decode("utf-8", "ignore"))


#find all the wifi names which are listed after 'Todos os Perfis de Usuários: ' (ignoring special string)
profile_names = (re.findall("Todos os Perfis de Usurios: (.*)\r", terminal_output.decode("utf-8", "ignore")))
#print(profile_names)

#Prints all wifi saved in this device
print("\n========================================================================\n")
print(str(len(profile_names)) + " WiFi SSIDs were found on this device..\n")


#Empty list to store the wifi profiles and passwords
wifi_list = []

#check if there's no wifi connections found/catched
#In case of success, we check more details of the wifi connection and see whether we can get their passwords
if len(profile_names) != 0:
    for name in profile_names:
        #creating a empty dictionary
        wifi_connections = {}
        
        #save into a variable string the content output from the system command line 'netsh wlan show profile *name*'
        profile_info = subprocess.run(['netsh', 'wlan', 'show', 'profile', name], capture_output = True).stdout
        #print(profile_info.decode("utf-8", "ignore"))
        
        #using the regular expression to only look for the absent cases, in order to ignore them
        if re.search("Chave de segurana           : No Presente", profile_info.decode("utf-8", "ignore")):
            continue
        else:
            #in present cases, we'll grab the wifi name and password and put it into the dictionary
            wifi_connections["wifi_name"] = name
            #adding key=clear in order to get the password
            profile_info_pass = subprocess.run(['netsh', 'wlan', 'show', 'profile', name, "key=clear"], capture_output = True).stdout
            #print(profile_info_pass.decode("utf-8", "ignore"))
            password = re.search("Contedo da Chave            : (.*)\r", profile_info_pass.decode("utf-8", "ignore"))
            #If there's no password insert 'None' value into the dictionary
            if password == None:
                wifi_connections["password"] = None
            else:
                wifi_connections["password"] = password[1]
        wifi_list.append(wifi_connections)


#Prints all the wifi and passwords saved in this list
for x in range(len(wifi_list)):
    print(wifi_list[x]) 

