The plugin PSWritePDF
======

# How it works

The plugin allows people to manipulate PDFs within powershell. This inlcudes editing, 

## Installation

Type the following code into Powershell

``` Install-Module PSWritePDF -Force ```

## Some examples of what it can do. 

### It can Create PDFs
Insert the following code to create a pdf, remembering to change the path to whatever is desired. This can also be added upon and developed however you like

```New-PDF {
    New-PDFText -Text 'Hello World' -Font HELVETICA, TIMES_ITALIC -FontColor GRAY, BLUE -FontBold $true, $false, $true
}-FilePath "[desired path]\[desired name].pdf" -Show
```

### It can merge PDFs
Insert this code to merge the two desired pdfs, changing the paths as needed for you. 

```
#$FilePath1 = "[path of pdf]\[pdf1].pdf"
#$FilePath2 = "[path of pdf]\[pdf2].pdf"
#$OutputFile = "[desired path]\merged.pdf"

#Merge-PDF -InputFile $FilePath1, $FilePath2 -OutputFile $OutputFile
```
### It can convert PDFs to text
Insert this code to convert whatever pdf you want into text, changing the path as needed. 
```
#Convert-PDFToText -FilePath "[path]\[pdf].pdf"
```

## Also

I committed and uploaded me testing this code to the following branch to see how this worked for me.
https://github.com/uc-bintzhm/it3038c-scripts/blob/main/powershell/PDFTest/plugintest.ps1'

I commented out everything as I went along, so all of the code is written in comments, but it did work and the pdfs were created. 
