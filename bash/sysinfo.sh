#!/bin/bash
#create a script that emails us our user, IP, hostname, and date

emailaddress=bintzhm@mail.uc.edu
today=$(date +"%d-%m-%Y %H:%M:%S")
ip=$(ip a | grep 'dynamic ens192' | awk 'print $2}')
servername=$(hostname)

content="User $USER
Server name is $servername
IP address is $ip
Date and Time is $today"
echo "Email will contain: $content"

mail -s "IT3038C Linux IP" $emailaddress <<< $(echo -e $content)