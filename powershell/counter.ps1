$Machines = 'MBINTZ-PC'
$Logfile = "C:\Users\madis\OneDrive\Documents\it3038c-scripts\logs\counterdata.log"
Foreach ($machine in $Machines)
{
#$RCounters = Get-Counter -ListSet * -ComputerName $machine
#“There are {0} counters on {1}” -f $RCounters.count, ($machine)
$pt = (Get-Counter -Counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 3).CounterSamples.CookedValue
    $sample = 1
    foreach ($p in $pt) {
        "Sample {2}: CPU is at {0}% on {1}" -f [int]$p, $machine, $sample | Out-File -Append $Logfile
        $sample++
    }
}


