import sys , re
x = len(sys.argv)-1
if x>0:
    result = re.findall("z",str(sys.argv))
    if len(result)>0:
        print("z"*len(result))
    else:
        print("There isn't any ""z"" in this")
else:
    print("none")