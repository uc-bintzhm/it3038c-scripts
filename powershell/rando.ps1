﻿$RANDO=0
$Logfile = "C:\Users\madis\OneDrive\Documents\it3038c-scripts\logs\rando.log"

for($i=0; $i -lt 5; $i++){
    $RANDO=Get-Random -Maximum 1000 -Minimum 1
    Write-Host($RANDO)
    Add-Content $Logfile "INFO: Random number is ${RANDO}"
}
