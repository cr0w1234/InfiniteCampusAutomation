'''
Only prints if debugs are enabled, in THIS FILE RIGHT HERE
'''
debug_prints = True

def dprint(t,**args):
    #**args is list, need to unwrap
    if debug_prints:
        print(t,*args)
'''
# file printing cos why not
# slow as all heck for ease of use
def fprint(**args,file="output.txt"):
    path=os.getcwd()+"/"+str(file)
    try:
        open(path,"x").close()
    except:
        pass
    with open(path,"a") as fl:
        fl.write("\n"+" ".join([str(s) for s in text]))
        fl.close()
'''
