import sys

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
        to = getUniqueArg('to',arglist)
        content = getUniqueArg('content',arglist)
        curl = ('curl https://api.zulip.com/v1/messages -u '
               + self.getEmail() + ':' + self.getKey()
               + '-d "type=private" '
               + '-d "to=' + to + '" '
               + '-d "content=' + content +'"')
        curlprint(curl)


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
        return (a[:i-1],a[i:]) # 'x=y' -> ('x','y')
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
    return {'set_email':Client.setEmail(args),  
            'set_key'  :Client.setKey(args),
            'msg'      :Client.sendMsg(args)
    }[cmd]


def curlprint(curl):
    for c in curl:
        if c=='-':
            sys.stdout.write('\n')
        sys.stdout.write(c)
    sys.stdout.write('\n')

if __name__=='__main__':
    args = [sys.argv[i] for i in range(len(sys.argv)) if i]
    cmd  = args.pop(0)
    a    = Client()
    result = dispatcher(a,cmd,args)
    
# # Send a private message
# client.send_message({
    # "type": "private" | "stream",
    # "to": "hamlet@example.com",
    # "subject": "hrtz" # stream messages only
    # "content": "I come not, friends, to steal away your hearts."
# })
