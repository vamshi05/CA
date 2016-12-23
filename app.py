from collections import defaultdict
import sys
import re

#Command line arguments
lines = sys.argv[1]
dependon={}
installed=[]
#function to perform DEPEND operation
def depend(argList): #Takes each argument line as a list
    dependon[argList[1]]=[]
    for i in range(2,len(argList)):
        dependon[argList[1]].append(argList[i])
    argList = ' '.join(argList)
    print argList
    return dependon

def install(argList):
    for i in range(1,len(argList)):
        if argList[i] not in installed:
            for dependants in dependon.values():
                for value in dependants:
                    if value == argList[i]:
                        if argList[i] not in installed:
                            print "   Installing " + ''.join(argList[i])
                            installed.append(argList[i])
                            break
                else:
                    continue
            compList = dependon[argList[i]]
            for components in compList:
                if components not in installed:
                    if argList[i] not in installed:
                        print "   Installing " + ''.join(argList[i])
                        installed.append(argList[i])
                    else:
                        continue
                else:
                    continue
        else:
            if argList[i] not in installed:
                print "   Installing " + ''.join(argList[i])
                installed.append(argList[i])
                break

    argList = ' '.join(argList)
    return argList


def remove(argList):
    print "Removing\n  ", installed.remove(argList[1])


def list():
     print "LIST\n   ",installed



print "\n\nOUTPUT \n"

for line in lines.splitlines():
    argList = re.sub("[^\w]", " ",  line).split()
#    print argList
    if argList[0]=="DEPEND":
        dictofdepends={}
        dictofdepends = depend(argList)
    if argList[0] == "INSTALL":
        print ' '.join(argList)
        install(argList)
    if argList[0] == "REMOVE":
        remove(argList)
    if argList[0] == "LIST":
        list()
#    else:
#        print "OPERATION NOT SUPPORTED!!!\nExpected operations are: DEPEND, INSTALL, REMOVE, LIST"

