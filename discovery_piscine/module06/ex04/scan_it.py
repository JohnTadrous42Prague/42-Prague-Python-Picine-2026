import sys , re
x = len(sys.argv)-1
if x==2:
    result = re.findall(sys.argv[1],sys.argv[2])
    print(len(result))
else:
    print("none")