# Name: Alyssa Richie
# CIS 41A Python Programming 50Z
# Description: Reads an error log and process the information to an output file and console
import os

print(os.getcwd())
OUT_FILE_NAME = "reportError.txt"

inFileName = input("Enter the name of the error log file: ")

try:
    inFile = open(inFileName, "r")
except:
    print("File cannot be opened:", inFileName)
    quit()

try:
    outFile = open(OUT_FILE_NAME, "w")
except:
    print("File cannot be opened:", inFileName)
    quit()

linesCount = 0
errorLinesCount = 0
for line in inFile:
    line = line.strip()
    if line != "":
        linesCount += 1

        if "error" in line or "Error" in line or "ERROR" in line:
            errorLinesCount += 1
            print(line)
            outFile.write(line)
            outFile.write("\n")

outFile.write("There are " + str(linesCount) + " lines in the file \n")
outFile.write("There are " + str(errorLinesCount) + " error lines in the file")
print("The total lines =", linesCount)
print("The total \"Error\" lines =", errorLinesCount)
inFile.close()
outFile.close()

'''
Output:

Enter the name of the error log file: ErrorLog.txt
[Sun Mar  7 21:16:17 2018] [error] [client 24.70.56.49] File does not exist: /home/httpd/twiki/view/Main/WebHome
[Mon Mar  8 07:27:36 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/_vti_bin/owssvr.dll
[Mon Mar  8 07:27:37 2018] [error] [client 61.9.4.61] File does not exist: /usr/local/apache/htdocs/MSOffice/cltreq.asp
[Thu Mar 11 02:27:34 2018] [error] [client 200.174.151.3] File does not exist: /usr/local/mailman/archives/public/cipg/2018-november.txt
[Thu Mar 11 07:39:29 2018] [error] [client 140.113.179.131] File does not exist: /usr/local/apache/htdocs/M83A
The total lines = 108
The total "Error" lines = 5

Invalid input Output
Enter the name of the error log file: Error.txt
File cannot be opened: Error.txt
'''