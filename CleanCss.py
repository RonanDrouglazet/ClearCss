#! /usr/bin/python

###
 # @author RonanDrouglazet <ronan.drouglazet@ebuzzing.com>
 # @date 12-2013
###

import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

cssFile = open(inputFile, 'r')
cssFileTabLines = cssFile.readlines()

newCssFile = open(outputFile, 'w')
newCssFileTabLines = []

def lineExist(newLine):
    for line in newCssFileTabLines:
        if line == newLine:
            return True
    return False

cssFile.seek(0);

for line in cssFileTabLines:
    if lineExist(line) == False:
        newCssFileTabLines.append(line)
        newCssFile.write(line)

print >> sys.stdout, "CleanCss (clear dead css code)"
print >> sys.stdout, "Original : " + str(len(cssFileTabLines)) + " Css lines " + sys.argv[1]
print >> sys.stdout, "Cleaned  : " + str(len(newCssFileTabLines)) + " Css lines " + sys.argv[2]
print >> sys.stdout, "Total    : " + str(len(cssFileTabLines) - len(newCssFileTabLines)) + " Css lines removed (" + str(100 - (len(newCssFileTabLines) * 100 / len(cssFileTabLines))) + "% gain)"

cssFile.close()
newCssFile.close()
