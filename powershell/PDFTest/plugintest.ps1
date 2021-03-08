#The following comments shows how the plugin can create PDFs

#New-PDF {
#    New-PDFText -Text 'Hello World' -Font HELVETICA, TIMES_ITALIC -FontColor GRAY, BLUE -FontBold $true, $false, $true
#}-FilePath "C:\Users\madis\OneDrive\Documents\it3038c-scripts\powershell\PDFTest\test1.pdf" -Show

#New-PDF {
#    New-PDFText -Text 'This is my second PDF' -Font HELVETICA, TIMES_ITALIC -FontColor GRAY, BLUE -FontBold $true, $false, $true
#}-FilePath "C:\Users\madis\OneDrive\Documents\it3038c-scripts\powershell\PDFTest\test2.pdf" -Show

#The following comments shows how to merge PDFs

#$FilePath1 = "C:\Users\madis\OneDrive\Documents\it3038c-scripts\powershell\PDFTest\test1.pdf"
#$FilePath2 = "C:\Users\madis\OneDrive\Documents\it3038c-scripts\powershell\PDFTest\test2.pdf"
#$OutputFile = "C:\Users\madis\OneDrive\Documents\it3038c-scripts\powershell\PDFTest\merged.pdf"

#Merge-PDF -InputFile $FilePath1, $FilePath2 -OutputFile $OutputFile

#The following comments shows how to convert PDFs to  text

#Convert-PDFToText -FilePath "C:\Users\madis\OneDrive\Documents\it3038c-scripts\powershell\PDFTest\merged.pdf"