import sys, os, json, fileinput

class Client:
    def __init__(self):
        pass
    def setEmail(self,args):
        email=args[0] # add warning for ignored args
        setData('email.txt',email)
    def setKey(self,args):
        key=args[0] # add warning for ignored args
        setData('key.txt',key)
    def getEmail(self):
        return getData('email.txt')
    def getKey(self):
        return getData('key.txt')
    def sendMsg(self,args):
        arglist = [getTupleArg(x) for x in args]
        print(arglist)
        if hasArgument('stream',arglist):
            self.sendStreamMsg(arglist)
        elif hasArgument('to',arglist):
            self.sendPrivateMsg(arglist)
        else:
            raise ValueError('You must supply either "stream" or "to" '
                            +'arguments when using msg. ')
    def sendPrivateMsg(self,arglist):
        to=getUniqueArg('to',arglist)
        content = getUniqueArg('content',arglist)
        curl = ('curl https://api.zulip.com/v1/messages -u '
               + self.getEmail() + ':' + self.getKey() + ' '
               + '-d "type=private" '
               + '-d "to=' + to + '" '
               + '-d "content=' + content +'" '
               + '-o output.txt') 
        makeRequest(curl)
    def sendStreamMsg(self,arglist):
        stream=getUniqueArg('stream',arglist)
        content = getUniqueArg('content',arglist)
        curl = ('curl https://api.zulip.com/v1/messages -u '
               + self.getEmail() + ':' + self.getKey() + ' '
               + '-d "type=stream" '
               + '-d "to=' + stream + '" '
               + '-d "content=' + content +'" '
               + '-o output.txt') 
        makeRequest(curl)

def makeRequest(x):
    # probably shouldn't be doing any of this with curl. urllib2 or requests...
    os.system(x)

def hasArgument(typestr,arglist):
    argtypes = [x for (x,y) in arglist]
    if typestr in argtypes:
        return True
    return False

def getUniqueArg(name,arglist):
    matches = [(n,val) for (n,val) in arglist if n==name]
    if not matches:
        raise ValueError(name+' is a mandatory argument.')
    elif len(matches)>1:
        raise ValueError('Only one '+name+' can be supplied as arguments.')
    else:
        return matches[0][1]

def getTupleArg(a):
    if a.find('=') != -1:
        i=a.find('=')
        return (a[:i],a[i+1:]) # 'x=y' -> ('x','y')
    else: 
        return ('content',a)
    print(a)

def setData(filename,content):
    with open(filename,'w+') as f:
        f.write(content)

def getData(filename):
    with open(filename,'r') as f:
        content = f.read().replace('\n','').replace(' ','')
    if content:
        return content
    sys.stdout.write('Error! no content in file '+filename)
    raise ValueError
        
def dispatcher(Client,cmd,args):
    if cmd=='set_email':
        return Client.setEmail(args)
    elif cmd=='set_key':
        return Client.setKey(args),
    elif cmd=='msg':
         return Client.sendMsg(args)

def curlprint(curl):
    for c in curl:
        if c=='-':
            sys.stdout.write('\n')
        sys.stdout.write(c)
    sys.stdout.write('\n')

if __name__=='__main__':
    args = [sys.argv[i] for i in range(len(sys.argv)) if i]
    try:
        cmd  = args.pop(0)
    except IndexError:
        raise IndexError("zlp.py must be run with command line arguments.")
    a = Client()
    result = dispatcher(a,cmd,args)

