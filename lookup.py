import csv
import os
import sys
#for PUK codes
def puksearch():
    pukcsv = open('./csv/pukcodes.csv')
    puklist = csv.reader(pukcsv)
    valuepuk = input('Enter IMSI or ICCID for PUK codes: ')
    for row in puklist:
        if valuepuk in row:
            print (" ICCID: " + row[0] + " IMSI: " + row[1] + " Pin1: " + row[2] + " PUK1: " + row[3] + " Pin2: " + row[4] + " PUK2:" + row[5])
#for dlinks
def dlinksearch():
    dlinkcsv = open('./csv/dlink.csv')
    dlinklist = csv.reader(dlinkcsv)
    valuedlink = input('Enter IMEI, Wifi Key or Config PW: ')
    for row in dlinklist:
        if valuedlink in row:
            print (" SSID: " + row[0] + " IMEI: " + row[1] + " Wifi Key: " + row[2] + " Config PW: " + row[3])

#for fixed sims
def simsearch():
    fixedsims = open('./csv/fixedsims.csv')
    fixedreader = csv.reader(fixedsims)
    valuesim = input('Enter ICCID, IMSI or MSISDN: ')
    for row in fixedreader:
        if valuesim in row:
            print (" ICCID: " + row[0] + " IMSI: " + row[1] + " MSISDN: " + row[2] + " activation code: " + row[3])
#for bec
def becsearch():
    bec = open('./csv/bec.csv')
    becreader = csv.reader(bec)
    valuebec = input('Enter IMEI or Serial Number: ')
    for row in becreader:
        if valuebec in row:
            print (" IMEI: " + row[0] + " SSID: " + row[1] + " Wifi Key: " + row[2] + " Config Password: " + row[3] + " Serial Number: " + row[4])

#option to choose which function to run
while True:
    option = input("choose puk, dlink, bec, or simsearch:")
    if option == 'puk':
        puksearch()
    elif option == 'dlink':
        dlinksearch()
    elif option == 'simsearch':
        simsearch()
    elif option == 'bec':
        becsearch()
    elif option == 'quit':
        break
    else:
        print("try again")
