import sys, requests, json, fileinput

# create custom OptionError to replace ValueError 
# decide when to registerEventQueue 
# do something with the results of these requests!

class Client:
    def __init__(self):
        pass
    def setEmail(self,args):
        if len(args)>1:
            warnIgnoredArgs(args[1:])
        email=args[0] 
        setData('email.txt',email)
    def setKey(self,args):
        if len(args)>1:
            warnIgnoredArgs(args[1:])
        key=args[0] 
        setData('key.txt',key)
    def getEmail(self):
        return getData('email.txt')
    def getKey(self):
        return getData('key.txt')
    def setQueueID(self,queue_ID):
        setData('queue_id.txt',queue_ID)
    def setLastEventID(self,lastEvent_ID):
        setData('last_event_id.txt',lastEvent_ID)
    def getQueueID(self):
        return getData('queue_id.txt')
    def getLastEventID(self):
        return getData('last_event_id.txt')
    def registerEventQueue(self):
        pass
    def sendMsg(self,args):
        arglist = [getTupleArg(x) for x in args]
        login = (self.getEmail(),self.getKey())
        parameters = dict()
        if hasArg('stream',arglist):
            parameters['type'] = 'stream'
            parameters['to'] = getUniqueArg('stream',arglist)
            parameters['subject'] = getUniqueArg('subj',arglist)
            
        elif hasArg('to',arglist):
            parameters['type'] = 'private'
            parameters['to'] = getUniqueArg('to',arglist)
        parameters['content'] = getUniqueArg('content',arglist)
        r = requests.post('https://api.zulip.com/v1/messages',auth=login,params=parameters)
    def getNews(self,args):
        login = (self.getEmail(),self.getKey())
        parameters = dict()
        parameters['queue_id'] = self.getQueueID()
        parameters['last_event_id'] = self.getLastEventID()
        # if dont_block is omitted, zulip wont respond until there's a new event
        parameters['dont_block'] = 'true' 
        r = requests.get('https://api.zulip.com/v1/events',auth=login,params=parameters)
    def getHistory(self,args):
        login = (self.getEmail(),self.getKey())
        r = requests.get('https://api.zulip.com/v1/export')
        
def warnIgnoredArgs(ignoredArgs):
    print('Warning: the following arguments were unused:')
    for arg in ignoredArgs:
        print('   '+arg)
        
def isValidMsg(args):
    if hasArg('stream') and hasArg('subject') and hasArg('content'):
        return True
    if hasArg('to') and hasArg('content'):
        return True
    raise ValueError("You must supply content in quotation marks ("+'""'+") and either a 'to' or 'stream' argument when using the msg command.")
    
def hasArg(typestr,arglist):
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
    ''' 'x=y' -> ('x','y') OR 'x' -> ('content','x') '''
    if a.find('=') != -1:
        i=a.find('=')
        return (a[:i],a[i+1:]) 
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
    return False
    
def dispatcher(Client,cmd,args):
    if cmd=='set_email':
        return Client.setEmail(args)
    elif cmd=='set_key':
        return Client.setKey(args),
    elif cmd=='msg':
         return Client.sendMsg(args)

if __name__=='__main__':
    args = [sys.argv[i] for i in range(len(sys.argv)) if i]
    try:
        cmd  = args.pop(0)
    except IndexError:
        raise IndexError("zlp.py must be run with command line arguments.")
    a = Client()
    result = dispatcher(a,cmd,args)

