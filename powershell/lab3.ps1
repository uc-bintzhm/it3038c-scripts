function getIP {
    (get-NetIPAddress).IPv4Address | Select-String "192*"
}
$IP = getIP
$User = $env:username
$Date = Get-Date -DisplayHint Date
$Hostname = hostname
$PWSH = $HOST.Version.Major

$Body = "This machine's IP address is $IP. User is $User. Hostname is $Hostname. Powershell version is $PWSH. Today's date is $Date"

write-host($Body)