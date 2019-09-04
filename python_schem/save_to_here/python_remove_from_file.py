import sys
with open(sys.argv[1], 'r') as myfile:
    data=myfile.read().replace('m39[5B1]','')
print(sys.argv[1],sys.argv[2])
