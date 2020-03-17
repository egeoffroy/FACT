#!/usr/bin/python3

#create files that identify significant hits with RCP > 0.5
#will need to be updated but general program here.

def InputFiles():
    with open('resultsFile.txt') as results:
        data = results.read()
    for line in data:
        #if RCP < 0.5
        #need to know what summary file looks like



